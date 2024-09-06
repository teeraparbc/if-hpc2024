#!/usr/bin/env python3
"""
File:	   ex16_mpi_scatterv_gatherv.py
"""

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# scatter a numpy array by using Scatterv
if rank == 0:
    send_buf = np.arange(10, dtype='i')
    print('Original data', send_buf,flush=True)
else:
    send_buf = None

recv_buf = np.zeros(rank+1, dtype='i')
count = [1, 2]
displ = [2, 4]

if rank == 0:
    print('---------- Starting Scatterv ----------',flush=True)

comm.Scatterv([send_buf, count, displ, MPI.INT], recv_buf, root=0)


print('Scatterv: rank %d has %s' % (rank, recv_buf),flush=True)
comm.Barrier()

if rank == 0:
    print('---------- Change Something -----------',flush=True)

comm.Barrier()

# Doing some change
recv_buf *= 2
print('Change: rank %d has %s' % (rank, recv_buf),flush=True)
comm.Barrier()

if rank == 0:
    print('------------- Now Gatherv -------------',flush=True)

comm.Barrier()
comm.Gatherv(recv_buf, [send_buf, count, displ, MPI.INT], root=0)
print('Gatherv: rank %d has %s' % (rank, send_buf),flush=True)
