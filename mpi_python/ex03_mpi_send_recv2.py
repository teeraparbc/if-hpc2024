#!/usr/bin/env python3
"""
File:	   ex03_mpi_send_recv2.py
"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    dict_data = {'a': 1, 'b': 3.14, 'c':1+1j}
    # No need to specify the data type
    comm.send(dict_data, dest=1, tag=11)
    print('Process 0: Sending dictionary data.')
elif rank == 1:
    # No need to define dict_data for process 1
    dict_data = comm.recv(source=0, tag=11)
    print('Process 1: Receive the dictionary data.')
    print(dict_data)

comm.barrier()

if rank == 0:
    list_data = numpy.arange(10).tolist()
    dict_data.update({'d':list_data})
    comm.send(dict_data, dest=1, tag=22)
    print('Process 0: Sending heterogenous data.')
elif rank == 1:
    dict_data = comm.recv(source=0, tag=22)
    print('Process 1: Receive the dictionary data.')
    print(dict_data)
    
