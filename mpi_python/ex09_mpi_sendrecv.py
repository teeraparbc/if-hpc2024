#!/usr/bin/env python3
"""
File:	   ex09_mpi_sendrecv.py
"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Sendrecv
if rank == 0:
    data_send = numpy.arange(10, dtype='i')
    data_receive = numpy.zeros(10, dtype='f')
    print('Process 0: Sending and Receiving data between process 1', flush=True)
    comm.Sendrecv(data_send, dest=1, sendtag=11, recvbuf=data_receive,
                  source=1, recvtag=22)
    print('Process 0: data received from process 1:', data_receive, flush=True)
elif rank == 1:
    data_send = numpy.arange(10, dtype='f')
    data_receive = numpy.zeros(10, dtype='i')
    print('Process 1: Sending and Receiving data between process 0', flush=True)
    comm.Sendrecv(data_send, dest=0, sendtag=22, recvbuf=data_receive,
                  source=0, recvtag=11)
    print('Process 1: data received from process 0:', data_receive, flush=True)
