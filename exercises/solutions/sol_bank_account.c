#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

typedef struct {
    double balance;
} BankAccount;

void process_transaction(BankAccount* account, char type, double amount) {
    if (type == '+') {
        // Synchronize this operation
        #pragma omp critical
        {
            account->balance += amount;
            printf("Thread %d: Deposit $%.2f, Balance: $%.2f\n", omp_get_thread_num(), amount, account->balance);
        }
    } else if (type == '-') {
        // Synchronize this operation
        #pragma omp critical
        {
            account->balance -= amount;
            printf("Thread %d: Withdrawal $%.2f, Balance: $%.2f\n", omp_get_thread_num(), amount, account->balance);
        }
    }
}

int main() {
    BankAccount account = {100000.0}; // Initial balance
    char type;
    double amount;
    int num_transactions = 0;

    omp_set_num_threads(4);

    // Open the file containing transactions
    FILE *file = fopen("transactions.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // First pass: count the number of transactions
    while (fscanf(file, " %c %lf", &type, &amount) == 2) {
        num_transactions++;
    }

    // Allocate memory for the transactions array
    char *transaction_types = (char *)malloc(num_transactions * sizeof(char));
    double *transaction_amounts = (double *)malloc(num_transactions * sizeof(double));

    // Reset the file pointer to the beginning of the file
    rewind(file);

    // Second pass: read the transactions into arrays
    int i = 0;
    while (fscanf(file, " %c %lf", &type, &amount) == 2) {
        transaction_types[i] = type;
        transaction_amounts[i] = amount;
        i++;
    }

    // Close the file
    fclose(file);

    // Process each transaction in parallel
    #pragma omp parallel for schedule(dynamic)
    for (int i = 0; i < num_transactions; i++) {
        process_transaction(&account, transaction_types[i], transaction_amounts[i]);
    }

    // Free allocated memory
    free(transaction_types);
    free(transaction_amounts);

    return 0;
}
