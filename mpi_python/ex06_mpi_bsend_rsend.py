#!/usr/bin/env python3
"""
File:	   ex06_mpi_bsend_rsend.py
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Allocate a buffer for MPI_Bsend
buffer_size = MPI.BSEND_OVERHEAD + 4 * MPI.INT.Get_size()  # Overhead + size of message
buffer = np.empty(buffer_size, dtype='b')  # Allocate buffer as bytes ('b')

# Attach the buffer
MPI.Attach_buffer(buffer)

# MPI_Bsend with user-provided buffer
if rank == 0:
    data = np.array([5, 6, 7, 8], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Bsend...", flush=True)
    start = time.time()
    comm.Bsend([data, MPI.INT], dest=1)
    end = time.time()
    print(f"Process {rank}: Bsend completed in {end - start:.5f} seconds",
          flush=True)
    MPI.Detach_buffer()
elif rank == 1:
    time.sleep(2)  # Simulate a delay in receiving
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Receiving data...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

# Detach the buffer after use
MPI.Detach_buffer()

comm.Barrier()

# MPI_Rsend requires that the receive is already posted
if rank == 0:
    time.sleep(1)  # Give time for the receiver to be ready
    data = np.array([9, 10, 11, 12], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Rsend...", flush=True)
    start = time.time()
    comm.Rsend([data, MPI.INT], dest=1)
    end = time.time()
    print(f"Process {rank}: Rsend completed in {end - start:.5f} seconds",
          flush=True)
elif rank == 1:
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Posting receive...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

comm.Barrier()
