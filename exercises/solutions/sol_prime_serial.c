#include <stdio.h>
#include <stdlib.h>

#define LIMIT 100000

void sieve(int limit, int *primes) {
    for (int i = 2; i * i <= limit; i++) {
        if (primes[i]) {
            for (int j = i * i; j <= limit; j += i) {
                primes[j] = 0;
            }
        }
    }
}

int main() {
    int *primes = (int *)malloc((LIMIT + 1) * sizeof(int));
    for (int i = 0; i <= LIMIT; i++) {
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
