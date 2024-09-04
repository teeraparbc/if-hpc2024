#include <stdio.h>
#include <omp.h>

// Structure to simulate a class-like behavior
typedef struct {
    int shared_data;
} MyClass;

// Function to initialize the shared data
void init_class(MyClass* my_class, int value) {
    my_class->shared_data = value;
}

// Function that performs some operations on shared data
void process_data(MyClass* my_class) {
    #pragma omp parallel
    {
	int thread_num = omp_get_thread_num();
        // Code that only the master thread will execute
        #pragma omp master
        {
            printf("Master thread %d: initializing data...\n", thread_num);
            my_class->shared_data *= 2;  // Master thread modifies shared data
        }

        // Synchronize all threads after master has executed
        #pragma omp barrier

        // Code that only a single thread will execute
        #pragma omp single
        {
            printf("Single thread %d: printing data: %d\n", thread_num,
		   my_class->shared_data);
        }
    }
}

// Main function
int main() {
    MyClass my_class;
    init_class(&my_class, 10);  // Initialize shared data to 10

    // Process the shared data using multiple threads
    process_data(&my_class);

    return 0;
}
