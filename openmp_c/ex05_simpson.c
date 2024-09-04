#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double Simpson(double a, double b, int n);
double func(double x);

int main() {
    /* We'll store our result in global_result: */
    double   a, b;        /* Left and right endpoints */
    int      n;           /* Total number of trapezoid */

    printf("Enter a, b, and n\n");
    scanf("%lf %lf %d", &a, &b, &n);

    printf("With n = %d simpsons, our estimate\n", n);
    printf("of the integral from %f to %f = %.14e\n", a, b, Simpson(a, b, n));

    return 0;
} /* main */

double Simpson(double a, double b, int n) {

    double h, x, result;
    int    i, local_n;

    h = (b-a)/n;
    result = func(a) + func(b);
    for (i = 1; i <= n - 1; i++) {
        x = a + i * h;
        if (i % 2 == 0) {
            result += 2 * func(x);
        } else {
            result += 4 * func(x);
        }
    }
    result = result * h / 3;

    return result;
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
