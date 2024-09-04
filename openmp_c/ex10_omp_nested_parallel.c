#include <omp.h>
#include <stdio.h>

int main() {

    omp_set_nested(1); // Enable nested parallelism

#pragma omp parallel num_threads(4)
    {
        printf("Outer: Thread %d of %d\n", omp_get_thread_num(), omp_get_num_threads());

        // Ensure all outer threads reach this point before any of the inner threads start
#pragma omp barrier

#pragma omp parallel num_threads(2)
        {
            printf("Inner: Thread %d of %d (Outer Thread %d)\n",
                   omp_get_thread_num(), omp_get_num_threads(),
                   omp_get_ancestor_thread_num(1));
        }
    }
    return 0;
}
