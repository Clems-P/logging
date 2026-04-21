#include <stdio.h>
#include <stdint.h>
#include <string.h>


// Ma fonction de "dispatch" (simule l'envoi UART ou le stockage Flash)
void log_dispatch_bin(uint32_t id, int32_t val) {
    printf("[BIN_LOG] ID: 0x%08X | Arg: %d\n", id, val);
    printf("0x%x:%d\n", id, val);
}



#define LOG_ERR(msg, val) \
    do { \
        _Static_assert(__builtin_constant_p(msg), "ERREUR : msg doit être une constante littérale !"); \
        static const char __l_str[] __attribute__((section(".log_strings"))) = msg; \
        log_dispatch_bin((uintptr_t)__l_str, val); \
    } while(0)
