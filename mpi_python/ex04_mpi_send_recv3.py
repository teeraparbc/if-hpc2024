#!/usr/bin/env python3
"""
File:	   ex04_mpi_send_recv3.py
"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Non-blocking communication
if rank == 0:
    data = numpy.random.randint(100, size=100)
    req = comm.isend(data, dest=1, tag=111)
    print('Process 0: Sending a request to process 1!')
    req.wait()
    print('Process 0: Finished data transfer!')
elif rank == 1:
    req = comm.irecv(source=0, tag=111)
    print('Process 1: Receiving a request from process 0!')
    data = req.wait()
    print('Process 1: data ', data)
    
