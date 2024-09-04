#include <stdio.h>
#include <stdlib.h>
#ifdef _OPENMP
#include <omp.h>
#endif

/* Size of the matrix */
#define N 3

int main(int argc, char* argv[]) {

    int      A[N][N], B[N][N], C[N][N];
    int      i, j, k;
    int      thread_count;

    if (argc > 1) {
	thread_count = strtol(argv[1], NULL, 10);
    }
    else {
	printf("Error need a number of threads as an argument!\n");
	exit(1);
    }
    
    /* Initialize matrices A and B with some values and matrix C equal zero */
#pragma omp parallel for collapse(2) num_threads(thread_count)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            A[i][j] = i + j;
            B[i][j] = i - j;
	    C[i][j] = 0;
        }
    }
    
    /* Matrix multiplication using OpenMP parallel for with num_threads */
#pragma omp parallel for collapse(2) num_threads(thread_count)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    /* Print the result matrix C */
    printf("Result matrix C:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;

} /* main */
