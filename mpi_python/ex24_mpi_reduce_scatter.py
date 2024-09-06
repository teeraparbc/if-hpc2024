#!/usr/bin/env python3
"""
File:    ex24_mpi_reduce_scatter.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Ensure all processes start the timer at the same time
comm.Barrier()
t_start = MPI.Wtime()

# Each process initializes its local data
data = np.zeros(10, dtype='d')  # Use double precision floating point
for i in range(rank, len(data), size):
    data[i] = i

# Print data on each process
comm.Barrier()
print(f"Process {rank} has data: {data}")

# Define recvcounts: each process will receive part of the result
recvcounts = np.array([5] * size, dtype='i')  # Each process will receive 5 elements
totals = np.zeros(5, dtype='d')  # Prepare to receive partial sums

# Perform the reduce_scatter operation
comm.Reduce_scatter([data, MPI.DOUBLE], [totals, MPI.DOUBLE], recvcounts=recvcounts, op=MPI.SUM)

# Print the result on each process
print(f"Process {rank}: The reduced scatter result is {totals}")

# Ensure all processes finish before measuring the elapsed time
comm.Barrier()
t_diff = MPI.Wtime() - t_start
if rank == 0:
    print(f"Total time used: {t_diff:.6f} seconds")
