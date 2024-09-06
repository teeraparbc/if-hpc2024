#!/usr/bin/env python3
"""
File:       ex08_mpi_recv_irecv.py
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.array([10, 20, 30, 40], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Send...", flush=True)
    comm.Send([data, MPI.INT], dest=1)
    print(f"Process {rank}: Send completed.", flush=True)

elif rank == 1:
    print(f"Process {rank}: Waiting to receive data...", flush=True)
    data = np.empty(4, dtype='i')
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)


comm.Barrier()

if rank == 0:
    data = np.array([50, 60, 70, 80], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Send...", flush=True)
    comm.Send([data, MPI.INT], dest=1)
    print(f"Process {rank}: Send completed.", flush=True)

elif rank == 1:
    print(f"Process {rank}: Initiating Irecv to receive data...", flush=True)
    data = np.empty(4, dtype='i')
    req = comm.Irecv([data, MPI.INT], source=0)
    
    # Do some other work while waiting for the message
    print(f"Process {rank}: Doing some other work while waiting...", flush=True)
    time.sleep(2)
    
    # Wait for the receive operation to complete
    req.Wait()
    print(f"Process {rank}: Data received: {data}", flush=True)
