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
from abc import ABC, abstractmethod

from typing import List

import multiprocess as mp

from SharsorIPCpp.PySharsorIPC import Journal, LogType
from SharsorIPCpp.PySharsorIPC import VLevel

import signal

class ControlClusterClient(ABC):

    # This is meant to handle a cluster of controllers for a type of robot, 
    # where each controller is the same 
    # Different controllers (e.g. with different formulations, etc..) should
    # be handled by a separate cluster client 

    def __init__(self, 
            namespace: str,
            cluster_size: int,
            processes_basename: str = "Controller", 
            set_affinity: bool = False,
            use_mp_fork: bool = True,
            isolated_cores_only: bool = False,
            core_ids_override_list: List[int] = None,
            verbose: bool = False,
            debug: bool = False):

        # ciao :D
        #        CR 

        signal.signal(signal.SIGINT, self._handle_sigint)

        self.set_affinity = set_affinity

        self.use_mp_fork = use_mp_fork
        
        self.isolated_cores_only = isolated_cores_only # will spawn each controller
        # in a isolated core, if they fit
        self.core_ids_override_list = core_ids_override_list

        from control_cluster_bridge.utilities.cpu_utils.core_utils import get_isolated_cores
        self.isolated_cores = get_isolated_cores()[1] # available isolated
        # cores 

        self._namespace = namespace
        
        self._verbose = verbose
        self._debug = debug
        self.processes_basename = processes_basename

        self.cluster_size = cluster_size

        self._device = "cpu"

        self._controllers = [] # list of controllers

        self._processes = [] 
        self._child_alive = [] 

        self._is_cluster_ready = False
                 
        # shared memory 

        self.cluster_stats = None
        
        self._remote_term = None

        self._child_ps_were_alive = False
        self._child_ps_spawn_timeout = 180.0 # [s]
        self._terminated = False
    
    def __del__(self):
        self.terminate()
    
    def _handle_sigint(self, signum, frame):
        Journal.log(f"{self.__class__.__name__}",
                "_handle_sigint",
                "SIGINT received -> Cleaning up...",
                LogType.WARN)
        self.terminate()

    def _set_affinity(self, 
                core_idxs: List[int], 
                controller_idx: int):
        
        if not isinstance(core_idxs, List):
            exception = f"core_idx should be a List"
            Journal.log(f"{self.__class__.__name__}{controller_idx}",
                    "solve",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)

        if not isinstance(core_idxs[0], int):
            exception = f"core_idx should be a List of integeters"
            Journal.log(f"{self.__class__.__name__}{controller_idx}",
                    "solve",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)

        import os
        pid = os.getpid()  
        os.sched_setaffinity(pid, core_idxs)
        info = f"Affinity ID {os.sched_getaffinity(pid)} was set for controller n.{controller_idx}."
        Journal.log(f"{self.__class__.__name__}{controller_idx}",
                    "_set_affinity",
                    info,
                    LogType.STAT,
                    throw_when_excep = True)

    def _spawn_controller(self,
                    idx: int,
                    available_cores: List[int]):
        
        # this runs in a child process for each controller
        if self.set_affinity:
            # put rhc controller on a single specific core 
            self._set_affinity(core_idxs=[self._compute_process_affinity(idx, core_ids=available_cores)],
                        controller_idx=idx)
        # if self.use_mp_fork: # that's an hack
        #     # use all available cores
        #     self._set_affinity(core_idxs=available_cores,
        #                 controller_idx=idx)
            
        controller = self._generate_controller(idx=idx)
        controller.solve() # runs the solution loop

    def _check_child_ps_status(self):
        for i in range(0, self.cluster_size):
            child_p = self._processes[i]
            if not child_p.is_alive():
                self._child_alive[i] = False
            else:
                self._child_alive[i] = True
                
    def _childs_all_dead(self):
        self._check_child_ps_status()
        return not any(self._child_alive) 
    
    def _childs_all_alive(self):
        self._check_child_ps_status()
        return all(self._child_alive) 

    def _wait_for_child_ps(self):

        import time
        timeout=0.0
        update_dt=1
        
        while True:
            if self._childs_all_alive():
                Journal.log(self.__class__.__name__,
                        "_wait_for_child_ps",
                        f"all childs are alive",
                        LogType.STAT)
                self._child_ps_were_alive=True
                break
            else:
                self._child_ps_were_alive=False
            time.sleep(update_dt)
            timeout+=update_dt
            if timeout>self._child_ps_spawn_timeout:
                Journal.log(self.__class__.__name__,
                        "_wait_for_child_ps",
                        f"not all child ps alive withing {self._child_ps_spawn_timeout} s timeout!",
                        LogType.EXCEP,
                        throw_when_excep=False)
                break
        return self._child_ps_were_alive

    def run(self):
            
        self._spawn_processes()
        
        from control_cluster_bridge.utilities.shared_data.cluster_profiling import RhcProfiling
        from perf_sleep.pyperfsleep import PerfSleep
        
        from SharsorIPCpp.PySharsor.wrappers.shared_data_view import SharedTWrapper
        from SharsorIPCpp.PySharsorIPC import dtype

        self._remote_term = SharedTWrapper(namespace=self._namespace,
            basename="RemoteTermination",
            is_server=True,
            n_rows = 1, 
            n_cols = 1, 
            verbose = self._verbose, 
            vlevel = VLevel.V2,
            safe = False, # boolean operations are atomdic on 64 bit systems
            dtype=dtype.Bool,
            force_reconnection=True,
            with_gpu_mirror=False,
            with_torch_view=True,
            fill_value = False)
        self._remote_term.run()
        self._remote_term.write_retry(False, 
                                row_index=0,
                                col_index=0)
        
        self.cluster_stats = RhcProfiling(is_server=False, 
                                    name=self._namespace,
                                    verbose=self._verbose,
                                    vlevel=VLevel.V2,
                                    safe=True)
        
        self.cluster_stats.run()
        self.cluster_stats.write_info(dyn_info_name="cluster_ready",
                                    val=self._is_cluster_ready)

        while not self._terminated:
            nsecs =  1000000000 # 1 sec
            PerfSleep.thread_sleep(nsecs) # we just keep it alive
            if self._childs_all_dead():
                Journal.log(self.__class__.__name__,
                            "run",
                            "no child process is alive -> will terminate",
                            LogType.EXCEP,
                            throw_when_excep = False)
                break
            else:
                continue
        
        self.terminate() # closes all processe

    def terminate(self):
        
        if not self._terminated:
            Journal.log(self.__class__.__name__,
                            "terminate",
                            "terminating cluster...",
                            LogType.STAT,
                            throw_when_excep = True)
            self._close_processes() # we terminate all the child processes
            self._close_shared_mem() # and close the used shared memory
            self._terminated = True
        
    def _close_processes(self):
        # Wait for each process to exit gracefully or terminate forcefully
        self._remote_term.write_retry(True, 
                                        row_index=0,
                                        col_index=0) # send termination to controllers
        for process in self._processes:
            process.join()  # Wait for 5 seconds for each process to exit gracefully
            Journal.log(self.__class__.__name__,
                    "_close_processes",
                    "Terminated child process " + str(process.name),
                    LogType.STAT)
    
    def _close_shared_mem(self):
        if self.cluster_stats is not None:
            self.cluster_stats.close()
        if self._remote_term is not None:
            self._remote_term.close()

    def _get_cores(self):

        cores = None
        if not self.isolated_cores_only:
            # distribute processes over all system cores and
            # over both physical and virtual cores
            import psutil
            cores = list(range(psutil.cpu_count()))
        else:
            # distribute processes over isolated cores only,
            # both physical and virtual
            cores = self.isolated_cores
        return cores
 
    def _debug_prints(self):
            
        if self.core_ids_override_list is not None:
            # we distribute the controllers over the available ones
            warning = "Custom core id list provided. Will distribute controllers over those idxs."
            Journal.log(self.__class__.__name__,
                        "_debug_prints",
                        warning,
                        LogType.WARN,
                        throw_when_excep = True)
        else:
            if self.isolated_cores_only:
                if not len(self.isolated_cores) > 0: 
                    exception ="No isolated cores found on this machine. Either isolate some cores or " + \
                        "deactivate the use_isolated_cores flag."
                    Journal.log(self.__class__.__name__,
                        "_debug_prints",
                        exception,
                        LogType.EXCEP,
                        throw_when_excep = True)
                # we distribute the controllers over the available ones
                warning = "Will distribute controllers over isolated cores only"
                Journal.log(self.__class__.__name__,
                            "_debug_prints",
                            warning,
                            LogType.WARN,
                            throw_when_excep = True)
        if len(self.isolated_cores) < self.cluster_size and self.isolated_cores_only:
            # we distribute the controllers over the available ones
            warning = "Not enough isolated cores available to distribute the controllers " + \
                f"on them. N. available isolated cores: {len(self.isolated_cores)}, n. controllers {self.cluster_size}. "+ \
                "Processes will be distributed among the available ones."
            Journal.log(self.__class__.__name__,
                        "_debug_prints",
                        warning,
                        LogType.WARN,
                        throw_when_excep = True)
            
    def _compute_process_affinity(self, 
                        process_index: int, 
                        core_ids: List[int]):

        # assign process_index to a single core 
        # in the core ids list
        num_cores = len(core_ids)
        return core_ids[process_index % num_cores]

    def _spawn_processes(self):

        ctx = None
        ctx_name = ""
        if self.use_mp_fork:
            ctx = mp.get_context('forkserver')
            ctx_name="forkserver"
        else:
            ctx = mp.get_context('spawn')
            ctx_name="spawn"
        
        Journal.log(self.__class__.__name__,
                        "_spawn_processes",
                        f"spawning processes (using context {ctx_name})-->",
                        LogType.STAT,
                        throw_when_excep = True)
            
        self._debug_prints() # some debug prints
        
        core_ids = []
        if self.core_ids_override_list is None:
            core_ids = self._get_cores() # gets cores over which processes are to be distributed
        else:
            # ini case user wants to set core ids manually
            core_ids = self.core_ids_override_list

        for i in range(0, self.cluster_size):
            info = f"Spawning process for controller n.{i}."
            Journal.log(self.__class__.__name__,
                    "_spawn_processes",
                    info,
                    LogType.STAT,
                    throw_when_excep = True)
            process = ctx.Process(target=self._spawn_controller, 
                            name=self.processes_basename + str(i),
                            args=(i, core_ids))
            self._processes.append(process)
            self._child_alive.append(True)
            self._processes[i].start()
        
        self._wait_for_child_ps() # blocking: waits that all child ps are alive

        self._is_cluster_ready = True

        Journal.log(self.__class__.__name__,
                    "_spawn_processes",
                    "Processes spawned.",
                    LogType.STAT,
                    throw_when_excep = True)

    @abstractmethod
    def _generate_controller(self,
                        idx: int):
        # to be overridden
        return None