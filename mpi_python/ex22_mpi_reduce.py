#!/usr/bin/env python3
"""
File:    ex22_mpi_reduce.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Ensure all processes start at the same time
comm.Barrier()
t_start = MPI.Wtime()

# Create an array of zeros on each process
data = np.zeros(5, dtype='d')  # Ensure the data type is double ('d')

# Set values in the array; each process sets different values
for i in range(rank, len(data), size):
    data[i] = i

# Ensure all processes have completed setting their data
comm.Barrier()

# Print out the data arrays for each process
for r in range(size):
    if rank == r:
        print(f'Process {rank} has data: {data}', flush=True)

comm.Barrier()

# Prepare for the reduction operation
totals = np.zeros_like(data) if rank == 0 else None

# Perform the reduction operation (sum all data arrays)
comm.Reduce([data, MPI.DOUBLE], [totals, MPI.DOUBLE], op=MPI.SUM, root=0)

# Only the root process will have the result
if rank == 0:
    print(f'The total sum is: {totals}', flush=True)

# Final barrier to synchronize before timing
comm.Barrier()
t_diff = MPI.Wtime() - t_start

# Print the total time taken by the root process
if rank == 0:
    print(f'Total time used: {t_diff:.4f} seconds', flush=True)
