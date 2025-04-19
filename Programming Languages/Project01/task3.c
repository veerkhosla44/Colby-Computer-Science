/**
 * Task 3
 *
 * Veer Khosla
 * 2/22/24 
 */

#include <stdio.h>
#include <stdlib.h>

        
/* Allocates memory infinitely (taking up space) unless freeing the allocation
 */ 
int main (int arg, char *argv[]) {
    unsigned char *ptr;

    // loops infinitely, allocating memory each time
    for(int i=0; i>=0; i++) {
	    ptr = (unsigned char *) malloc(sizeof(unsigned char)); 

        // frees memory allocated
        free(ptr);
	}
  return 0;
}  
    