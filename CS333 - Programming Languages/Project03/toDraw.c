/**
 * Test code for Stack 
 *
 * Ying Li
 * 08/01/2016
 */

#include "cstk.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    Stack *s = stk_create(20);

    // Printing addresses at Mark 1
    printf("Mark 1: Stack and Heap Memory\n");
    printf("------------------------------\n");
    printf("Stack Pointer (s): %p\n", (void *)s);
    printf("Heap Memory (Stack Data)\n");
    printf("-------------------------------\n");
    printf("Address: %p\n", (void *)s->data);  // Address of the start of the stack data
    printf("Top Pointer: %p\n", (void *)s->top);  // Address of the top pointer
    printf("Capacity: %p\n", (void *)&(s->capacity));  // Address of the capacity variable
    printf("\n");
	
    int i;
    for (i = 0; i < 10; i++) {
        stk_push(s, i + 1);
    }

    int *a = (int *)malloc( sizeof(int)*4 );

    printf( "a is at %p\n", &a );
    printf( "i is at %p\n", &i );
    
    printf( "array starts at %p\n", a );
    for (i = 0; i < 4; i++) {
        a[i] = i*2;


    printf("The original list: ");
    stk_display(s, 0);

    printf("The reversed list: ");
    stk_display(s, 1);

    stk_destroy(s);

    // Printing addresses at Mark 2
    printf("\nMark 2: Stack and Heap Memory After Destruction\n");
    printf("---------------------------------------------\n");
    printf("Stack Pointer (s): %p\n", (void *)s);
    printf("Heap Memory (Stack Data) Freed\n");
    printf("--------------------------------\n");

    return 0;
	}
}