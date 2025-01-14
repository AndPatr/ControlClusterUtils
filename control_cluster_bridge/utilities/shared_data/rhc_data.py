from EigenIPC.PyEigenIPC import dtype

from EigenIPC.PyEigenIPCExt.wrappers.shared_data_view import SharedTWrapper
from EigenIPC.PyEigenIPCExt.wrappers.shared_tensor_dict import SharedTensorDict
from EigenIPC.PyEigenIPC import VLevel
from EigenIPC.PyEigenIPC import LogType
from EigenIPC.PyEigenIPC import Journal
from EigenIPC.PyEigenIPC import StringTensorServer, StringTensorClient

from control_cluster_bridge.utilities.shared_data.abstractions import SharedDataBase
from control_cluster_bridge.utilities.shared_data.state_encoding import FullRobState

import numpy as np

from typing import List
        
class RobotState(FullRobState):

    def __init__(self,
            namespace: str,
            is_server: bool,
            n_robots: int = None,
            n_jnts: int = None,
            n_contacts: int = 1,
            jnt_names: List[str] = None,
            contact_names: List[str] = None,
            q_remapping: List[int] = None,
            with_gpu_mirror: bool = False,
            with_torch_view: bool = False,
            force_reconnection: bool = False,
            safe: bool = True,
            verbose: bool = False,
            vlevel: VLevel = VLevel.V1,
            fill_value = 0,
            optimize_mem: bool = False):

        basename = "RobotState"

        super().__init__(namespace=namespace,
            basename=basename,
            is_server=is_server,
            n_robots=n_robots,
            n_jnts=n_jnts,
            n_contacts=n_contacts,
            jnt_names=jnt_names,
            contact_names=contact_names,
            q_remapping=q_remapping,
            with_gpu_mirror=with_gpu_mirror,
            with_torch_view=with_torch_view,
            force_reconnection=force_reconnection,
            safe=safe,
            verbose=verbose,
            vlevel=vlevel,
            fill_value=fill_value,
            optimize_mem=optimize_mem)

class RhcCmds(FullRobState):

    def __init__(self,
            namespace: str,
            is_server: bool,
            n_robots: int = None,
            n_jnts: int = None,
            n_contacts: int = 1,
            jnt_names: List[str] = None,
            contact_names: List[str] = None,
            q_remapping: List[int] = None,
            with_gpu_mirror: bool = False,
            with_torch_view: bool = False,
            force_reconnection: bool = False,
            safe: bool = True,
            verbose: bool = False,
            vlevel: VLevel = VLevel.V1,
            fill_value=0,
            optimize_mem: bool = False):

        basename = "RhcCmds"

        super().__init__(namespace=namespace,
            basename=basename,
            is_server=is_server,
            n_robots=n_robots,
            n_jnts=n_jnts,
            n_contacts=n_contacts,
            jnt_names=jnt_names,
            contact_names=contact_names,
            q_remapping=q_remapping,
            with_gpu_mirror=with_gpu_mirror,
            with_torch_view=with_torch_view,
            force_reconnection=force_reconnection,
            safe=safe,
            verbose=verbose,
            vlevel=vlevel,
            fill_value=fill_value,
            optimize_mem=optimize_mem)

class RhcPred(FullRobState):

    def __init__(self,
            namespace: str,
            is_server: bool,
            n_robots: int = None,
            n_jnts: int = None,
            n_contacts: int = 1,
            jnt_names: List[str] = None,
            contact_names: List[str] = None,
            q_remapping: List[int] = None,
            with_gpu_mirror: bool = False,
            with_torch_view: bool = False,
            force_reconnection: bool = False,
            safe: bool = True,
            verbose: bool = False,
            vlevel: VLevel = VLevel.V1,
            fill_value=0,
            optimize_mem: bool = False):

        basename = "RhcPredictions"

        super().__init__(namespace=namespace,
            basename=basename,
            is_server=is_server,
            n_robots=n_robots,
            n_jnts=n_jnts,
            n_contacts=n_contacts,
            jnt_names=jnt_names,
            contact_names=contact_names,
            q_remapping=q_remapping,
            with_gpu_mirror=with_gpu_mirror,
            with_torch_view=with_torch_view,
            force_reconnection=force_reconnection,
            safe=safe,
            verbose=verbose,
            vlevel=vlevel,
            fill_value=fill_value,
            optimize_mem=optimize_mem)

class RhcPredDelta(FullRobState):

    def __init__(self,
            namespace: str,
            is_server: bool,
            n_robots: int = None,
            n_jnts: int = None,
            n_contacts: int = 1,
            jnt_names: List[str] = None,
            contact_names: List[str] = None,
            q_remapping: List[int] = None,
            with_gpu_mirror: bool = False,
            with_torch_view: bool = False,
            force_reconnection: bool = False,
            safe: bool = True,
            verbose: bool = False,
            vlevel: VLevel = VLevel.V1,
            fill_value=0,
            optimize_mem: bool = False):

        basename = "RhcPredictionDelta"

        super().__init__(namespace=namespace,
            basename=basename,
            is_server=is_server,
            n_robots=n_robots,
            n_jnts=n_jnts,
            n_contacts=n_contacts,
            jnt_names=jnt_names,
            contact_names=contact_names,
            q_remapping=q_remapping,
            with_gpu_mirror=with_gpu_mirror,
            with_torch_view=with_torch_view,
            force_reconnection=force_reconnection,
            safe=safe,
            verbose=verbose,
            vlevel=vlevel,
            fill_value=fill_value,
            optimize_mem=optimize_mem)
        
class RhcRefs(SharedDataBase):
    
    class RobotFullConfigRef(FullRobState):

        def __init__(self,
                namespace: str,
                is_server: bool,
                basename: str = "",
                n_robots: int = None,
                n_jnts: int = None,
                n_contacts: int = 1,
                jnt_names: List[str] = None,
                contact_names: List[str] = None,
                q_remapping: List[int] = None,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                force_reconnection: bool = False,
                safe: bool = True,
                verbose: bool = False,
                vlevel: VLevel = VLevel.V1,
                fill_value=np.nan, # if ref is not used
                optimize_mem: bool = False
                ):

            basename = basename + "RobotFullConfigRef"

            super().__init__(namespace=namespace,
                basename=basename,
                is_server=is_server,
                n_robots=n_robots,
                n_jnts=n_jnts,
                n_contacts=n_contacts,
                jnt_names=jnt_names,
                contact_names=contact_names,
                q_remapping=q_remapping,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                force_reconnection=force_reconnection,
                safe=safe,
                verbose=verbose,
                vlevel=vlevel,
                fill_value=fill_value,
                optimize_mem=optimize_mem)
    
    class Phase(SharedTWrapper):

        def __init__(self,
            namespace = "",
            basename = "",
            is_server = False, 
            n_robots: int = -1, 
            verbose: bool = False, 
            vlevel: VLevel = VLevel.V0,
            force_reconnection: bool = False,
            with_torch_view: bool = False,
            with_gpu_mirror: bool = False,
            safe: bool = True,
            optimize_mem: bool = False):
        
            basename = basename + "PhaseMode" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_robots, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = safe, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Int,
                force_reconnection=force_reconnection,
                with_torch_view=with_torch_view,
                with_gpu_mirror=with_gpu_mirror,
                fill_value = -1,
                optimize_mem=optimize_mem)
            
    class ContactFlag(SharedTWrapper):

        def __init__(self,
            namespace = "",
            basename = "",
            is_server = False, 
            n_robots: int = -1, 
            n_contacts: int = -1,
            verbose: bool = False, 
            vlevel: VLevel = VLevel.V0,
            force_reconnection: bool = False,
            with_torch_view: bool = False,
            with_gpu_mirror: bool = False,
            safe: bool = True,
            optimize_mem: bool = False):
        
            basename = basename + "ContactFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_robots, 
                n_cols = n_contacts, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = safe, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_torch_view=with_torch_view,
                with_gpu_mirror=with_gpu_mirror,
                fill_value = True,
                optimize_mem=optimize_mem)

    class FlightInfo(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_robots: int = None, 
                n_contacts: int = -1,
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                safe: bool = True,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                fill_value = 0,
                optimize_mem: bool = False):
            
            basename = "FlightInfo" 
            
            self._n_data = 2 # flight pos, flight length

            self.n_robots = n_robots
            self.n_contacts=n_contacts

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_robots, 
                n_cols = self._n_data*n_contacts, 
                dtype = dtype.Float,
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                optimize_mem=optimize_mem)

            # root
            self._pos = None
            self._len = None
            self._all = None

            self._pos_gpu = None
            self._len_gpu = None
            self._all_gpu = None
            
        def run(self):
            # overriding parent 
            super().run()
            if not self.is_server:
                self.n_robots = self.n_rows
                self.n_contacts = int(self.n_cols/self._n_data)
            self._init_views()

        def _init_views(self):

            # root
            if self._with_torch_view:
                self._pos = self.get_torch_mirror()[:, 0:self.n_contacts].view(self.n_robots, self.n_contacts)
                self._len = self.get_torch_mirror()[:, self.n_contacts:2*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._all = self.get_torch_mirror()[:, 0:self._n_data*self.n_contacts].view(self.n_robots, self._n_data*self.n_contacts)
            else:
                self._pos = self.get_numpy_mirror()[:, 0:self.n_contacts].view()
                self._len = self.get_numpy_mirror()[:, self.n_contacts:2*self.n_contacts].view()
                self._all = self.get_numpy_mirror()[:, 0:self._n_data*self.n_contacts].view()

            if self.gpu_mirror_exists():

                # gpu views
                self._pos_gpu = self._gpu_mirror[:, 0:self.n_contacts].view(self.n_robots, self.n_contacts)
                self._len_gpu = self._gpu_mirror[:, self.n_contacts:2*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._all_gpu = self._gpu_mirror[:, 0:self._n_data*self.n_contacts].view(self.n_robots, self._n_data*self.n_contacts)
        
        def _retrieve_data(self,
            name: str,
            gpu: bool = False):
            
            if not gpu:
                if name == "pos":
                    return self._pos
                elif name == "len":
                    return self._len
                elif name == "all":
                    return self._all
                else:
                    return None
            else:
                if name == "pos":
                    return self._pos_gpu
                elif name == "len":
                    return self._len_gpu
                elif name == "all":
                    return self._all_gpu
                else:
                    return None
        
        def set(self,
                data,
                data_type: str,
                robot_idxs= None,
                contact_idx = None,
                gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                gpu=gpu)
            
            if robot_idxs is None:
                if contact_idx is None:
                    internal_data[:, :] = data
                else:
                    internal_data[:, contact_idx] = data
            else:
                if contact_idx is None:
                    internal_data[robot_idxs, :] = data
                else:
                    internal_data[robot_idxs, contact_idx] = data
                    
        def get(self,
            data_type: str,
            robot_idxs = None,
            contact_idx = None,
            gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                        gpu=gpu)
                
            if robot_idxs is None:
                if contact_idx is None:
                    return internal_data
                else:
                    return internal_data[:, contact_idx]
            else:
                if contact_idx is None:
                    return internal_data[robot_idxs, :]
                else:
                    return internal_data[robot_idxs, contact_idx]

    class FlightSettings(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_robots: int = None, 
                n_contacts: int = -1,
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                safe: bool = True,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                fill_value = 0,
                optimize_mem: bool = False):
            
            basename = "FlightSettings" 
            
            self._n_data = 3 # flight length, apex dpos, end dpos (w.r.t initial pos)

            self.n_robots = n_robots
            self.n_contacts=n_contacts

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_robots, 
                n_cols = self._n_data*n_contacts, 
                dtype = dtype.Float,
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                optimize_mem=optimize_mem)

            # root
            self._len = None
            self._apex_dpos = None
            self._end_dpos = None
            self._all = None

            self._len_gpu = None
            self._apex_dpos_gpu = None
            self._end_dpos_gpu = None
            self._all_gpu = None
            
        def run(self):
            # overriding parent 
            super().run()
            if not self.is_server:
                self.n_robots = self.n_rows
                self.n_contacts = int(self.n_cols/self._n_data)
            self._init_views()

        def _init_views(self):

            # root
            if self._with_torch_view:
                self._len = self.get_torch_mirror()[:, 0:self.n_contacts].view(self.n_robots, self.n_contacts)
                self._apex_dpos = self.get_torch_mirror()[:, self.n_contacts:2*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._end_dpos = self.get_torch_mirror()[:, 2*self.n_contacts:3*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._all = self.get_torch_mirror()[:, 0:self._n_data*self.n_contacts].view(self.n_robots, self._n_data*self.n_contacts)
            else:
                self._len = self.get_numpy_mirror()[:, 0:self.n_contacts].view()
                self._apex_dpos = self.get_numpy_mirror()[:, self.n_contacts:2*self.n_contacts].view()
                self._end_dpos = self.get_numpy_mirror()[:, 2*self.n_contacts:3*self.n_contacts].view()
                self._all = self.get_numpy_mirror()[:, 0:self._n_data*self.n_contacts].view()

            if self.gpu_mirror_exists():
                # gpu views
                self._len_gpu = self._gpu_mirror[:, 0:self.n_contacts].view(self.n_robots, self.n_contacts)
                self._apex_dpos_gpu = self._gpu_mirror[:, self.n_contacts:2*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._end_dpos_gpu = self._gpu_mirror[:, 2*self.n_contacts:3*self.n_contacts].view(self.n_robots, self.n_contacts)
                self._all_gpu = self._gpu_mirror[:, 0:self._n_data*self.n_contacts].view(self.n_robots, self._n_data*self.n_contacts)
        
        def _retrieve_data(self,
            name: str,
            gpu: bool = False):
            
            if not gpu:
                if name == "len":
                    return self._len
                if name == "apex_dpos":
                    return self._apex_dpos
                if name == "end_dpos":
                    return self._end_dpos
                elif name == "all":
                    return self._all
                else:
                    return None
            else:
                if name == "len":
                    return self._len_gpu
                if name == "apex_dpos":
                    return self._apex_dpos_gpu
                if name == "end_dpos":
                    return self._end_dpos_gpu
                elif name == "all":
                    return self._all_gpu
                else:
                    return None
        
        def set(self,
                data,
                data_type: str,
                robot_idxs= None,
                contact_idx = None,
                gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                gpu=gpu)
            
            if robot_idxs is None:
                if contact_idx is None:
                    internal_data[:, :] = data
                else:
                    internal_data[:, contact_idx] = data
            else:
                if contact_idx is None:
                    internal_data[robot_idxs, :] = data
                else:
                    internal_data[robot_idxs, contact_idx] = data
                    
        def get(self,
            data_type: str,
            robot_idxs = None,
            contact_idx = None,
            gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                        gpu=gpu)
                
            if robot_idxs is None:
                if contact_idx is None:
                    return internal_data
                else:
                    return internal_data[:, contact_idx]
            else:
                if contact_idx is None:
                    return internal_data[robot_idxs, :]
                else:
                    return internal_data[robot_idxs, contact_idx]
                
    class AlphaView(SharedTWrapper):
        
        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "Alpha" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomdic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0.0,
                optimize_mem=optimize_mem)
    
    class BoundRelaxView(SharedTWrapper):
        
        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "BoundRelax" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomdic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0.0,
                optimize_mem=optimize_mem)
            
    def __init__(self,
                namespace: str,
                is_server: bool,
                n_robots: int = None,
                n_jnts: int = None,
                n_contacts: int = 1,
                jnt_names: List[str] = None,
                contact_names: List[str] = None,
                q_remapping: List[int] = None,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                force_reconnection: bool = False,
                safe: bool = False,
                verbose: bool = False,
                vlevel: VLevel = VLevel.V1,
                fill_value=np.nan,
                optimize_mem: bool = False):
        
        self._optimize_mem=optimize_mem

        self.basename = "RhcRefs"

        self.is_server = is_server

        self._with_gpu_mirror = with_gpu_mirror
        self._with_torch_view = with_torch_view

        self.n_robots = n_robots

        self.namespace = namespace

        self.verbose = verbose

        self.vlevel = vlevel

        self.force_reconnection = force_reconnection

        self.safe = safe

        self.rob_refs = self.RobotFullConfigRef(namespace=namespace,
                                    basename=self.basename,
                                    is_server=is_server,
                                    n_robots=n_robots,
                                    n_jnts=n_jnts,
                                    n_contacts=n_contacts,
                                    jnt_names=jnt_names,
                                    contact_names=contact_names,
                                    q_remapping=q_remapping,
                                    with_gpu_mirror=with_gpu_mirror,
                                    with_torch_view=with_torch_view,
                                    force_reconnection=force_reconnection,
                                    safe=safe,
                                    verbose=verbose,
                                    vlevel=vlevel,
                                    fill_value=fill_value,
                                    optimize_mem=optimize_mem)
        
        self.contact_flags = None

        self._is_runnning = False

    def __del__(self):

        self.close()

    def is_running(self):
    
        return self._is_runnning
    
    def get_shared_mem(self):
        return self.rob_refs.get_shared_mem() + [
            self.phase_id.get_shared_mem(),
            self.contact_flags.get_shared_mem(),
            self.flight_info.get_shared_mem(),
            self.flight_settings.get_shared_mem(),
            self.alpha.get_shared_mem(),
            self.bound_rel.get_shared_mem()]
    
    def run(self):

        self.rob_refs.run()

        self._n_contacts = self.rob_refs.n_contacts()
        
        self.contact_flags = self.ContactFlag(namespace=self.namespace,
                            basename=self.basename,
                            is_server=self.is_server,
                            n_robots=self.rob_refs.root_state.n_rows,
                            n_contacts=self._n_contacts,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            safe=self.safe,
                            optimize_mem=self._optimize_mem)
        self.contact_flags.run()

        self.flight_info = self.FlightInfo(namespace=self.namespace,
                            is_server=self.is_server,
                            n_robots=self.rob_refs.root_state.n_rows,
                            n_contacts=self._n_contacts,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            safe=self.safe,
                            optimize_mem=self._optimize_mem)
        self.flight_info.run()

        self.flight_settings = self.FlightSettings(namespace=self.namespace,
                            is_server=self.is_server,
                            n_robots=self.rob_refs.root_state.n_rows,
                            n_contacts=self._n_contacts,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            safe=self.safe,
                            optimize_mem=self._optimize_mem)
        self.flight_settings.run()
        
        self.phase_id = self.Phase(namespace=self.namespace,
                            basename=self.basename,
                            is_server=self.is_server,
                            n_robots=self.rob_refs.root_state.n_rows,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            safe=self.safe,
                            optimize_mem=self._optimize_mem)
        self.phase_id.run()
        self.alpha = self.AlphaView(namespace=self.namespace,
                            is_server=self.is_server,
                            cluster_size=self.rob_refs.root_state.n_rows,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            optimize_mem=self._optimize_mem)
        self.alpha.run()
        self.bound_rel = self.BoundRelaxView(namespace=self.namespace,
                            is_server=self.is_server,
                            cluster_size=self.rob_refs.root_state.n_rows,
                            verbose=self.verbose,
                            vlevel=self.vlevel,
                            force_reconnection=self.force_reconnection,
                            with_gpu_mirror=self._with_gpu_mirror,
                            with_torch_view=self._with_torch_view,
                            optimize_mem=self._optimize_mem)
        self.bound_rel.run()

        self._is_runnning = True
    
    def n_contacts(self):
        return self._n_contacts
    
    def close(self):
        
        if self.is_running():
            
            self.rob_refs.close()
            self.phase_id.close()
            self.flight_info.close()
            self.flight_settings.close()

            self.contact_flags.close()
            self.alpha.close()
            self.bound_rel.close()

            self._is_runnning = False

class RhcStatus(SharedDataBase):
    
    class FailFlagView(SharedTWrapper):
        
        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterFailFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomdic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = False,
                optimize_mem=optimize_mem)
    
    class ResetFlagView(SharedTWrapper):
        
        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterResetFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = False,
                optimize_mem=optimize_mem)
    
    class TriggerFlagView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterTriggerFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = False,
                optimize_mem=optimize_mem)
    
    class ActivationFlagView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterActivationFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = False,
                optimize_mem=optimize_mem)
    
    class RegistrationFlagView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterRegistrationFlag" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Bool,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = False,
                optimize_mem=optimize_mem)
            
    class ControllersCounterView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterControllersCounter" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = 1, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Int,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
    
    class FailsCounterView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "ClusterControllerFailsCounter" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Int,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
            
    class RhcCostView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcCost" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = np.nan,
                optimize_mem=optimize_mem)
    
    class RhcCnstrViolationView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcCnstrViolation" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = np.nan,
                optimize_mem=optimize_mem)
    
    class RhcNodesCostView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                n_nodes: int = -1,
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcNodesCost" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
    
    class RhcNodesCnstrViolationView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                n_nodes: int = -1,
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcNodesCnstrViolation" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
    
    class RhcNIterationsView(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcNIterations" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = np.nan,
                optimize_mem=optimize_mem)
    
    class RhcFcNormalized(SharedTWrapper): 

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                n_contacts: int = -1,
                n_nodes: int = -1,
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcContactForces" # hardcoded

            n_cols=None
            if is_server:
                n_cols=n_contacts*3*n_nodes
            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = n_cols, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
        
        def tot_dim(self):
            return self.n_cols
    
    class RhcFailIndex(SharedTWrapper): 

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcFailIndex" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = 1, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = False, # boolean operations are atomic on 64 bit systems
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
    
    class RhcStaticInfo(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                cluster_size: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                force_reconnection: bool = False,
                with_gpu_mirror: bool = False,
                with_torch_view: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcStaticInfo" # hardcoded
            self.n_data = 6 # rhc dts, rhc horizon length, rhc n nodes, ncontacts,
            # robot mass, pred node idx
            
            self._n_rhcs = cluster_size

            self._dts = None
            self._horizons = None
            self._nnodes = None
            self._ncontacts = None
            self._robot_mass = None
            self._pred_node_idx = None

            self._dts_gpu = None
            self._horizons_gpu = None
            self._nnodes_gpu = None
            self._ncontacts_gpu = None
            self._robot_mass_gpu = None
            self._pred_node_idx_gpu = None

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = cluster_size, 
                n_cols = self.n_data, 
                verbose = verbose, 
                vlevel = vlevel,
                safe = True,
                dtype=dtype.Float,
                force_reconnection=force_reconnection,
                with_gpu_mirror=with_gpu_mirror,
                with_torch_view=with_torch_view,
                fill_value = 0,
                optimize_mem=optimize_mem)
        
        def run(self):
            # overriding parent 
            super().run()
            if not self.is_server:
                self._n_rhcs=self.n_rows
            self._init_views()

        def _init_views(self):
                
            if self._with_torch_view:
                self._dts = self.get_torch_mirror()[:, 0:1].view(self._n_rhcs, 1)
                self._horizons = self.get_torch_mirror()[:, 1:2].view(self._n_rhcs, 1)
                self._nnodes = self.get_torch_mirror()[:, 2:3].view(self._n_rhcs, 1)
                self._ncontacts = self.get_torch_mirror()[:, 3:4].view(self._n_rhcs, 1)
                self._robot_mass = self.get_torch_mirror()[:, 4:5].view(self._n_rhcs, 1)
                self._pred_node_idx = self.get_torch_mirror()[:, 5:6].view(self._n_rhcs, 1)

            else:
                self._dts = self.get_numpy_mirror()[:, 0:1].view()
                self._horizons = self.get_numpy_mirror()[:, 1:2].view()
                self._nnodes = self.get_numpy_mirror()[:, 2:3].view()
                self._ncontacts = self.get_numpy_mirror()[:, 3:4].view()
                self._robot_mass = self.get_numpy_mirror()[:, 4:5].view()
                self._pred_node_idx = self.get_numpy_mirror()[:, 5:6].view()
            
            if self.gpu_mirror_exists():
                # gpu views 
                self._dts_gpu = self._gpu_mirror[:, 0:1].view(self._n_rhcs, 1)
                self._horizons_gpu = self._gpu_mirror[:, 1:2].view(self._n_rhcs, 1)
                self._nnodes_gpu = self._gpu_mirror[:, 2:3].view(self._n_rhcs, 1)
                self._ncontacts_gpu = self._gpu_mirror[:, 3:4].view(self._n_rhcs, 1)
                self._robot_mass_gpu = self._gpu_mirror[:, 4:5].view(self._n_rhcs, 1)
                self._pred_node_idx_gpu= self._gpu_mirror[:, 5:6].view(self._n_rhcs, 1)

        def _retrieve_data(self,
                name: str,
                gpu: bool = False):
        
            if not gpu:
                if name == "dts":
                    return self._dts
                elif name == "horizons":
                    return self._horizons
                elif name == "nnodes":
                    return self._nnodes
                elif name == "ncontacts":
                    return self._ncontacts
                elif name == "robot_mass":
                    return self._robot_mass
                elif name == "pred_node_idx":
                    return self._pred_node_idx
                else:
                    return None
            else:
                if name == "dts":
                    return self._dts_gpu
                elif name == "horizons":
                    return self._horizons_gpu
                elif name == "nnodes":
                    return self._nnodes_gpu
                elif name == "ncontacts":
                    return self._ncontacts_gpu
                elif name == "robot_mass":
                    return self._robot_mass_gpu
                elif name == "pred_node_idx":
                    return self._pred_node_idx_gpu
                else:
                    return None
        
        def set(self,
            data,
            data_type: str,
            rhc_idxs= None,
            gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                        gpu=gpu)
            if rhc_idxs is None:
                internal_data[:, :] = data
            else:
                internal_data[rhc_idxs, :] = data

        def get(self,
            data_type: str,
            rhc_idxs = None,
            gpu: bool = False):

            internal_data = self._retrieve_data(name=data_type,
                        gpu=gpu)
            if rhc_idxs is None:
                return internal_data
            else:
                return internal_data[rhc_idxs, :]
            
    def __init__(self, 
            is_server = False, 
            cluster_size: int = -1, 
            n_nodes: int = -1,
            n_contacts: int = -1,
            namespace = "", 
            verbose = False, 
            vlevel: VLevel = VLevel.V0,
            force_reconnection: bool = False,
            with_gpu_mirror: bool = False,
            with_torch_view: bool = False,
            optimize_mem: bool = False):

        self._optimize_mem=optimize_mem
        
        self.is_server = is_server

        self.cluster_size = cluster_size
        self.n_nodes = n_nodes
        self.n_contacts = n_contacts

        self.namespace = namespace

        self.verbose = verbose

        self.vlevel = vlevel
        self.force_reconnection=force_reconnection

        self.with_gpu_mirror = with_gpu_mirror
        self.with_torch_view = with_torch_view

        self.fails =None
        self.resets=None
        self.trigger=None
        self.activation_state=None
        self.registration=None
        self.controllers_counter=None
        self.controllers_fail_counter=None
        self.rhc_cost=None
        self.rhc_constr_viol=None
        self.rhc_nodes_cost=None
        self.rhc_nodes_constr_viol=None
        self.rhc_n_iter=None
        self.rhc_fcn=None
        self.rhc_fail_idx=None

        self._is_runnning = False

        self._acquired_reg_sem = False

        self._init_shared_memory()
        
    def __del__(self):

        self.close()

    def is_running(self):
    
        return self._is_runnning
    
    def get_shared_mem(self):
        return [self.fails.get_shared_mem(),
            self.resets.get_shared_mem(),
            self.trigger.get_shared_mem(),
            self.activation_state.get_shared_mem(),
            self.registration.get_shared_mem(),
            self.controllers_counter.get_shared_mem(),
            self.controllers_fail_counter.get_shared_mem(),
            self.rhc_cost.get_shared_mem(),
            self.rhc_constr_viol.get_shared_mem(),
            self.rhc_n_iter.get_shared_mem(),
            self.rhc_nodes_cost.get_shared_mem(),
            self.rhc_nodes_constr_viol.get_shared_mem(),
            self.rhc_fcn.get_shared_mem(),
            self.rhc_fail_idx.get_shared_mem(),
            self.rhc_static_info.get_shared_mem()]
    
    def _init_shared_memory(self):

        if self.is_server:
            if self.n_contacts<=0:
                Journal.log(self.__class__.__name__,
                    "run",
                    "n_contacts<=0!",
                    LogType.EXCEP,
                    throw_when_excep = True)
            if self.n_nodes<=0:
                Journal.log(self.__class__.__name__,
                    "run",
                    "n_nodes<=0!",
                    LogType.EXCEP,
                    throw_when_excep = True)
        self.rhc_static_info = self.RhcStaticInfo(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.fails = self.FailFlagView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.resets = self.ResetFlagView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.trigger = self.TriggerFlagView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.activation_state = self.ActivationFlagView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.registration = self.RegistrationFlagView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.controllers_counter = self.ControllersCounterView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.controllers_fail_counter = self.FailsCounterView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size,
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.rhc_cost = self.RhcCostView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.rhc_constr_viol = self.RhcCnstrViolationView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.rhc_nodes_cost = self.RhcNodesCostView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                n_nodes=self.n_nodes,
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.rhc_nodes_constr_viol = self.RhcNodesCnstrViolationView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                n_nodes=self.n_nodes,
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

        self.rhc_n_iter = self.RhcNIterationsView(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)
        
        self.rhc_fcn = self.RhcFcNormalized(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                n_contacts=self.n_contacts,
                                n_nodes=self.n_nodes,
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem) 
        
        self.rhc_fail_idx = self.RhcFailIndex(namespace=self.namespace, 
                                is_server=self.is_server, 
                                cluster_size=self.cluster_size, 
                                verbose=self.verbose, 
                                vlevel=self.vlevel,
                                force_reconnection=self.force_reconnection,
                                with_gpu_mirror=self.with_gpu_mirror,
                                with_torch_view=self.with_torch_view,
                                optimize_mem=self._optimize_mem)

    def run(self):
                
        self.rhc_static_info.run()
        self.resets.run()
        self.trigger.run()
        self.fails.run()
        self.activation_state.run()
        self.registration.run()
        self.controllers_counter.run()
        self.controllers_fail_counter.run()
        self.rhc_cost.run()
        self.rhc_constr_viol.run()
        self.rhc_nodes_cost.run()
        self.rhc_nodes_constr_viol.run()
        self.rhc_n_iter.run()
        self.rhc_fcn.run()
        self.rhc_fail_idx.run()

        if not self.is_server:
            self.cluster_size = self.trigger.getNRows()
            self.n_nodes = self.rhc_nodes_cost.n_cols
            self.n_contacts = int(self.rhc_fcn.n_cols / (3*self.n_nodes))

        self._is_runnning = True
    
    def close(self):
        
        if self.is_running():
            
            self.resets.close()
            self.trigger.close()
            self.fails.close()    
            self.activation_state.close()
            self.registration.close()
            self.controllers_counter.close()
            self.controllers_fail_counter.close()
            self.rhc_n_iter.close()
            self.rhc_cost.close()
            self.rhc_constr_viol.close()
            self.rhc_nodes_cost.close()
            self.rhc_nodes_constr_viol.close()
            self.rhc_fcn.close()
            self.rhc_fail_idx.close()
            self.rhc_static_info.close()
            
            self._is_runnning = False

class RhcInternal(SharedDataBase):

    # class for sharing internal data of a 
    # receding-horizon controller

    class Q(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "Q" # configuration vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
    
    class V(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "V" # velocity vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
    
    class A(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "A" # acceleration vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
    
    class ADot(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "ADot" # jerk vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
    
    class F(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "F" # cartesian force vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
            
    class FDot(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "FDot" # yank vector

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)
            
    class Eff(SharedTWrapper):

        def __init__(self,
                namespace = "",
                is_server = False, 
                n_dims: int = -1, 
                n_nodes: int = -1, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                fill_value: float = np.nan,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "Eff" # hardcoded

            super().__init__(namespace = namespace,
                basename = basename,
                is_server = is_server, 
                n_rows = n_dims, 
                n_cols = n_nodes, 
                verbose = verbose, 
                vlevel = vlevel,
                fill_value = fill_value, 
                safe = safe,
                force_reconnection=force_reconnection,
                optimize_mem=optimize_mem)

    class RHCosts(SharedTensorDict):

        def __init__(self,
                names: List[str] = None, # not needed if client
                dimensions: List[int] = None, # not needed if client
                n_nodes: int = -1, # not needed if client 
                namespace = "",
                is_server = False, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcCosts"

            super().__init__(names = names, # not needed if client
                    dimensions = dimensions, # not needed if client
                    n_nodes = n_nodes, # not needed if client 
                    namespace = namespace + basename,
                    is_server = is_server, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    safe = safe,
                    force_reconnection = force_reconnection) 
    
    class RHConstr(SharedTensorDict):

        def __init__(self,
                names: List[str] = None, # not needed if client
                dimensions: List[int] = None, # not needed if client
                n_nodes: int = -1, # not needed if client 
                namespace = "",
                is_server = False, 
                verbose: bool = False, 
                vlevel: VLevel = VLevel.V0,
                safe: bool = True,
                force_reconnection: bool = False,
                optimize_mem: bool = False):
            
            basename = "RhcConstraints"

            super().__init__(names = names, # not needed if client
                    dimensions = dimensions, # not needed if client
                    n_nodes = n_nodes, # not needed if client 
                    namespace = namespace + basename,
                    is_server = is_server, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    safe = safe,
                    force_reconnection = force_reconnection) 
    
    class Config():

        def __init__(self,
            is_server: bool = False,
            enable_q: bool = False, 
            enable_v: bool = False, 
            enable_a: bool = False,
            enable_a_dot: bool = False, 
            enable_f: bool = False, 
            enable_f_dot: bool = False, 
            enable_eff: bool = False, 
            cost_names: List[str] = None, 
            constr_names: List[str] = None,
            cost_dims: List[int] = None, 
            constr_dims: List[int] = None,
            enable_costs: bool = False,
            enable_constr: bool = False):

            self.is_server = is_server

            self.enable_q = enable_q
            self.enable_v = enable_v
            self.enable_a = enable_a
            self.enable_a_dot = enable_a_dot
            self.enable_f = enable_f
            self.enable_f_dot = enable_f_dot
            self.enable_eff = enable_eff

            self.enable_costs = enable_costs
            self.enable_constr = enable_constr

            self.cost_names = None
            self.cost_dims = None

            self.constr_names = None
            self.constr_dims = None

            self.n_costs = 0
            self.n_constr = 0

            self._set_cost_data(cost_names, cost_dims)
            self._set_constr_data(constr_names, constr_dims)


        def _set_cost_data(self, 
                        names: List[str] = None,
                        dims: List[str] = None):

            self.cost_names = names
            self.cost_dims = dims

            if (names is not None) and (self.cost_names is None) and \
                self.is_server:
                
                exception = f"Cost enabled but no cost_names list was provided"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
                
            if (dims is not None) and (self.cost_dims is None) and \
                self.is_server:
                
                exception = f"Cost enabled but no cost_dims list was provided"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
                
            if self.is_server and (not (len(self.cost_names) == len(self.cost_dims))):
                
                exception = f"Cost names dimension {len(self.cost_names)} " + \
                    f"does not match dim. vector length {len(self.cost_dims)}"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
            
            if self.is_server:

                self.enable_costs = True
                self.n_costs = len(self.cost_names)

        def _set_constr_data(self, 
                        names: List[str] = None,
                        dims: List[str] = None):

            self.constr_names = names
            self.constr_dims = dims

            if (names is not None) and (self.constr_names is None) and \
                self.is_server:
                
                exception = "Constraints enabled but no cost_names list was provided"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)

            if (dims is not None) and (self.constr_dims is None) and \
                self.is_server:
                
                exception = "Cost enabled but no constr_dims list was provided"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)

            if self.is_server and (not (len(self.constr_names) == len(self.constr_dims))):
                
                exception = f"Cost names dimension {len(self.constr_names)} " + \
                    f"does not match dim. vector length {len(self.constr_dims)}"

                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
            
            if self.is_server:

                self.enable_constr = True
                self.n_constr = len(self.constr_names)

    def __init__(self,
            config: Config = None,
            namespace = "",
            rhc_index = 0,
            n_nodes: int = -1, 
            n_contacts: int = -1,
            n_jnts: int = -1,
            jnt_names: List[str] = None,
            verbose: bool = False, 
            vlevel: VLevel = VLevel.V0,
            force_reconnection: bool = False,
            safe: bool = True,
            optimize_mem: bool = False):

        self.rhc_index = rhc_index
        self._basename = "RhcInternal"

        self._verbose = verbose
        self._vlevel = vlevel

        self._jnt_names = jnt_names
        self._n_jnts = n_jnts

        # appending controller index to namespace
        self.namespace = self._basename + namespace + "_n_" + str(self.rhc_index)
        
        if config is not None:
            self.config = config
        else:
            # use defaults
            self.config = self.Config()

        self.q = None
        self.v = None
        self.a = None
        self.a_dot = None
        self.f = None
        self.f_dot = None
        self.eff = None
        self.costs = None
        self.cnstr = None
        
        self._shared_jnt_names = None

        self._is_server = config.is_server

        if self.config.enable_q:
            self.q = self.Q(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 3 + 4 + n_jnts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_v:
            self.v = self.V(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 3 + 3 + n_jnts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_a:
            self.a = self.A(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 3 + 3 + n_jnts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_a_dot:
            self.a_dot = self.ADot(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 3 + 3 + n_jnts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_f:
            self.f = self.F(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 6 * n_contacts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
            
        if self.config.enable_f_dot:
            self.f_dot = self.FDot(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 6 * n_contacts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_eff:
            self.eff = self.Eff(namespace = self.namespace,
                    is_server = self._is_server, 
                    n_dims = 3 + 3 + n_jnts, 
                    n_nodes = n_nodes, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
            
        if self.config.enable_costs:
            self.costs = self.RHCosts(names = self.config.cost_names, # not needed if client
                    dimensions = self.config.cost_dims, # not needed if client
                    n_nodes = n_nodes, # not needed if client 
                    namespace = self.namespace,
                    is_server = self._is_server, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self.config.enable_constr:
            self.cnstr = self.RHConstr(names = self.config.constr_names, # not needed if client
                    dimensions = self.config.constr_dims, # not needed if client
                    n_nodes = n_nodes, # not needed if client 
                    namespace = self.namespace,
                    is_server = self._is_server, 
                    verbose = verbose, 
                    vlevel = vlevel,
                    force_reconnection=force_reconnection,
                    safe=safe,
                    optimize_mem=optimize_mem)
        
        if self._is_server:
            self._shared_jnt_names = StringTensorServer(length = len(self._jnt_names), 
                                        basename = self._basename + "Names", 
                                        name_space = self.namespace,
                                        verbose = self._verbose, 
                                        vlevel = self._vlevel,
                                        safe = safe,
                                        force_reconnection = force_reconnection)
        else:
            self._shared_jnt_names = StringTensorClient(
                                        basename = self._basename + "Names", 
                                        name_space = self.namespace,
                                        verbose = self._verbose, 
                                        vlevel = self._vlevel,
                                        safe = safe)
            
        self._is_running = False
    
    def is_running(self):

        return self._is_running
    
    def get_shared_mem(self):
        return [self.fails.get_shared_mem(),
            self.q.get_shared_mem(),
            self.v.get_shared_mem(),
            self.a.get_shared_mem(),
            self.a_dot.get_shared_mem(),
            self.f.get_shared_mem(),
            self.f_dot.get_shared_mem(),
            self.eff.get_shared_mem(),
            self.costs.get_shared_mem(),
            self.cnstr.get_shared_mem(),
            self._shared_jnt_names.get_shared_mem()]
                
    def jnt_names(self):

        return self._jnt_names
        
    def run(self):

        if self.q is not None:
            self.q.run()
    
        if self.v is not None:
            self.v.run()
        
        if self.a is not None:
            self.a.run()
        
        if self.a_dot is not None:
            self.a_dot.run()
        
        if self.f is not None:
            self.f.run()
            
        if self.f_dot is not None:
            self.f_dot.run()
        
        if self.eff is not None:
            self.eff.run()
            
        if self.costs is not None:
            self.costs.run()
        
        if self.cnstr is not None:
            self.cnstr.run()

        self._shared_jnt_names.run()

        if self._is_server:
            
            if self._jnt_names is None:
                self._jnt_names = [""] * self._n_jnts
            else:
                if not len(self._jnt_names) == self._n_jnts:
                    exception = f"Joint names list length {len(self._jnt_names)} " + \
                        f"does not match the number of joints {self._n_jnts}"
                    Journal.log(self.__class__.__name__,
                        "run",
                        exception,
                        LogType.EXCEP,
                        throw_when_excep = True)
            jnt_names_written = self._shared_jnt_names.write_vec(self._jnt_names, 0)
            if not jnt_names_written:
                exception = "Could not write joint names on shared memory!"
                Journal.log(self.__class__.__name__,
                    "run",
                    exception,
                    LogType.EXCEP,
                    throw_when_excep = True)
                    
        else:
            
            if self.q is not None:

                self._n_jnts = self.q.n_rows - 7
                self._jnt_names = [""] * self._n_jnts
                while not self._shared_jnt_names.read_vec(self._jnt_names, 0):
                    Journal.log(self.__class__.__name__,
                        "run",
                        "Could not read joint names on shared memory. Retrying...",
                        LogType.WARN,
                        throw_when_excep = True)

        self._is_running = True

    def synch(self, read = True):
        
        # to be used to read updated data 
        # (before calling any read method)
        # it synchs all available data
        
        if self.q is not None:
            self.q.synch_all(read=read, retry=True)
        
        if self.v is not None:
            self.v.synch_all(read=read, retry=True)
        
        if self.a is not None:
            self.a.synch_all(read=read, retry=True)
        
        if self.a_dot is not None:
            self.a_dot.synch_all(read=read, retry=True)
        
        if self.f is not None:
            self.f.synch_all(read=read, retry=True)
            
        if self.f_dot is not None:
            self.f_dot.synch_all(read=read, retry=True)
        
        if self.eff is not None:
            self.eff.synch_all(read=read, retry=True)
            
        if self.costs is not None:
            self.costs.synch()
        
        if self.cnstr is not None:
            self.cnstr.synch()

    def close(self):

        if self.q is not None:
            self.q.close()
        
        if self.v is not None:
            self.v.close()
        
        if self.a is not None:
            self.a.close()
        
        if self.a_dot is not None:
            self.a_dot.close()
        
        if self.f is not None:
            self.f.close()
            
        if self.f_dot is not None:
            self.f_dot.close()
        
        if self.eff is not None:
            self.eff.close()
            
        if self.costs is not None:
            self.costs.close()
        
        if self.cnstr is not None:
            self.cnstr.close()
        
        if self._shared_jnt_names is not None:
            self._shared_jnt_names.close()

    def _check_running_or_throw(self,
                        name: str):

        if not self.is_running():
            exception = "RhcInternal not initialized. Did you call the run()?"
            Journal.log(self.__class__.__name__,
                name,
                exception,
                LogType.EXCEP,
                throw_when_excep = True)
        
    def write_q(self, 
                data: np.ndarray = None,
                retry = True):
        
        self._check_running_or_throw("write_q")
        if (self.q is not None) and (data is not None):
            
            if retry:
                self.q.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.q.write(data=data,
                        row_index=0, col_index=0)
    
    def write_v(self, 
            data: np.ndarray = None,
            retry = True):
        
        self._check_running_or_throw("write_v")
        if (self.v is not None) and (data is not None):
            if retry:
                self.v.write_retry(data=data,
                        row_index=0, col_index=0)
            else:

                self.v.write(data=data,
                        row_index=0, col_index=0)

    def write_a(self, 
            data: np.ndarray = None,
            retry = True):
        
        self._check_running_or_throw("write_a")
        if (self.a is not None) and (data is not None):    
            if retry:
                self.a.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.a.write(data=data,
                        row_index=0, col_index=0)
            
    def write_a_dot(self, 
        data: np.ndarray = None,
        retry = True):

        self._check_running_or_throw("write_a_dot")
        if (self.a_dot is not None) and (data is not None):
            if retry:
                self.a_dot.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.a_dot.write(data=data,
                        row_index=0, col_index=0)
    
    def write_f(self, 
        data: np.ndarray = None,
        retry = True):
        
        self._check_running_or_throw("write_f")  
        if (self.f is not None) and (data is not None): 
            if retry:
                self.f.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.f.write(data=data,
                        row_index=0, col_index=0)
    
    def write_f_dot(self, 
        data: np.ndarray = None,
        retry = True):

        self._check_running_or_throw("write_f_dot")
        if (self.f is not None) and (data is not None):
            if retry:
                self.f_dot.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.f_dot.write(data=data,
                        row_index=0, col_index=0)
    
    def write_eff(self, 
        data: np.ndarray = None,
        retry = True):

        self._check_running_or_throw("write_eff")
        if (self.eff is not None) and (data is not None):
            if retry:
                self.eff.write_retry(data=data,
                        row_index=0, col_index=0)
            else:
                self.eff.write(data=data,
                        row_index=0, col_index=0)
                
    def write_cost(self, 
                cost_name: str,
                data: np.ndarray = None,
                retry = True):

        self._check_running_or_throw("write_cost")
        if (self.costs is not None) and (data is not None):
            self.costs.write(data = data, 
                            name=cost_name,
                            retry=retry)
    
    def read_cost(self, 
            cost_name: str,
            retry = True):
        
        self._check_running_or_throw("read_cost")
        if self.costs is not None:
            return self.costs.get(cost_name)
        else:
            exception = "Cannot retrieve costs. Make sure to provide cost names and dims to Config."
            Journal.log(self.__class__.__name__,
                "read_cost",
                exception,
                LogType.EXCEP,
                throw_when_excep = True)
                    
    def write_constr(self, 
                constr_name: str,
                data: np.ndarray = None,
                retry = True):
        
        self._check_running_or_throw("write_constr")
        if (self.cnstr is not None) and (data is not None):
            self.cnstr.write(data = data, 
                            name=constr_name,
                            retry=retry)
            
    def read_constr(self, 
            constr_name,
            retry = True):
        
        self._check_running_or_throw("read_constr")
        if self.cnstr is not None:
            return self.cnstr.get(constr_name)
        else:
            exception = "Cannot retrieve constraints. Make sure to provide cost names and dims to Config."
            Journal.log(self.__class__.__name__,
                "read_constr",
                exception,
                LogType.EXCEP,
                throw_when_excep = True)