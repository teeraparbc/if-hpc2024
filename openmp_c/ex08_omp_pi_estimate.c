#include <stdio.h>
#include <stdlib.h>
#ifdef _OPENMP
#include <omp.h>
#endif

int main(int argc, char* argv[]) {

    double   pi_approx = 0., sum = 0.;
    double   factor;
    int      k;
    int      n = 1000; /* number of terms */
    int      thread_count;

    if (argc > 1) {
	thread_count = strtol(argv[1], NULL, 10);
    }
    else {
	printf("Error need a number of threads as an argument!\n");
	exit(1);
    }

#pragma omp parallel for num_threads(thread_count) reduction(+:sum) \
    private(factor)
    for (k = 0; k < n; k++) {
	if (k % 2 == 0)
	    factor = 1.0;
	else
	    factor = -1.0;
	sum += factor / (2 * k + 1);
    }

    pi_approx = 4 * sum;

    printf("With n = %4d terms and %d threads,\n", n, thread_count);
    printf("    Our estimate of pi = %16.14f\n", pi_approx);
    return 0;
}
