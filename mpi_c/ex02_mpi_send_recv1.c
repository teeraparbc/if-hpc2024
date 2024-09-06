/*
 * File:    ex02_mpi_send_recv1.c
 */

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // First part: sending and receiving integer array
    if (rank == 0) {
        int data[10];
        for (int i = 0; i < 10; i++) {
            data[i] = i;
        }
        MPI_Send(data, 10, MPI_INT, 1, 77, MPI_COMM_WORLD);
        printf("Sending integer array from process %d\n", rank);
    } else if (rank == 1) {
        int data[10];
        MPI_Recv(data, 10, MPI_INT, 0, 77, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Receiving integer array from process %d: \n", rank);
        for (int i = 0; i < 10; i++) {
            printf("%d ", data[i]);
        }
        printf("\n");
    }

    MPI_Barrier(MPI_COMM_WORLD);  // Synchronize processes

    // Second part: sending and receiving float array
    if (rank == 0) {
        double data[10];
        for (int i = 0; i < 10; i++) {
            data[i] = (double)i;
        }
        MPI_Send(data, 10, MPI_DOUBLE, 1, 13, MPI_COMM_WORLD);
        printf("Sending float array from process %d\n", rank);
    } else if (rank == 1) {
        double data[10];
        MPI_Recv(data, 10, MPI_DOUBLE, 0, 13, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Receiving float array from process %d: \n", rank);
        for (int i = 0; i < 10; i++) {
            printf("%f ", data[i]);
        }
        printf("\n");
    }

    MPI_Barrier(MPI_COMM_WORLD);  // Synchronize processes

    // Third part: sending and receiving a message using a char array
    if (rank == 0) {
        char message[] = "Greeting from main process!";
        MPI_Send(message, strlen(message) + 1, MPI_CHAR, 1, 99, MPI_COMM_WORLD);
        printf("Sending message from process %d\n", rank);
    } else if (rank == 1) {
        char buf[256];
        MPI_Recv(buf, 256, MPI_CHAR, 0, 99, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Receiving message from process %d: %s\n", rank, buf);
    }

    MPI_Finalize();
    return 0;
}
