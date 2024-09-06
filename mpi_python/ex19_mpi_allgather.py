#!/usr/bin/env python3
"""
File: ex19_mpi_allgather.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("-" * 78)
    print(" Running on %d cores" % size)
    print("-" * 78, flush=True)

# Number of elements each process will work on
my_N = 4
N = my_N * size  # Total number of elements across all processes

# Root process initializes the data
if rank == 0:
    A = np.arange(N, dtype=np.float64)
else:
    A = np.empty(N, dtype=np.float64)  # Allocate memory on all processes

# Each process will store a chunk of the data in my_A
my_A = np.empty(my_N, dtype=np.float64)

# Scatter data from root to all processes
comm.Scatter([A, MPI.DOUBLE], [my_A, MPI.DOUBLE])

if rank == 0:
    print("\nAfter Scatter:", flush=True)

# Print each process's chunk of data after scatter
print(f"[{rank}] Received chunk: {my_A}", flush=True)

# Perform some computation (e.g., multiplying each element by 2)
my_A *= 2

# Now all processes gather the results back into A
comm.Allgather([my_A, MPI.DOUBLE], [A, MPI.DOUBLE])

# After Allgather, print the result in rank 0
if rank == 0:
    print("\nAfter AllGather:")
    print(f"Allgathered data in A: {A}", flush=True)

# Print data from all processes after the gather
print(f"[{rank}] Final result: {A}", flush=True)
