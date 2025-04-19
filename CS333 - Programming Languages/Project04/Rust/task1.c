/**
 * Given an array of random integers, sort it in such a way that the even 
 * numbers appear first and the odd numbers appear later. The even numbers 
 * should be sorted in descending order and the odd numbers should be sorted 
 * in ascending order.
 *
 * Veer Khosla
 * 3/27/24
 */

#include <stdio.h>
#include <stdlib.h>

/* Comparator function to arrange even numbers first in descending order,
   followed by odd numbers in ascending order */
int comparator(const void *p, const void *q) {
	int a = *(const int*)p;
    int b = *(const int*)q;

    if (a % 2 == 0 && b % 2 == 0) { // Both even
        return b - a; // Sort in descending order
    } else if (a % 2 == 0) { // only first element is even
        return -1; // first_element should come first
    } else if (b % 2 == 0) { // only second element is even
        return 1; // second_element should come first
    } else { // Both odd
        return a - b; // Sort in ascending order
    }
}

int main(int argc, char **argv) {
    int ary[] = {10, 11, 1, 8, 9, 0, 13, 4, 2, 7, 6, 3, 5, 12};
    
    int size = sizeof(ary) / sizeof(int);
    
    qsort((void *)ary, size, sizeof(int), comparator);
    
    printf("The sorted array is: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", ary[i]);
    }
    printf("\n");
    
    return 0;
}