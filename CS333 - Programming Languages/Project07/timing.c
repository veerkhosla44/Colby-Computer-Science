#include <time.h>

// Return the time in seconds
double get_time_sec() {
    return (double)clock() / CLOCKS_PER_SEC;
}