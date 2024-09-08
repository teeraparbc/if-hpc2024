#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#ifdef _OPENMP
#include <omp.h>
#endif

/* Ramanujan's series for 1/pi */
double ramanujan_pi(int num_terms, int num_threads) {

    double sum = 0.0;
    double factor = (2 * sqrt(2)) / 9801;

    #pragma omp parallel for num_threads(num_threads) reduction(+:sum)
    for (int k = 0; k < num_terms; k++) {
        double numerator = tgamma(4*k + 1) * (1103 + 26390*k);
        double denominator = pow(tgamma(k + 1), 4) * pow(396, 4*k);
        sum += numerator / denominator;
    }

    return 1.0 / (factor * sum);
}

int main(int argc, char* argv[]) {

    if (argc != 3) {
        printf("Usage: %s <num_terms> <num_threads>\n", argv[0]);
        exit(1);
    }

    int num_terms = atoi(argv[1]);
    int num_threads = atoi(argv[2]);

    double pi_estimate = ramanujan_pi(num_terms, num_threads);

    printf("Estimate of pi with %d terms and %d threads: %.15f\n", num_terms,
	   num_threads, pi_estimate);

    return 0;
}
