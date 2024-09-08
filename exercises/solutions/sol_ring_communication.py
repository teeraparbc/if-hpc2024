#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# The message to pass along the ring
if rank == 0:
    message = f"Message from process {rank}"
else:
    message = None

# Ring communication: each process sends to the next and receives from the previous
next_rank = (rank + 1) % size
prev_rank = (rank - 1 + size) % size

# First process (rank 0) starts by sending a message
if rank == 0:
    comm.send(message, dest=next_rank)
    message = comm.recv(source=prev_rank)
    print(f"Process {rank} received: {message}")
else:
    # Other processes receive, print, then send
    message = comm.recv(source=prev_rank)
    print(f"Process {rank} received: {message}")
    comm.send(f"Message from process {rank}", dest=next_rank)
