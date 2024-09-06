#include <stdio.h>
#include <stdlib.h>
#ifdef _OPENMP
#include <omp.h>
#endif

void Hello(void); /* Thread function */

int main(int argc, char* argv[]) {
    int thread_count;
    /* Get number of threads from command line */
    if (argc > 1) {
    	thread_count = strtol(argv[1], NULL, 10);
    }
    else {
    	printf("Error need a number of threads as an argument!\n");
    	exit(1);
    }

#pragma omp parallel num_threads(thread_count)
    Hello();

    printf("End of the example.\n");
    return 0;
} /* main */

void Hello(void) {

#ifdef _OPENMP
    int my_rank = omp_get_thread_num();
    int thread_count = omp_get_num_threads();
#else
    int my_rank = 0;
    int thread_count = 1;
#endif  
    printf("Hello from thread %d of %d\n", my_rank, thread_count);

} /* Hello */



