#include <stdio.h>
#include <omp.h>

#define N 10

int main() {
    int array[N];
    int prefix_sum[N];

    #pragma omp parallel shared(array, prefix_sum)
    {
        int i;

        // Initialize the array in parallel
        #pragma omp for
        for (i = 0; i < N; i++) {
            array[i] = i + 1;
            printf("Thread %d initialized array[%d] = %d\n", omp_get_thread_num(), i, array[i]);
        }

        // Ensure all threads have finished initializing the array before moving to the next step
        #pragma omp barrier

        // Compute the prefix sum in parallel
        #pragma omp for
        for (i = 0; i < N; i++) {
            prefix_sum[i] = 0;
            for (int j = 0; j <= i; j++) {
                prefix_sum[i] += array[j];
            }
            printf("Thread %d computed prefix_sum[%d] = %d\n", omp_get_thread_num(), i, prefix_sum[i]);
        }
    }

    // Print the final prefix sum array
    printf("Final prefix sum array:\n");
    for (int i = 0; i < N; i++) {
        printf("%d ", prefix_sum[i]);
    }
    printf("\n");

    return 0;
}
