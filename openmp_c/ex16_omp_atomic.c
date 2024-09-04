#include <stdio.h>
#include <omp.h>

typedef struct {
    int count;
} Counter;

// Function to initialize the counter
void init_counter(Counter* counter) {
    counter->count = 0;
}

// Function to increment the counter using the atomic directive
void increment(Counter* counter) {
    #pragma omp atomic
    counter->count++;
}

// Function to get the current value of the counter
int get_count(Counter* counter) {
    return counter->count;
}

int main() {
    Counter counter;
    init_counter(&counter);

    // Parallel region where multiple threads increment the counter
    #pragma omp parallel for
    for (int i = 0; i < 1000; i++) {
        increment(&counter);
    }

    // Output the final value of the counter
    printf("Final count: %d\n", get_count(&counter));

    return 0;
}
