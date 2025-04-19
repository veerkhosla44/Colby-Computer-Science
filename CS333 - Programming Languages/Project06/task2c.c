/*Veer Khosla
CS333
04/09/23
demonstrates handling of SIGSEGV and registers a handler for the SIGSEGV signal that is triggered by attempting to write to a null pointer.
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handle_segfault(int sig) {
    printf("Segmentation fault handled.\n");
    exit(EXIT_FAILURE);
}

int main() {
    signal(SIGSEGV, handle_segfault); // Register the handler
    int *ptr = NULL; // NULL pointer
    *ptr = 42; // Accessing illegal memory which causes segmentation fault
    return 0;
}
