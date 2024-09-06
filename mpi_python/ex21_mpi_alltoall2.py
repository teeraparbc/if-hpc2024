#!/usr/bin/env python3
"""
File: ex21_mpi_alltoall2.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Ensure square grid: The number of processes should match the matrix size
matrix_size = size  # Assume we have a square matrix of size (size x size)

# Initialize the matrix: Each process holds one row of the matrix
row = np.arange(rank * matrix_size, (rank + 1) * matrix_size, dtype=int)
print(f"Process {rank}: Original row = {row}", flush=True)

# Prepare send and receive buffers for Alltoall
send_buf = np.copy(row)  # Send the row that each process holds
recv_buf = np.empty(matrix_size, dtype=int)  # Prepare to receive one column of the transposed matrix

# Perform the Alltoall operation to redistribute rows into columns
comm.Alltoall(send_buf, recv_buf)

# Print out the transposed columns
print(f"Process {rank}: Transposed column = {recv_buf}", flush=True)
