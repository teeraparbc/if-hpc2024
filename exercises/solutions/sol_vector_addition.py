#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define vector size (same for all cores)
N = 10

# Initialize a random vector for each process
local_vector = np.random.rand(N)

# Root process will collect and sum all vectors
if rank == 0:
    total_sum = np.zeros(N)  # Vector to store the sum of all vectors
else:
    total_sum = None  # Other processes don't need the full vector

# Non-blocking send each core's vector to the root
if rank != 0:
    # Non-root processes send their vector to the root (rank 0)
    comm.Isend([local_vector, MPI.DOUBLE], dest=0, tag=rank)
else:
    # Root process (rank 0) receives vectors from all cores
    for i in range(1, size):
        recv_buffer = np.zeros(N)  # Buffer to hold each received vector
        req = comm.Irecv([recv_buffer, MPI.DOUBLE], source=i, tag=i)
        req.Wait()
        total_sum += recv_buffer  # Add the received vector to the sum
    
    # Root also adds its own vector
    total_sum += local_vector

# Root process sends the result (total_sum) back to all other processes
if rank == 0:
    for i in range(1, size):
        comm.Isend([total_sum, MPI.DOUBLE], dest=i, tag=i+size)
else:
    # Non-root processes receive the total sum from the root
    req = comm.Irecv([local_vector, MPI.DOUBLE], source=0, tag=rank+size)
    req.Wait()

# Now all processes have the summed vector in `local_vector`
print(f"Process {rank}: Resulting summed vector received.")

if rank == 0:
    print(f"The sum of the vector is \n{total_sum}")
