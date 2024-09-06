#!/usr/bin/env python3
"""
File:	   ex02_mpi_send_recv1.py
"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(10, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print('Sending integer array from process ', rank)
elif rank == 1:
    data = numpy.empty(10, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print('Receiving integer array:', data)

comm.Barrier() # Synchronize processes

# automatic MPI datatype discovery
if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
    print('Sending float array from process ', rank)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print('Receiving float array:', data)

comm.Barrier() # Synchronize processes

if comm.rank == 0:
    # Sending message using bytearray
    comm.Send([b'Greeting from main process!',MPI.CHAR],dest=1)
elif comm.rank == 1:
    buf = bytearray(256)
    comm.Recv([buf,MPI.CHAR],source=0)
    # Decode the string to remove the empty characters from bytearray
    print(buf.decode('utf-8'))
