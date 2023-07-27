from abc import ABC, abstractmethod

from control_cluster_utils.controllers.rhc import RHChild
from control_cluster_utils.utilities.control_cluster_utils import RobotClusterState, ActionChild
from control_cluster_utils.utilities.pipe_utils import NamedPipesHandler
OMode = NamedPipesHandler.OMode
DSize = NamedPipesHandler.DSize

import os
import struct

from typing import List

import multiprocess as mp

class ControlClusterSrvr(ABC):

    def __init__(self, 
                pipes_config_path: str,
                processes_basename: str = "controller"):

        # ciao :D
        #        CR 
        
        self.pipes_manager = NamedPipesHandler(pipes_config_path) # object to better handle 
        self.pipes_manager.create_buildpipes()

        self.status = "status"
        self.info = "info"
        self.warning = "warning"
        self.exception = "exception"

        self.processes_basename = processes_basename

        self.termination_flag = mp.Value('i', 0)

        self.cluster_size = -1

        self._device = "cpu"

        self._robot_states: RobotClusterState = None

        self._controllers: List[RHChild] = [] # list of controllers (must inherit from
        # RHController)

        self._handshake() 

        self._processes: List[mp.Process] = [] 

        self._is_cluster_ready = False

        self._controllers_count = 0

        self.solution_time = -1.0

    def _close_processes(self):
    
        # Wait for each process to exit gracefully or terminate forcefully
        
        self.termination_flag.value = 1
        
        for process in self._processes:

            process.join(timeout=0.2)  # Wait for 5 seconds for each process to exit gracefully

            if process.is_alive():
                
                process.terminate()  # Forcefully terminate the process
            
            print(f"[{self.__class__.__name__}]" + f"{self.info}" + ": terminating child process " + str(process.name))

    def _clean_pipes(self):

        self.pipes_manager.close_pipes(selector=["cluster_size", "jnt_number"])
        
        for i in range(0, self.cluster_size): 

            self._controllers[i].terminate() # send signal to close controller's internal pipes

    def _handshake(self):
        
        print(f"[{self.__class__.__name__}]" + f"{self.info}" + ": waiting for handshake with the ControlCluster client...")

        # retrieves some important configuration information from the server
        self.pipes_manager.open_pipes(["cluster_size"], 
                                    mode=OMode["O_RDONLY"])
        cluster_size_raw = os.read(self.pipes_manager.pipes_fd["cluster_size"], DSize["int"])
        # this will block until we get the info from the client
        self.cluster_size = struct.unpack('i', cluster_size_raw)[0]
        
        self.pipes_manager.create_runtime_pipes(self.cluster_size) # we create the remaining pipes

        print(f"[{self.__class__.__name__}]" + f"{self.info}" + ": friendship with ControlCluster client established.")

    def _check_state_size(self, 
                        cluster_state: RobotClusterState):

        if cluster_state.n_dofs != self.n_dofs:

            return False
        
        if cluster_state.cluster_size != self.cluster_size:

            return False
        
        return True

    @abstractmethod
    def _check_cmd_size(self, 
                    cluster_cmd: ActionChild):
        
        pass

    @abstractmethod
    def _synch_controllers_from_cluster(self):

        # pushes all necessary data from the cluster (which interfaces with the environment)
        # to each controller, so that their internal state is updated

        pass

    @abstractmethod
    def _synch_cluster_from_controllers(self):

        # synch the cluster with the data in each controller: 
        # this might include, for example, computed control commands

        pass

    def _spawn_processes(self):

        if self._controllers_count == self.cluster_size:
            
            for i in range(0, self.cluster_size):

                process = mp.Process(target=self._controllers[i].solve, 
                                    name = self.processes_basename + str(i))

                self._processes.append(process)

            # we start the processes
            for process in self._processes:

                process.start()

            self._is_cluster_ready = True
                
        else:

            raise Exception(f"[{self.__class__.__name__}]" + f"{self.exception}" + "You didn't finish to fill the cluster. Please call the add_controller() method to do so.")

    def _finalize_init(self):

        self.n_dofs = self._controllers[0]._get_ndofs() # we assume all controllers to be for the same robot

        self._robot_states = RobotClusterState(n_dofs = self.n_dofs, 
                                cluster_size = self.cluster_size,
                                device = self._device)
        
        jnt_number_data = struct.pack('i', self.n_dofs)
        
        self.pipes_manager.open_pipes(selector=["jnt_number"], 
                                mode=OMode["O_WRONLY"])

        os.write(self.pipes_manager.pipes_fd["jnt_number"], jnt_number_data) # we send this info
        # to the client, which is now guaranteed to be listening on the pipe

    def add_controller(self, controller: RHChild):

        if self._controllers_count < self.cluster_size:

            self._controllers.append(controller)
            
            self._controllers_count += 1

            if self._controllers_count == self.cluster_size:
            
                self._finalize_init()
        
            return True

        if self._controllers_count > self.cluster_size:

            print(f"[{self.__class__.__name__}]" + f"[{self.warning}]" + ": cannot add any more controllers to the cluster. The cluster is full.")

            return False
    
    def start(self):

        self._spawn_processes()

    def terminate(self):

        print(f"[{self.__class__.__name__}]" + f"[{self.info}]" + ": terminating cluster")

        self._close_processes() # we also terminate all the child processes

        self._clean_pipes() # we close all the used pipes

    @abstractmethod
    def get(self):

        pass
    
    @abstractmethod
    def set_commands(self,  
                    cluster_cmd: ActionChild):

        pass