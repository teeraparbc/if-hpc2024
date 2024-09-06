#!/usr/bin/env python3
"""
File:    ex23_mpi_allreduce.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Create an array with values based on the process rank
local_data = np.array([rank], dtype='i')  # 'i' for integer

# Prepare an array to hold the result of the all-reduce operation
global_sum = np.zeros(1, dtype='i')  # 'i' for integer

# Perform Allreduce operation to sum all local_data values
comm.Allreduce([local_data, MPI.INT], [global_sum, MPI.INT], op=MPI.SUM)

# Print the results
print(f"Process {rank}: local_data = {local_data[0]}, global_sum = {global_sum[0]}")

