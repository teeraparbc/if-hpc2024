#!/usr/bin/env python3
"""
File:	   ex16_mpi_iscatterv_igatherv.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Root process prepares data to scatter
if rank == 0:
    send_buf = np.arange(16, dtype='i')  # Data to scatter
    print(f"Root: Original data: {send_buf}", flush=True)
    sendcounts = np.array([2, 3, 5, 6], dtype='i')  # Number of elements each process will receive
    displs = np.array([0, 2, 5, 10], dtype='i')     # Start position for each process in send_buf
else:
    send_buf = None
    sendcounts = None
    displs = None

# Each process prepares to receive its chunk (based on sendcounts)
recv_count = 2 if rank == 0 else (rank + 1)  # Example: variable size, each rank gets different number of elements
recv_buf = np.zeros(recv_count, dtype='i')

# Non-blocking Scatterv
req_scatterv = comm.Iscatterv([send_buf, sendcounts, displs, MPI.INT], recv_buf, root=0)

# Wait for the scatter operation to complete
req_scatterv.Wait()

print(f"Process {rank} received: {recv_buf}", flush=True)

# Perform computation (e.g., doubling the values)
recv_buf *= 2

# Root process prepares buffer to gather results
if rank == 0:
    gather_buf = np.zeros(16, dtype='i')  # Full buffer to gather results
else:
    gather_buf = None

# Non-blocking Gatherv
req_gatherv = comm.Igatherv(recv_buf, [gather_buf, sendcounts, displs, MPI.INT], root=0)

# Wait for the gather operation to complete
req_gatherv.Wait()

# Root process prints the gathered result
if rank == 0:
    print(f"Root: Gathered data: {gather_buf}", flush=True)
