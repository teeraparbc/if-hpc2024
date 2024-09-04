#include <stdio.h>
#include <omp.h>

int main() {

    int N = 10;
    int array[N];

    // Initialize the array in parallel
    #pragma omp parallel num_threads(4)
    {
        #pragma omp for
        for (int i = 0; i < N; i++) {
            array[i] = i * i;
            printf("Thread %d initialized array[%d] = %d\n", omp_get_thread_num(), i, array[i]);
        }
    } // End of parallel region

    printf("\nArray after initialization:\n");
    for (int i = 0; i < N; i++) {
        printf("array[%d] = %d\n", i, array[i]);
    }

    return 0;
}
