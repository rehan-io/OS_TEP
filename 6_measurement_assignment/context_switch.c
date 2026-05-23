#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int main(){
    cpu_set_t set;
    CPU_ZERO(&set);
    CPU_SET(0, &set);

    pid_t child = fork();

    if (child < 0)
    {
        fprintf(stderr, "fork for child failed\n");
        exit(1);
    }
    return 0;
}