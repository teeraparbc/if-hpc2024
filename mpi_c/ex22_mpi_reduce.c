/*
 * File:    ex22_mpi_reduce.c
 */

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Ensure all processes start at the same time
    MPI_Barrier(MPI_COMM_WORLD);
    double t_start = MPI_Wtime();

    // Create an array of zeros on each process
    int N = 5;
    double data[N];
    for (int i = 0; i < N; i++) {
        data[i] = 0.0;
    }

    // Set values in the array; each process sets different values
    for (int i = rank; i < N; i += size) {
        data[i] = (double)i;
    }

    // Ensure all processes have completed setting their data
    MPI_Barrier(MPI_COMM_WORLD);

    // Print out the data arrays for each process
    for (int r = 0; r < size; r++) {
        if (rank == r) {
            printf("Process %d has data: ", rank);
            for (int i = 0; i < N; i++) {
                printf("%f ", data[i]);
            }
            printf("\n");
        }
        MPI_Barrier(MPI_COMM_WORLD);  // Synchronize before printing the next process' data
    }

    // Prepare for the reduction operation
    double totals[N];
    if (rank == 0) {
        for (int i = 0; i < N; i++) {
            totals[i] = 0.0;
        }
    }

    // Perform the reduction operation (sum all data arrays)
    MPI_Reduce(data, totals, N, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Only the root process will have the result
    if (rank == 0) {
        printf("The total sum is: ");
        for (int i = 0; i < N; i++) {
            printf("%f ", totals[i]);
        }
        printf("\n");
    }

    // Final barrier to synchronize before timing
    MPI_Barrier(MPI_COMM_WORLD);
    double t_diff = MPI_Wtime() - t_start;

    // Print the total time taken by the root process
    if (rank == 0) {
        printf("Total time used: %f seconds\n", t_diff);
    }

    MPI_Finalize();
    return 0;
}
