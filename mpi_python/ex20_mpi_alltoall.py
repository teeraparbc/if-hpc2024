#!/usr/bin/env python3
"""
File: ex20_mpi_alltoall.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Each process will send and receive 'chunk_size' number of elements to/from each process
chunk_size = 2

# Create the send buffer: rank+1 times an array ranging from 0 to size*chunk_size
send_data = (rank + 1) * np.arange(size * chunk_size, dtype=int)

# Create the receive buffer to hold the data received from all processes
recv_data = np.empty(size * chunk_size, dtype=int)

# Perform the Alltoall operation
comm.Alltoall(send_data, recv_data)

# Print the results for each process
print(f"Process {rank}: Sent {send_data}, Received {recv_data}", flush=True)
