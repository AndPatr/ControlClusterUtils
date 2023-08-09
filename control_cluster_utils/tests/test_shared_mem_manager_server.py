from control_cluster_utils.utilities.shared_mem import SharedMemSrvr

import torch

import time

import random

def profile_copy_cuda_cpu():
    
    n_samples = 100

    n_envs = 100
    n_jnts = 60

    dtype = torch.float32

    server_state = SharedMemSrvr(n_envs, n_jnts, "state", 
                    dtype=dtype)
    for i in range(server_state.tensor_view.shape[0]):

        server_state.tensor_view[i, :] = torch.full((1, server_state.tensor_view.shape[1]), 
                                        i,
                                        dtype=server_state.dtype)
    
    server_cmds = SharedMemSrvr(n_envs, n_jnts, "cmds", 
                    dtype=dtype)
    for i in range(server_state.tensor_view.shape[0]):

        server_cmds.tensor_view[i, :] = torch.full((1, server_cmds.tensor_view.shape[1]), 
                                        i,
                                        dtype=server_cmds.dtype)
        
    fake_state = torch.full((n_envs, n_jnts), random.random(),
                    dtype=server_state.dtype, device=torch.device("cuda"))
    
    fake_cmds = torch.full((n_envs, n_jnts), random.random(),
                    dtype=server_cmds.dtype, device=torch.device("cuda"))
    
    for i in range(0, n_samples):
        
        print("###########################")
        
        t = time.monotonic()
        server_state.tensor_view[:, :] = fake_state.cpu()
        torch.cuda.synchronize()
        t_end = time.monotonic() - t 
        print("time 2 copy from cuda to cpu: " + str(t_end))
        print(server_state.tensor_view)

        t = time.monotonic()
        fake_cmds[:, :] = server_cmds.tensor_view.cuda()
        torch.cuda.synchronize()
        t_end = time.monotonic() - t 
        print("time 2 copy from cpu to cuda: " + str(t_end))
        print(fake_cmds)

        time.sleep(0.1)

def profile_reading_bool_array():

    n_samples = 100

    n_envs = 100
    n_jnts = 1

    dtype = torch.bool

    server = SharedMemSrvr(n_envs, n_jnts, "solved", 
                    dtype=dtype)

    for i in range(0, n_samples):
        
        print("###########################")

        t = time.monotonic()
        
        print(server.all())

        t_end = time.monotonic() - t 

        print("time 2 check bool array: " + str(t_end))

        time.sleep(0.1)

def profile_writing_global_bool():

    n_samples = 100

    dtype = torch.bool

    server = SharedMemSrvr(1, 1, "trigger", 
                    dtype=dtype)

    for i in range(0, n_samples):
        
        print("###########################")

        if i > n_samples/2:

            t = time.monotonic()

            server.reset_bool(to_true = True)

            t_end = time.monotonic() - t 

            print("time 2 set global bool array: " + str(t_end))

        time.sleep(0.1)

if __name__ == "__main__":

    profile_writing_global_bool()

    profile_reading_bool_array()

    profile_copy_cuda_cpu()