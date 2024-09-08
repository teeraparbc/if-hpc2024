#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#ifdef _OPENMP
#include <omp.h>
#endif

void Simpson(double a, double b, int n, double* global_result_p);
double func(double x);

int main(int argc, char* argv[]) {
    /* We'll store our result in global_result: */
    double   global_result = 0.0;
    double   a, b;        /* Left and right endpoints */
    int      n;           /* Total number of trapezoid */
    int      thread_count;

    if (argc > 1) {
	thread_count = strtol(argv[1], NULL, 10);
    }
    else {
	printf("Error need a number of threads as an argument!\n");
	exit(1);
    }
    printf("Enter a, b, and n\n");
    scanf("%lf %lf %d", &a, &b, &n);
#pragma omp parallel num_threads(thread_count)
    Simpson(a, b, n, &global_result);

    printf("With n = %d simpsons, our estimate\n", n);
    printf("of the integral from %f to %f = %.14e\n", a, b, global_result);

    return 0;
} /* main */

void Simpson(double a, double b, int n, double *global_result_p) {

    double h, x, my_result;
    double local_a, local_b;
    int    i, local_n;
#ifdef _OPENMP
    int my_rank = omp_get_thread_num();
    int thread_count = omp_get_num_threads();
#else
    int my_rank = 0;
    int thread_count = 1;
#endif

    h = (b-a)/n;
    local_n = n/thread_count;
    local_a = a + my_rank * local_n * h;
    local_b = local_a + local_n * h;
    my_result = func(local_a) + func(local_b);
    for (i = 1; i <= local_n - 1; i++) {
        x = local_a + i * h;
        if (i % 2 == 0) {
            my_result += 2 * func(x);
        } else {
            my_result += 4 * func(x);
        }
    }
    my_result = my_result * h / 3;

#pragma omp critical
    *global_result_p += my_result;
}

double func(double x) {
    double a0,a1,a2,a3,a4,a5;

    a0 = 4.0;
    a1 = 6.069828395061729;
    a2 = -2.794364197530864;
    a3 = 0.3736801440329219;
    a4 = -0.015674668495656158;
    a5 = 0.0001;

    return a5 * pow(x, 5) + a4 * pow(x, 4) + a3 * pow(x, 3) + a2 * pow(x, 2)
	+ a1 * x + a0;
}
