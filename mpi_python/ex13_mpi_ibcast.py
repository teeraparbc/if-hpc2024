#!/usr/bin/env python3
"""
File:	   ex13_mpi_ibcast.py
"""

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Rank 0 initializes the data
if rank == 0:
    data = np.array([1, 2, 3, 4], dtype='i')
    print(f"Process {rank} broadcasting data: {data}", flush=True)
else:
    data = np.empty(4, dtype='i')

# Non-blocking broadcast (Ibcast)
request = comm.Ibcast(data, root=0)

# Perform some work while the broadcast is in progress
print(f"Process {rank} is doing some other work...", flush=True)
time.sleep(1)

# Wait for the non-blocking broadcast to complete
request.Wait()

# After the broadcast completes, every process should have the same data
print(f"Process {rank} received data: {data}", flush=True)
