#!/usr/bin/env python3
"""
File:	   ex05_mpi_send_ssend.py
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# First communication block: Synchronous MPI_Ssend / MPI_Recv
if rank == 0:
    data = np.array([1, 2, 3, 4], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Ssend...", flush=True)
    comm.Ssend([data, MPI.INT], dest=1)
    print(f"Process {rank}: Ssend completed.", flush=True)
elif rank == 1:
    time.sleep(2)  # Simulate a delay in receiving
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Receiving data...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

# Barrier to ensure all processes complete the first communication
comm.Barrier()  # All processes wait here until Send/Recv + print are done

# Second communication block: Standard MPI_Send
if rank == 0:
    data = np.array([1, 2, 3, 4], dtype='i')
    print(f"Process {rank}: Sending data with MPI_Send...", flush=True)
    start = time.time()
    comm.Send([data, MPI.INT], dest=1)
    end = time.time()
    print(f"Process {rank}: Send completed in {end - start:.5f} seconds", flush=True)
elif rank == 1:
    time.sleep(2)  # Simulate a delay in receiving
    data = np.empty(4, dtype='i')
    print(f"Process {rank}: Receiving data...", flush=True)
    comm.Recv([data, MPI.INT], source=0)
    print(f"Process {rank}: Data received: {data}", flush=True)

# Final Barrier to ensure all processes complete the second communication
comm.Barrier()
