/**
 * Print out first 100 bytes of stack
 *
 * Veer Khosla
 * 2/22/24
 */

#include <stdio.h>
#include <stdlib.h>
        
/* 
 */ 
int main (int arg, char *argv[]) {
    int a = 12;
    float b = 158.3;
    char c = 'Z';
    unsigned char *ptr;

    // Pointing ptr to its own address
    ptr = (unsigned char *)&ptr;

    // Print out the first 100 bytes of memory from ptr onwards
    for(int i = 0; i < 100; i++) {
        printf("%d: %02X\n", i, ptr[i]);
    }	

  return 0;
}  