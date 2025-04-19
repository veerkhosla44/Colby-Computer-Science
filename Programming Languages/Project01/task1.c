/**
 * Assign value to each type and locate in memory
 *
 * Veer Khosla
 * 2/22/24
 */

#include <stdio.h>
#include <stdlib.h>
        
/* Find locations of variable data in memory
 */ 
int main (int arg, char *argv[]) {
    char c = 'A';    
    short s = 0x1234;
    int i = 0x01234567;
    long l = 123456789;
    float f = 123.456;
    double d = 123.456789;
                        
    unsigned char *ptr;

    // Inspect char
    ptr = (unsigned char *)&c;
    printf("char: ");
    for(int i = 0; i < sizeof(char); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    // Inspect short
    ptr = (unsigned char *)&s;
    printf("short: ");
    for(int i = 0; i < sizeof(short); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    // Inspect int
    ptr = (unsigned char *)&i;
    printf("int: ");
    for(int i = 0; i < sizeof(int); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    // Inspect long
    ptr = (unsigned char *)&l;
    printf("long: ");
    for(int i = 0; i < sizeof(long); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    // Inspect float
    ptr = (unsigned char *)&f;
    printf("float: ");
    for(int i = 0; i < sizeof(float); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    // Inspect double
    ptr = (unsigned char *)&d;
    printf("double: ");
    for(int i = 0; i < sizeof(double); i++) {
        printf("%02X ", ptr[i]);
    }
    printf("\n");

    return 0;
}  