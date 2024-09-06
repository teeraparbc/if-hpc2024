/*
 * File:    ex12_mpi_bcast.c
 */

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        printf("----------------------------------------------------------------------------\n");
        printf(" Running on %d cores\n", size);
        printf("----------------------------------------------------------------------------\n");
    }

    MPI_Barrier(MPI_COMM_WORLD);  // Synchronize processes

    // Prepare a vector of N=5 elements to be broadcasted
    int N = 5;
    double A[N];

    if (rank == 0) {
        // Rank 0 initializes the array with data
        for (int i = 0; i < N; i++) {
            A[i] = (double)i;
        }
    }

    // Broadcast array A from rank 0 to all other processes
    MPI_Bcast(A, N, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Every process should now have the same data
    printf("[%02d] ", rank);
    for (int i = 0; i < N; i++) {
        printf("%f ", A[i]);
    }
    printf("\n");

    MPI_Finalize();
    return 0;
}
