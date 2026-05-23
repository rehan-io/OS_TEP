// a more precise measure

#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
    struct timespec ts;
    int iterations = 1000000;
    
    clock_gettime(CLOCK_MONOTONIC, &ts);
    unsigned long long before = ts.tv_sec * 1000000000ULL + ts.tv_nsec;
    
    for (int i = 0; i < iterations; i++) {
        read(0, NULL, 0);
    }
    
    clock_gettime(CLOCK_MONOTONIC, &ts);
    unsigned long long after = ts.tv_sec * 1000000000ULL + ts.tv_nsec;
    
    printf("Average time per null read: %llu nanoseconds\n", 
           (after - before) / iterations);
    
    return 0;
}