#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include "my_timing.h"

#define NUM_THREADS 8

int counts[10] = {0};
pthread_mutex_t mutexes[10];

typedef struct {
    double *data;
    int start;
    int end;
} thread_data_t;

int loadData(const char *filename, double **data) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) {
        perror("fopen");
        return -1;
    }

    int N;
    fread(&N, sizeof(int), 1, fp);
    *data = (double *)malloc(sizeof(double) * N);
    if (!(*data)) {
        perror("malloc");
        fclose(fp);
        return -1;
    }
    fread(*data, sizeof(double), N, fp);
    fclose(fp);

    return N;
}

int leadingDigit(double n) {
    if (fabs(n) < 1.0) {
        double temp = fabs(n);
        while (temp < 1.0) {
            temp *= 10.0;
        }
        return (int)temp;
    } else {
        long long unsigned temp = (long long unsigned)fabs(n);
        while (temp >= 10) {
            temp /= 10;
        }
        return (int)temp;
    }
}

void *countDigits(void *arg) {
    thread_data_t *td = (thread_data_t *)arg;

    for (int i = td->start; i < td->end; i++) {
        int digit = leadingDigit(td->data[i]);
        pthread_mutex_lock(&mutexes[digit]);
        counts[digit]++;
        pthread_mutex_unlock(&mutexes[digit]);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input file>\n", argv[0]);
        return 1;
    }

    double *data;
    int N = loadData(argv[1], &data);
    if (N <= 0) {
        fprintf(stderr, "Failed to load data from file\n");
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        pthread_mutex_init(&mutexes[i], NULL);
    }

    struct timespec start, end;
    double elapsed;

    clock_gettime(CLOCK_MONOTONIC, &start);

    pthread_t threads[NUM_THREADS];
    thread_data_t td[NUM_THREADS];
    int chunk_size = N / NUM_THREADS;

    for (int i = 0; i < NUM_THREADS; i++) {
        td[i].data = data;
        td[i].start = i * chunk_size;
        td[i].end = (i == NUM_THREADS - 1) ? N : (i + 1) * chunk_size;

        pthread_create(&threads[i], NULL, countDigits, &td[i]);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    clock_gettime(CLOCK_MONOTONIC, &end);
    elapsed = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

    printf("Elapsed time: %.4f seconds\n", elapsed);

    for (int i = 1; i < 10; i++)
        printf("Digit %d: %d\n", i, counts[i]);

    free(data);
    return 0;
}
