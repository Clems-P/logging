#include <stdio.h>
#include <stdint.h>
#include <stdarg.h>

// Macros de comptage
#define PP_NARG(...) PP_NARG_HELPER(0, ##__VA_ARGS__, 5, 4, 3, 2, 1, 0)
#define PP_NARG_HELPER(_0, _1, _2, _3, _4, _5, N, ...) N

// Simulation du dispatch binaire
// On passe le nombre d'arguments pour aider le décodeur
void log_dispatch_bin(uintptr_t addr, int n_args, ...) {
    printf("0x%lx:%d", addr, n_args);
    
    va_list args;
    va_start(args, n_args);
    for (int i = 0; i < n_args; i++) {
        // Pour le test on considère que tout est int32_t
        printf(":%d", va_arg(args, int32_t));
    }
    va_end(args);
    printf("\n");
}

#define LOG_ERR(msg, ...) \
    do { \
        /* 1. Vérification du msg (Flash) */ \
        _Static_assert(__builtin_constant_p(msg), "Msg doit être littéral"); \
        \
        /* 2. Bloquer si plus de 2 arguments après le msg */ \
        _Static_assert(PP_NARG(__VA_ARGS__) <= 2, "Trop d'arguments ! Max 2."); \
        \
        /* 3. Stockage en section spécifique */ \
        static const char __l_str[] __attribute__((section(".log_strings"), aligned(1))) = msg; \
        \
        /* 4. Envoi : Adresse + Nb args + les args eux-mêmes */ \
        log_dispatch_bin((uintptr_t)__l_str, PP_NARG(__VA_ARGS__), ##__VA_ARGS__); \
    } while(0)
