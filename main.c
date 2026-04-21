#include "logging.h"

int main() {
    int a = 10, b = 20, c = 30;

    LOG_ERR("Zero arg");                 // OK
    LOG_ERR("Un arg: %d", a);            // OK
    LOG_ERR("Deux args: %d %d", a, b);   // OK

    // LOG_ERR("Trois args", 1, 2, 3); // <--- ERROR: Static assert failed!
    
    return 0;
}