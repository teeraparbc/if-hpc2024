#!/usr/bin/env python3
"""
File:	   ex17_mpi_iscatter_igather.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define total data size and chunk size for each process
N = 16  # Total number of elements
chunk_size = N // size  # Size of each chunk (assuming size divides N perfectly)

# Root process prepares data to be scattered
if rank == 0:
    send_buf = np.arange(N, dtype='i')  # Create an array with values 0 to N-1
    print(f"Root: Original data: {send_buf}", flush=True)
else:
    send_buf = None

# Each process will receive a chunk of the data
recv_buf = np.zeros(chunk_size, dtype='i')

# Non-blocking scatter
req_scatter = comm.Iscatter(send_buf, recv_buf, root=0)

# Wait for the scatter to complete
req_scatter.Wait()

print(f"Process {rank} received: {recv_buf}", flush=True)

# Perform some computation on the received data
recv_buf *= 2  # Example: double the values

# Prepare buffer on the root to gather results
if rank == 0:
    gather_buf = np.zeros(N, dtype='i')
else:
    gather_buf = None

# Non-blocking gather
req_gather = comm.Igather(recv_buf, gather_buf, root=0)

# Wait for the gather to complete
req_gather.Wait()

# Root process prints the gathered result
if rank == 0:
    print(f"Root: Gathered data: {gather_buf}", flush=True)
