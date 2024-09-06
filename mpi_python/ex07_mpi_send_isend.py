#!/usr/bin/env python3
"""
File:       ex07_mpi_send_isend.py
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

### Example 1: Blocking Send (MPI_Send)

if rank == 0:
    data = np.array([1, 2, 3, 4], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Send...", flush=True)
    start = time.time()
    comm.Send([data, MPI.INT], dest=1)
    end = time.time()
    print(f"Process {rank}: Send completed in {end - start:.5f} seconds", flush=True)
elif rank == 1:
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Receiving data...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

comm.Barrier()  # Synchronize processes

### Example 2: Non-blocking Send (MPI_Isend)

if rank == 0:
    data = np.array([5, 6, 7, 8], dtype='i')
    print(f"\nProcess {rank}: Sending data with MPI_Isend...", flush=True)
    start = time.time()
    request = comm.Isend([data, MPI.INT], dest=1)
    # Do some other work while the message is being sent
    print(f"Process {rank}: Doing some work while waiting...", flush=True)
    request.Wait()  # Wait for the send to complete
    end = time.time()
    print(f"Process {rank}: Isend completed in {end - start:.5f} seconds", flush=True)
elif rank == 1:
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Receiving data...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

# Final barrier to synchronize
comm.Barrier()
