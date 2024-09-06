#!/usr/bin/env python3
"""
File:	   ex14_mpi_ibarrier.py
"""

from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Simulate work before the barrier
print(f"Process {rank} is doing some work before the barrier...", flush=True)
time.sleep(rank + 1)  # Different sleep times for each process to simulate work
print(f"Process {rank} reached the non-blocking barrier.", flush=True)

# Non-blocking barrier
req = comm.Ibarrier()

# Do some additional work while waiting for the barrier to complete
for i in range(5):
    print(f"Process {rank} is doing some work after reaching the barrier (iteration {i})...")
    time.sleep(0.5)

# Wait for the barrier to complete
req.Wait()

# Now, all processes should have reached the barrier
print(f"Process {rank} finished waiting at the barrier.", flush=True)
