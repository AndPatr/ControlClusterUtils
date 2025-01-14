from EigenIPC.PyEigenIPCExt.wrappers.shared_data_view import SharedTWrapper
from EigenIPC.PyEigenIPC import StringTensorServer, StringTensorClient
from EigenIPC.PyEigenIPC import VLevel
from EigenIPC.PyEigenIPC import dtype as eigenipc_dtype, toNumpyDType
from EigenIPC.PyEigenIPC import Journal
from EigenIPC.PyEigenIPC import LogType

from control_cluster_bridge.utilities.shared_data.abstractions import SharedDataBase

from typing import Dict, Union, List
import numpy as np

# Control cluster profiling data

class ClusterCumulativeData(SharedTWrapper):
                 
    def __init__(self,
        namespace = "",
        is_server = False, 
        n_dims: int = -1, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "ClusterCumulativeData" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = n_dims, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = True,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)
        
class RtiSolTime(SharedTWrapper):
                 
    def __init__(self,
        cluster_size: int, 
        namespace = "",
        is_server = False, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        safe: bool = True,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "RtiSolTime" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = cluster_size, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = safe,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)

class SolveLoopDt(SharedTWrapper):
                 
    def __init__(self,
        cluster_size: int, 
        namespace = "",
        is_server = False, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        safe: bool = True,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "SolveLoopDt" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = cluster_size, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = safe,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)
     
class PrbUpdateDt(SharedTWrapper):
                 
    def __init__(self,
        cluster_size: int, 
        namespace = "",
        is_server = False, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        safe: bool = True,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "PrbUpdateDt" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = cluster_size, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = safe,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)

class PhasesShiftDt(SharedTWrapper):
                 
    def __init__(self,
        cluster_size: int, 
        namespace = "",
        is_server = False, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        safe: bool = True,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "PhasesShiftDt" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = cluster_size, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = safe,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)

class TaskRefUpdateDt(SharedTWrapper):
                 
    def __init__(self,
        cluster_size: int, 
        namespace = "",
        is_server = False, 
        verbose: bool = False, 
        vlevel: VLevel = VLevel.V0,
        safe: bool = True,
        force_reconnection: bool = False,
        optimize_mem: bool = False):

        basename = "TaskRefUpdateDt" 

        super().__init__(namespace = namespace,
            basename = basename,
            is_server = is_server, 
            n_rows = cluster_size, 
            n_cols = 1, 
            verbose = verbose, 
            vlevel = vlevel,
            dtype=eigenipc_dtype.Float,
            fill_value=np.nan,
            safe = safe,
            force_reconnection=force_reconnection,
            optimize_mem=optimize_mem)
        
class ClusterRuntimeInfoNames:

    def __init__(self):

        self._keys = ["cluster_rt_factor", 
                "cluster_sol_time",
                "cluster_ready"]
        
        self.idx_dict = dict.fromkeys(self._keys, None)

        # dynamic sim info is by convention
        # put at the start
        for i in range(len(self._keys)):
            
            self.idx_dict[self._keys[i]] = i

    def get(self):

        return self._keys

    def get_idx(self, name: str):

        return self.idx_dict[name]
    
class RhcProfiling(SharedDataBase):
                           
    def __init__(self, 
                cluster_size: int = 1,
                is_server = False, 
                param_dict: Dict = None,
                name = "",
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V2,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
        
        self.cluster_size = cluster_size
        
        self.vlevel = vlevel
        self.verbose = verbose

        self.safe = safe

        self.name = name

        self.namespace = self.name + "RhcProfiling"

        self._terminate = False
        
        self.is_server = is_server

        self.init = None                                                  

        self.param_keys = []

        self.runtime_info =  ClusterRuntimeInfoNames()

        self.static_param_dict = param_dict

        n_dims=None
        if self.is_server:
            # if client info is read on shared memory
            self.param_keys = self.runtime_info.get() + list(self.static_param_dict.keys())
            n_dims=len(self.param_keys)

        self.shared_data = ClusterCumulativeData(namespace = self.namespace,
                            is_server = is_server, 
                            n_dims = n_dims,
                            verbose = verbose, 
                            vlevel = vlevel,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)

        self.rti_sol_time = RtiSolTime(cluster_size= cluster_size, 
                            namespace = self.namespace,
                            is_server = is_server, 
                            verbose = verbose, 
                            vlevel = vlevel,
                            safe=False,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)
        
        self.solve_loop_dt = SolveLoopDt(cluster_size= cluster_size, 
                            namespace = self.namespace,
                            is_server = is_server, 
                            verbose = verbose, 
                            vlevel = vlevel,
                            safe=False,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)
        
        self.prb_update_dt = PrbUpdateDt(cluster_size= cluster_size, 
                            namespace = self.namespace,
                            is_server = is_server, 
                            verbose = verbose, 
                            vlevel = vlevel,
                            safe=False,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)

        self.phase_shift_dt = PhasesShiftDt(cluster_size= cluster_size, 
                            namespace = self.namespace,
                            is_server = is_server, 
                            verbose = verbose, 
                            vlevel = vlevel,
                            safe=False,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)

        self.task_ref_update_dt = TaskRefUpdateDt(cluster_size= cluster_size, 
                            namespace = self.namespace,
                            is_server = is_server, 
                            verbose = verbose, 
                            vlevel = vlevel,
                            safe=False,
                            force_reconnection=force_reconnection,
                            optimize_mem=optimize_mem)
        
        # names
        if self.is_server:

            self.shared_datanames = StringTensorServer(length = len(self.param_keys), 
                                        basename = "DataNames", 
                                        name_space = self.namespace,
                                        verbose = verbose, 
                                        vlevel = vlevel, 
                                        force_reconnection = force_reconnection)

        else:

            self.shared_datanames = StringTensorClient(
                                        basename = "DataNames", 
                                        name_space = self.namespace,
                                        verbose = verbose, 
                                        vlevel = vlevel)
        
        self._is_runnning = False
    
    def __del__(self):

        self.close()
    
    def is_running(self):

        return self._is_runnning
    
    def get_shared_mem(self):
        return [self.shared_data.get_shared_mem(),
            self.rti_sol_time.get_shared_mem(),
            self.solve_loop_dt.get_shared_mem(),
            self.prb_update_dt.get_shared_mem(),
            self.phase_shift_dt.get_shared_mem(),
            self.task_ref_update_dt.get_shared_mem(),
            self.shared_datanames.get_shared_mem()]
    
    def run(self):
        
        self.shared_datanames.run()
        
        self.shared_data.run()

        self.rti_sol_time.run()

        self.solve_loop_dt.run()

        self.prb_update_dt.run()

        self.phase_shift_dt.run()

        self.task_ref_update_dt.run()
            
        if self.is_server:
            names_written = self.shared_datanames.write_vec(self.param_keys, 0)
            if not names_written:
                exception = "Could not write shared sim names on shared memory!"
                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
                                        
        else:
            self.param_keys = [""] * self.shared_datanames.length()
            while not self.shared_datanames.read_vec(self.param_keys, 0):
                Journal.log(self.__class__.__name__,
                        "run",
                        "Could not read shared sim names on shared memory. Retrying...",
                        LogType.WARN,
                        throw_when_excep = True)
            
            self.shared_data.synch_all(read=True, retry=True)
            # wait flag since safe = False doesn't do anything
            self.rti_sol_time.synch_all(read=True, retry=True)

            self.solve_loop_dt.synch_all(read=True, retry=True)

            self.cluster_size = self.rti_sol_time.getNRows()
            
        self.param_values = np.full((len(self.param_keys), 1), 
                                fill_value=np.nan, 
                                dtype=toNumpyDType(eigenipc_dtype.Float))

        if self.is_server:
            
            for i in range(len(list(self.static_param_dict.keys()))):
                
                # writing static sim info

                dyn_info_size = len(self.runtime_info.get())

                # first m elements are custom info
                self.param_values[dyn_info_size + i, 0] = \
                    self.static_param_dict[self.param_keys[dyn_info_size + i]]
                                        
            self.shared_data.write_retry(row_index=0,
                                    col_index=0,
                                    data=self.param_values)

        self._is_runnning = True
                          
    def write_info(self,
            dyn_info_name: Union[str, List[str]],
            val: Union[float, List[float]]):

        # always writes to shared memory
        
        if isinstance(dyn_info_name, list):
            if not isinstance(val, list):
                exception = "The provided val should be a list of values!"
                Journal.log(self.__class__.__name__,
                    "write_info",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
            if len(val) != len(dyn_info_name):
                exception = "Name list and values length mismatch!"
                Journal.log(self.__class__.__name__,
                    "write_info",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)

            for i in range(len(val)):
                
                idx = self.runtime_info.get_idx(dyn_info_name[i])
                self.param_values[idx, 0] = val[i]
                self.shared_data.write_retry(data=self.param_values[idx, 0],
                                row_index=idx, col_index=0) 
            
        elif isinstance(dyn_info_name, str):
            
            idx = self.runtime_info.get_idx(dyn_info_name)
            self.param_values[idx, 0] = val
            self.shared_data.write_retry(data=self.param_values[idx, 0],
                                row_index=idx, col_index=0) 
    
    def get_static_info_idx(self, name: str):

        return self.idx_dict[name]
    
    def get_info(self,
            info_name: Union[str, List[str]]):
        
        if isinstance(info_name, list):
            return_list = []
            for i in range(len(info_name)):
                try:
                    return_list.append(self.param_values[idx, 0].item())
                except ValueError:
                    pass
            return return_list
        
        elif isinstance(info_name, str):    
            try:
                idx = self.param_keys.index(info_name)           
                return self.param_values[idx, 0].item()
            except ValueError:
                pass

        else:
            exception = "The provided info_name should be a list strings or a string!"
            Journal.log(self.__class__.__name__,
                "get_info",
                exception,
                LogType.EXCEP,
                throw_when_excep = True)
            
    def synch_info(self, row_index: int = 0):

        self.shared_data.synch_all(read=True, retry = True, row_index=row_index, col_index=0)
        self.param_values[:, :] = self.shared_data.get_numpy_mirror()

    def synch_all(self,
            row_index: int = 0,
            col_index: int = 0):

        self.rti_sol_time.synch_all(read=True, retry = True, row_index=row_index, col_index=col_index)
        self.solve_loop_dt.synch_all(read=True, retry = True, row_index=row_index, col_index=col_index)

    def get_all_info(self):

        self.synch_info()
        return self.param_values
    
    def close(self):

        self.shared_data.close()
        self.shared_datanames.close()

        self.rti_sol_time.close()
        self.solve_loop_dt.close()
        self.prb_update_dt.close()
        self.phase_shift_dt.close()
        self.task_ref_update_dt.close()

    def terminate(self):

        # just an alias for legacy compatibility
        self.close()
