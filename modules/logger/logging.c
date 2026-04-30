// modules/logger/logging.c
#include "logging.h"
#include <stdarg.h>
#include <stdio.h>

void log_dispatch_bin(uintptr_t addr, int n_args, ...) {
    // Format simple : LEVEL:ADDR:NARGS:ARG1:ARG2...
    printf("%d:0x%lx:%d", 0, addr, n_args);
    
    va_list args;
    va_start(args, n_args);
    for (int i = 0; i < n_args; i++) {
        printf(":%d", va_arg(args, int32_t));
    }
    va_end(args);
    printf("\n");
    fflush(stdout); // Important pour le pipe Python
}