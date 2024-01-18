# Copyright (C) 2023  Andrea Patrizi (AndrePatri, andreapatrizi1b6e6@gmail.com)
# 
# This file is part of CoClusterBridge and distributed under the General Public License version 2 license.
# 
# CoClusterBridge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# CoClusterBridge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with CoClusterBridge.  If not, see <http://www.gnu.org/licenses/>.
# 
from abc import ABC

from control_cluster_bridge.controllers.rhc import RHChild
from control_cluster_bridge.utilities.control_cluster_defs import HanshakeDataCntrlSrvr
from control_cluster_bridge.utilities.defs import Journal
from control_cluster_bridge.utilities.cpu_utils import get_isolated_cores

from control_cluster_bridge.utilities.defs import jnt_names_rhc_name
from control_cluster_bridge.utilities.shared_mem import SharedStringArray

from typing import List

import multiprocess as mp
import os

from typing import TypeVar

ClusterSrvrChild = TypeVar('ClusterSrvrChild', bound='ControlClusterSrvr')

class ControlClusterSrvr(ABC):

    def __init__(self, 
            namespace = "",
            processes_basename: str = "controller", 
            use_isolated_cores = False,
            verbose: bool = False):

        # ciao :D
        #        CR 

        self.use_isolated_cores = use_isolated_cores # will spawn each controller
        # in a isolated core, if they fit
        self.distribute_over_cores = False

        self.isolated_cores = []

        self.namespace = namespace
        
        self.verbose = verbose

        self.journal = Journal()

        self.processes_basename = processes_basename

        self.cluster_size = -1

        self._device = "cpu"

        self._controllers: List[RHChild] = [] # list of controllers (must inherit from
        # RHController)

        self.handshake_srvr = HanshakeDataCntrlSrvr(verbose=self.verbose, 
                                        namespace=self.namespace)
        self.handshake_srvr.handshake()
        self.cluster_size = self.handshake_srvr.cluster_size.tensor_view[0, 0].item()

        self._processes: List[mp.Process] = [] 

        self._is_cluster_ready = False

        self._controllers_count = 0

        self.solution_time = -1.0
        
        self.jnt_names_rhc = None # publishes joint names from controller to shared mem
    
    def _close_processes(self):
    
        # Wait for each process to exit gracefully or terminate forcefully
                
        for process in self._processes:

            process.join(timeout=0.2)  # Wait for 5 seconds for each process to exit gracefully

            if process.is_alive():
                
                process.terminate()  # Forcefully terminate the process
            
            print(f"[{self.__class__.__name__}]" + f"{self.journal.status}" + ": terminating child process " + str(process.name))
    
    def _assign_process_to_core_idx(self, 
                process_index: int, core_ids: List[int]):

        num_cores = len(core_ids)

        return core_ids[process_index % num_cores]

    def _spawn_processes(self):

        print(f"[{self.__class__.__name__}]" + f"[{self.journal.status}]" + \
            ": spawning processes...")

        if self._controllers_count == self.cluster_size:
            
            if self.use_isolated_cores:

                self.isolated_cores = get_isolated_cores()[1] # available isolated
                # cores -> if possible we spawn a controller for each isolated 
                # core

                if not len(self.isolated_cores) > 0: 
                    
                    exception = "[{self.__class__.__name__}]" + f"[{self.journal.exception}]" + \
                        ": No isolated cores found on this machine. Either isolate some cores or " + \
                        "deactivate the use_isolated_cores flag."

                    raise Exception(exception)
                
            if len(self.isolated_cores) < self.cluster_size and self.use_isolated_cores:
                
                self.distribute_over_cores = True # instead of assigning each process to a separate core
                # we distribute the controllers over the available ones
                warning = f"[{self.__class__.__name__}]" + f"[{self.journal.warning}]" + \
                    ": Not enough isolated cores available to distribute the controllers " + \
                    f"on them. N. available cores: {len(self.isolated_cores)}, n. controllers {self.cluster_size}. "+ \
                    "Processes will be distributed among the available ones."
                
                print(warning)

                if not (self.cluster_size % len(self.isolated_cores) == 0):

                    cores_not_saturated_warn = f"[{self.__class__.__name__}]" + f"[{self.journal.warning}]" + \
                        f": the number of cluster controllers {self.cluster_size} is not a multiple of "+ \
                        f"the number of available isolated_cores "

                    print(cores_not_saturated_warn)
                
            for i in range(0, self.cluster_size):

                process = mp.Process(target=self._controllers[i].solve, 
                                    name = self.processes_basename + str(i))
                
                self._processes.append(process)
                
            # we start the processes and set affinity
            i = 0
            for process in self._processes:

                process.start()

                if self.use_isolated_cores:
                    
                    os.sched_setaffinity(process.pid, {self._assign_process_to_core_idx(i, self.isolated_cores)})

                    info = f"[{self.__class__.__name__}]" + f"[{self.journal.status}]" + \
                            f": setting affinity ID {os.sched_getaffinity(process.pid) } for controller n.{i}." 
                    
                    print(info)
                
                i = i + 1

            self._is_cluster_ready = True

            print(f"[{self.__class__.__name__}]" + f"[{self.journal.status}]" + ": processes spawned.")
                
        else:

            raise Exception(f"[{self.__class__.__name__}]" + f"[{self.journal.exception}]" + \
                    "You didn't finish to fill the cluster. Please call the add_controller() method to do so.")

    def _finalize_init(self):

        # steps to be performed after the controllers are fully initialized 

        print(f"[{self.__class__.__name__}]" + f"{self.journal.status}" + \
            ": performing final initialization steps...")
        
        self.handshake_srvr.finalize_init(add_data_length=self._controllers[0].add_data_lenght, 
                                    n_contacts=self._controllers[0].n_contacts)
        
        for i in range(0, self.cluster_size):

            # we assign the client-side joint names to each controller (used for mapping purposes)
            self._controllers[i].assign_client_side_jnt_names(self.handshake_srvr.jnt_names_client.read())

            self._controllers[i].create_jnt_maps()

            self._controllers[i].init_states() # initializes states

            self._controllers[i].set_cmds_to_homing() # safe cmds

            self._controllers[i].init_rhc_task_cmds() # initializes rhc commands

        # publishing joint names on shared memory for external use
        self.jnt_names_rhc = SharedStringArray(length=len(self._controllers[0].get_server_side_jnt_names()), 
                                name=jnt_names_rhc_name(), 
                                namespace=self.namespace,
                                is_server=True)

        self.jnt_names_rhc.start(init = self._controllers[0].get_server_side_jnt_names())

        print(f"[{self.__class__.__name__}]" + f"[{self.journal.status}]" + ": final initialization steps completed.")

    def add_controller(self, controller: RHChild):

        if self._controllers_count < self.cluster_size:

            self._controllers.append(controller)
            
            self._controllers_count += 1

            if self._controllers_count == self.cluster_size:
            
                self._finalize_init()
        
            return True

        if self._controllers_count > self.cluster_size:

            print(f"[{self.__class__.__name__}]" + f"[{self.journal.warning}]" + ": cannot add any more controllers to the cluster. The cluster is full.")

            return False
    
    def start(self):

        self._spawn_processes()

    def terminate(self):
        
        print(f"[{self.__class__.__name__}]" + f"[{self.journal.info}]" + ": terminating cluster")

        if self.jnt_names_rhc is not None:

            self.jnt_names_rhc.terminate()

        self._close_processes() # we also terminate all the child processes
