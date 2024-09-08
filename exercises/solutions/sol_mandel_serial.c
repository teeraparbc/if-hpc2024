#include <stdio.h>
#include <stdlib.h>

#define WIDTH 800
#define HEIGHT 800
#define MAX_ITER 1000

int mandelbrot(double real, double imag) {
    double z_real = 0, z_imag = 0;
    int iter = 0;

    while (z_real * z_real + z_imag * z_imag <= 4.0 && iter < MAX_ITER) {
        double temp = z_real * z_real - z_imag * z_imag + real;
        z_imag = 2.0 * z_real * z_imag + imag;
        z_real = temp;
        iter++;
    }

    return iter;
}

int main() {
    FILE *fp = fopen("mandelbrot.dat", "w");
    if (fp == NULL) {
        perror("Unable to open file");
        return 1;
    }

    double min_real = -2.0, max_real = 1.0;
    double min_imag = -1.5, max_imag = 1.5;

    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double real = min_real + (max_real - min_real) * x / (WIDTH - 1);
            double imag = min_imag + (max_imag - min_imag) * y / (HEIGHT - 1);
            int value = mandelbrot(real, imag);

            fprintf(fp, "%d %d %d\n", x, y, value);
        }
    }

    fclose(fp);
    printf("Mandelbrot set data written to mandelbrot.dat\n");
    return 0;
}
