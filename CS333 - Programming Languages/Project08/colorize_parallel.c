#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "ppmIO.h"

typedef struct {
    Pixel *src;
    int start;
    int end;
} thread_data_t;

void *process_image(void *arg) {
    thread_data_t *td = (thread_data_t *)arg;
    for (int i = td->start; i < td->end; i++) {
        td->src[i].r = td->src[i].r > 128 ? (220 + td->src[i].r) / 2 : (30 + td->src[i].r) / 2;
        td->src[i].g = td->src[i].g > 128 ? (220 + td->src[i].g) / 2 : (30 + td->src[i].g) / 2;
        td->src[i].b = td->src[i].b > 128 ? (220 + td->src[i].b) / 2 : (30 + td->src[i].b) / 2;
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    Pixel *src;
    int rows, cols, colors;

    // check usage
    if (argc < 3) {
        printf("Usage: %s <image filename> <num_threads>\n", argv[0]);
        exit(-1);
    }

    int num_threads = atoi(argv[2]);
    if (num_threads != 1 && num_threads != 2 && num_threads != 4) {
        printf("Number of threads must be 1, 2, or 4\n");
        exit(-1);
    }

    // read image and check for errors
    src = ppm_read(&rows, &cols, &colors, argv[1]);
    if (!src) {
        printf("Unable to read file %s\n", argv[1]);
        exit(-1);
    }

    pthread_t threads[num_threads];
    thread_data_t td[num_threads];
    int chunk_size = (rows * cols) / num_threads;

    for (int i = 0; i < num_threads; i++) {
        td[i].src = src;
        td[i].start = i * chunk_size;
        td[i].end = (i == num_threads - 1) ? (rows * cols) : ((i + 1) * chunk_size);
        pthread_create(&threads[i], NULL, process_image, &td[i]);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    // write out the image
    ppm_write(src, rows, cols, colors, "bold_parallel.ppm");

    free(src);

    return 0;
}