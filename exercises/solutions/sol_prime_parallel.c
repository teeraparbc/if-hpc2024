#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>

#define LIMIT 100000

void sieve(int limit, int *primes) {

    int i;
    int c;

    c = (int) sqrt(limit);
    #pragma omp parallel for schedule(dynamic)
    for (i = 2; i <= c; i++) {
        if (primes[i]) {
            for (int j = i * i; j <= limit; j += i) {
                primes[j] = 0;
            }
        }
    }
}

int main() {
    int i;
    int *primes = (int *)malloc((LIMIT + 1) * sizeof(int));

    #pragma omp parallel for num_threads(10)
    for (i = 0; i <= LIMIT; i++) {
        primes[i] = 1;
    }

    sieve(LIMIT, primes);

    
    printf("Prime numbers up to %d:\n", LIMIT);
    for (int i = 2; i <= LIMIT; i++) {
        if (primes[i]) {
            printf("%d ", i);
        }
    }
    printf("\n");
    

    free(primes);
    return 0;
}
