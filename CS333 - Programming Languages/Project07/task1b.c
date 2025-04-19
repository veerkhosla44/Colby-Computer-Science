/*Veer Khosla
   CS333
   5/13/24
   This program measures memory allocation times for various data types.
*/

#include <stdio.h>
#include <stdlib.h>
#include "timing.h"

// memory allocation and deallocation
void performMemoryTest(void *allocate(size_t), void deallocate(void*), size_t size, int numIterations) {
    for (int i = 0; i < numIterations; i++) {
        void *memoryBlock = allocate(size);
        deallocate(memoryBlock);
    }
}

// Allocator for integers
void *allocateInt(size_t size) {
    return malloc(size * sizeof(int));
}

// Allocator for doubles
void *allocateDouble(size_t size) {
    return malloc(size * sizeof(double));
}

// Allocator for chars
void *allocateChar(size_t size) {
    return malloc(size * sizeof(char));
}

// free mem
void freeMemory(void *memory) {
    free(memory);
}

int main() {
    int iterations = 100;
    int trials = 10;
    int intSize = 10;
    double doubleSize = 10000000.000;
    char charSize = 'c';

    double startTime, endTime;

    // trials for integers
    for (int trial = 0; trial < trials; trial++) {
        startTime = get_time_sec();
        performMemoryTest(allocateInt, freeMemory, intSize, iterations);
        endTime = get_time_sec();
        printf("Trial %d, Time for int: %f sec\n", trial + 1, endTime - startTime);
    }

    //  trials for doubles
    for (int trial = 0; trial < trials; trial++) {
        startTime = get_time_sec();
        performMemoryTest(allocateDouble, freeMemory, doubleSize, iterations);
        endTime = get_time_sec();
        printf("Trial %d, Time for double: %f sec\n", trial + 1, endTime - startTime);
    }

    //  trials for chars
    for (int trial = 0; trial < trials; trial++) {
        startTime = get_time_sec();
        performMemoryTest(allocateChar, freeMemory, charSize, iterations);
        endTime = get_time_sec();
        printf("Trial %d, Time for char: %f sec\n", trial + 1, endTime - startTime);
    }

    return 0;
}