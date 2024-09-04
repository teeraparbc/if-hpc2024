#include <stdio.h>
#include <omp.h>
#include <unistd.h> // for sleep function

#define N 10

int main() {
    int i;

    // Parallel loop with dynamic scheduling
    #pragma omp parallel for schedule(dynamic) num_threads(4)
    for (i = 0; i < N; i++) {
        int sleep_time = (i % 3 + 1); // Variable sleep time for each iteration
        printf("Thread %d processing index %d, sleep time = %d seconds\n", omp_get_thread_num(), i, sleep_time);
        sleep(sleep_time); // Simulate work by sleeping
    }

    return 0;
}
