#include <stdio.h>
#include <omp.h>

#define ARRAY_SIZE 10000

int main() {
    int array[ARRAY_SIZE];
    int sum = 0;
    int i;

    // Initialize the array
    for (i = 0; i < ARRAY_SIZE; i++) {
        array[i] = i;
    }

    // Parallelize the loop only if the array size is large enough
    #pragma omp parallel for if (ARRAY_SIZE >= 1000) shared(array, sum) private(i)
    for (i = 0; i < ARRAY_SIZE; i++) {
        sum += array[i];
    }

    printf("Sum of the array: %d\n", sum);

    return 0;
}
