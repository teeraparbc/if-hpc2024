#!/usr/bin/env python3
"""
File:       ex00_mpi_greeting.py
"""

from mpi4py import MPI

comm1 = MPI.COMM_WORLD	   # an instance of the Intracomm class
comm2 = MPI.COMM_SELF	   # another instance

rank1 = comm1.Get_rank()   # or rank
size1 = comm1.Get_size()   # or size

rank2 = comm2.rank   	   # or comm.rank
size2 = comm2.size   	   # or comm.size

print('Greeting from process ', rank1 + 1, ' of ', size1, ' in ', \
      comm1.Get_name())
print('Greeting from process ', rank2 + 1, ' of ', size2, ' in ', \
      comm2.Get_name())


