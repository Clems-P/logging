#include <stdio.h>
#include <stdint.h>
#include <stdarg.h>

// Macros de comptage
#define PP_NARG(...) PP_NARG_HELPER(0, ##__VA_ARGS__, 5, 4, 3, 2, 1, 0)
#define PP_NARG_HELPER(_0, _1, _2, _3, _4, _5, N, ...) N

#define LOG_ERR(msg, ...) \
    do { \
        /* 1. Vérification du msg (Flash) */ \
        _Static_assert(__builtin_constant_p(msg), "Msg doit être littéral"); \
        \
        /* 2. Bloquer si plus de 2 arguments après le msg */ \
        _Static_assert(PP_NARG(__VA_ARGS__) <= 2, "Trop d'arguments ! Max 2."); \
        \
        /* 3. Stockage en section spécifique */ \
        static const char __l_str[] __attribute__((section(".log_strings"), used, retain, aligned(1))) = msg; \
        \
        /* 4. Envoi : Adresse + Nb args + les args eux-mêmes */ \
        log_dispatch_bin((uintptr_t)__l_str, PP_NARG(__VA_ARGS__), ##__VA_ARGS__); \
    } while(0)

extern void log_dispatch_bin(uintptr_t addr, int n_args, ...);