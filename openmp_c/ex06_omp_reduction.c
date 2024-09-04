#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 100

int main() {
    double array[ARRAY_SIZE];
    double sum = 0.0;
    double product = 1.0;
    double min_value = 1.0;  // Initializing to maximum possible value since the array contains values between 0 and 1
    double max_value = 0.0;  // Initializing to minimum possible value

    // Seed the random number generator
    srand(time(NULL));

    // Initialize the array with random values
    for (int i = 0; i < ARRAY_SIZE; i++) {
        array[i] = (double) rand() / (double) RAND_MAX;
    }

    // Use reduction clauses for various operations
    #pragma omp parallel for reduction(+:sum) reduction(*:product) reduction(min:min_value) reduction(max:max_value)
    for (int i = 0; i < ARRAY_SIZE; i++) {
        sum += array[i];
        product *= array[i];
        min_value = (array[i] < min_value) ? array[i] : min_value;
        max_value = (array[i] > max_value) ? array[i] : max_value;
    }

    printf("Sum: %f\n", sum);             // Corrected to %f for double
    printf("Product: %g\n", product);     // Corrected to %f for double
    printf("Minimum value: %f\n", min_value);  // Corrected to %f for double
    printf("Maximum value: %f\n", max_value);  // Corrected to %f for double

    return 0;
}
