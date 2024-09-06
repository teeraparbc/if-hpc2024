#!/usr/bin/env python3
"""
File:       ex10_mpi_sendrecv2.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the data each process will send (the rank of the process)
send_data = np.array([rank], dtype='i')

# Prepare a variable to receive the data
recv_data = np.empty(1, dtype='i')

# Determine the neighbors in the ring
# Each process sends to (rank + 1) % size and receives from (rank - 1) % size
send_to = (rank + 1) % size
recv_from = (rank - 1 + size) % size

# Use Sendrecv to send data to the next process and receive data from the previous one
print(f"Process {rank}: Sending {send_data[0]} to process {send_to} and waiting to receive from process {recv_from}...", flush=True)
comm.Sendrecv(sendbuf=send_data, dest=send_to, recvbuf=recv_data, source=recv_from)

# Print the result
print(f"Process {rank}: Received {recv_data[0]} from process {recv_from}", flush=True)
