#include "logging.h"

int main() {
    int capteur = 42;
    char buffer_ram[] = "Je suis en RAM";

    // Cas 1 : Ça doit compiler et afficher l'ID
    LOG_ERR("Hello World", 0);
    LOG_ERR("Valeur: %d", capteur);

    // Cas 2 : Décommentez la ligne suivante pour voir l'erreur de compilation
    // LOG_ERR(buffer_ram, 10); 


    return 0;
}