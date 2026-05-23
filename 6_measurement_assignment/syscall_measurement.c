#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

int main()
{
    struct timeval tv;
    // struct timezone tz;

    gettimeofday(&tv, NULL);
    unsigned long long initial = tv.tv_sec*1000000 + tv.tv_usec;

    unsigned long long temp = 100000;

    read(0, NULL, 0);

    gettimeofday(&tv, NULL);
    unsigned long long final = tv.tv_sec*1000000 + tv.tv_usec;
    printf("%llu, %llu \n", initial, final);
    unsigned long long time = (final - initial);
    printf("%llu microseconds\n", time);
    return (0);
}