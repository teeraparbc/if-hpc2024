#!/usr/bin/env python3
"""
File:	   ex01_mpi_send_recv0.py
"""

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

randNum = numpy.zeros(1) # Need to define type of randNum first

if rank != 0:
    randNum = numpy.random.random_sample(1)
    print('Process', rank, 'drew the number ', randNum[0], \
          'and send to process 0.')
    comm.Send(randNum, dest=0, tag=rank)

else:
    print('Process', rank, 'before receiving has the number', randNum[0])
    for i in range(1, size):
        comm.Recv(randNum, source=i, tag=MPI.ANY_TAG)
        print('Process', rank, "received the number", randNum[0], \
              'from process ', i)
