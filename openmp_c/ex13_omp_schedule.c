#include <stdio.h>
#include <omp.h>

#define N 16

int main() {
    int array[N], i;

    // Initialize the array
    for (i = 0; i < N; i++) {
        array[i] = i + 1;
    }

    int sum = 0;

    // Parallelize the loop with OpenMP using the 'schedule' clause
    // You can modify the schedule(static, 4) to schedule(dynamic, 4)
    // or schedule(guided, 4) to see how the behavior changes.
    #pragma omp parallel for schedule(static, 4) reduction(+:sum)
    for (i = 0; i < N; i++) {
        sum += array[i];
        printf("Thread %d processing index %d with value %d\n", omp_get_thread_num(), i, array[i]);
    }

    printf("Final sum = %d\n", sum);

    return 0;
}
