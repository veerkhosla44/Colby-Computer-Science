/* Veer Khosla
   CS333
   5/13/24
   This program measures memory allocation times for various data types.
*/

#include <stdio.h>
#include <stdlib.h>
#include "timing.h"

// Function to perform memory allocation and deallocation
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

// Allocator for chars
void *allocateChar(size_t size) {
    return malloc(size * sizeof(char));
}

// Allocator for doubles
void *allocateDouble(size_t size) {
    return malloc(size * sizeof(double));
}

// Free memory
void freeMemory(void *memory) {
    free(memory);
}

int main() {
    int iterations = 1000;
    int intSize = 10;
    double doubleSize = 10000000000.000;
    char charSize = 'c';

    double startTime, endTime;

    // Time memory allocation for integers
    startTime = get_time_sec(); 
    performMemoryTest(allocateInt, freeMemory, intSize, iterations);
    endTime = get_time_sec();  
    printf("Time for allocating integers: %f sec\n", endTime - startTime);

    // Time memory allocation for characters
    startTime = get_time_sec(); 
    performMemoryTest(allocateChar, freeMemory, charSize, iterations);
    endTime = get_time_sec();  
    printf("Time for allocating characters: %f sec\n", endTime - startTime);

    // Time memory allocation for doubles
    startTime = get_time_sec(); 
    performMemoryTest(allocateDouble, freeMemory, doubleSize, iterations);
    endTime = get_time_sec();  
    printf("Time for allocating doubles: %f sec\n", endTime - startTime);

    return 0;
}
