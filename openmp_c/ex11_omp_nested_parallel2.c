#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#define MATRIX_SIZE 10

int main() {
    int **matrixA, **matrixB, **matrixC;
    int i, j, k;

    // Allocate memory for matrices
    matrixA = (int **)malloc(MATRIX_SIZE * sizeof(int *));
    matrixB = (int **)malloc(MATRIX_SIZE * sizeof(int *));
    matrixC = (int **)malloc(MATRIX_SIZE * sizeof(int *));
    for (i = 0; i < MATRIX_SIZE; ++i) {
        matrixA[i] = (int *)malloc(MATRIX_SIZE * sizeof(int));
        matrixB[i] = (int *)malloc(MATRIX_SIZE * sizeof(int));
        matrixC[i] = (int *)malloc(MATRIX_SIZE * sizeof(int));
    }

    // Initialize matrices with random values
    srand(time(NULL));
    for (i = 0; i < MATRIX_SIZE; ++i) {
        for (j = 0; j < MATRIX_SIZE; ++j) {
            matrixA[i][j] = rand() % 100;
            matrixB[i][j] = rand() % 100;
        }
    }

    // Perform matrix multiplication using nested parallelism
    #pragma omp parallel for shared(matrixA, matrixB, matrixC) private(i, j, k)
    for (i = 0; i < MATRIX_SIZE; ++i) {
        #pragma omp parallel for shared(matrixA, matrixB, matrixC, i) private(j, k)
        for (j = 0; j < MATRIX_SIZE; ++j) {
            matrixC[i][j] = 0;
            for (k = 0; k < MATRIX_SIZE; ++k) {
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    // Print the matrices
    printf("Matrix A:\n");
    for (i = 0; i < MATRIX_SIZE; ++i) {
        for (j = 0; j < MATRIX_SIZE; ++j) {
            printf("%3d ", matrixA[i][j]);
        }
        printf("\n");
    }

    printf("\nMatrix B:\n");
    for (i = 0; i < MATRIX_SIZE; ++i) {
        for (j = 0; j < MATRIX_SIZE; ++j) {
            printf("%3d ", matrixB[i][j]);
        }
        printf("\n");
    }

    printf("\nMatrix C (Result):\n");
    for (i = 0; i < MATRIX_SIZE; ++i) {
        for (j = 0; j < MATRIX_SIZE; ++j) {
            printf("%3d ", matrixC[i][j]);
        }
        printf("\n");
    }

    // Free memory
    for (i = 0; i < MATRIX_SIZE; ++i) {
        free(matrixA[i]);
        free(matrixB[i]);
        free(matrixC[i]);
    }
    free(matrixA);
    free(matrixB);
    free(matrixC);

    return 0;
}
