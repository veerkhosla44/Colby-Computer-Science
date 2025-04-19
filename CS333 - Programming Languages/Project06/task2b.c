/*Veer Khosla
CS333
04/09/23
demonstrates handling of SIGFPE and registers a handler for the SIGFPE signal that is triggered by a floating point division by zero.
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handle_fpe(int sig) {
    printf("Floating point exception occurred.\n");
    // Resetting the signal handler to default action
    signal(sig, SIG_DFL); 
    printf("Continuing execution...\n");
}

int main() {
    signal(SIGFPE, handle_fpe); // Register the handler
    float a = 10.0, b = 0.0;
    float c = a / b; // This will generate a floating point exception
    printf("Result: %f\n", c);
    while(1); // Continue program execution
    return 0;
}
