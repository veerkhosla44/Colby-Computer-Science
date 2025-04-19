/**
 * Veer Khosla
 * 03/27/24
 * CS333
 * defines factorial function and allows for command line arguments
 */

#include <stdio.h>
#include <stdlib.h>

// function takes in an integer and returns its factorial value
int factorial(int x){
    if (x == 0) { // Base case
        return 1;
    } else { // Recursive case
        return x * factorial(x-1);
    }
}

int main (int argc, char **argv) {
    // declares and initializes a function pointer to the factorial function 
    int (*calc)(const int) = factorial;

    // prints return value of the function factorial
    printf("%d", calc(atoi(argv[1])));
  
    return 0;
}