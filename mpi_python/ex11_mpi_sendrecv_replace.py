#!/usr/bin/env python3
"""
File:       ex11_mpi_sendrecv_replace.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Prepare the buffer for sending and receiving data
data = np.array([rank], dtype='i')

# Determine neighbors in the ring
send_to = (rank + 1) % size
recv_from = (rank - 1 + size) % size

# Use Sendrecv_replace to send data and receive data into the same buffer
print(f"Process {rank}: Sending and receiving data...", flush=True)
comm.Sendrecv_replace(data, dest=send_to, source=recv_from)

# Print the results
print(f"Process {rank}: Received {data[0]} from process {recv_from}", flush=True)
