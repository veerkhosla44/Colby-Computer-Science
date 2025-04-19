/*Veer Khosla
CS333
04/09/23
Program demonstrates a SIGINT singal and makes a signal handler that catches the Ctrl+C interrupt signal.
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handle_interrupt(int sig) {
    printf("Interrupted!\n");
    exit(EXIT_SUCCESS); // Exit cleanly
}

int main() {
    signal(SIGINT, handle_interrupt); // Register the handler
    printf("Program started. Press Ctrl+C to interrupt.\n");
    while(1); // Infinite loop
    return 0;
}