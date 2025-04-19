/**
 * Define struct versions with varying arrangements
 *
 * Veer Khosla
 * 2/22/24 
 */

#include <stdio.h>
#include <stdlib.h>
        
/* 
 */ 
struct Version1 {
    char c1; // 1 byte
    int i;   // 4 bytes
    char c2; // 1 byte
    short s; // 2 bytes
};

struct Version2 {
    char c1; // 1 byte
    char c2; // 1 byte
    int i;   // 4 bytes
    short s; // 2 bytes
};

struct Version3 {
    int i;   // 4 bytes
    short s; // 2 bytes
    char c1; // 1 byte
    char c2; // 1 byte
};


void inspectMemoryLayout(void *ptr, size_t size) {
    unsigned char *bytePtr = (unsigned char *)ptr;
    for(size_t i = 0; i < size; i++) {
        printf("%zu: %02X ", i, bytePtr[i]);
        if ((i+1) % 4 == 0) printf("\n");
    }
    printf("\n");
}

int main(int arg, char *argv[]) {
    // Allocate and initialize struct Version1
    struct Version1 v1 = {.c1 = 'A', .i = 0x12345678, .c2 = 'B', .s = 0x1234};
    printf("Version1 Memory Layout (sizeof: %zu):\n", sizeof(v1));
    inspectMemoryLayout(&v1, sizeof(v1));
    printf("\n");

    // Allocate and initialize struct Version2
    struct Version2 v2 = {.c1 = 'A', .c2 = 'B', .i = 0x12345678, .s = 0x1234};
    printf("Version2 Memory Layout (sizeof: %zu):\n", sizeof(v2));
    inspectMemoryLayout(&v2, sizeof(v2));
    printf("\n");

    // Allocate and initialize struct Version3
    struct Version3 v3 = {.i = 0x12345678, .s = 0x1234, .c1 = 'A', .c2 = 'B'};
    printf("Version3 Memory Layout (sizeof: %zu):\n", sizeof(v3));
    inspectMemoryLayout(&v3, sizeof(v3));
    printf("\n");

    return 0;
}
