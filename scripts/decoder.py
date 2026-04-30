import sys
import json
import os

# Configuration des couleurs ANSI
RED    = "\x1b[31m"
YELLOW = "\x1b[33m"
BLUE   = "\x1b[34m"
RESET  = "\x1b[0m"
BOLD   = "\x1b[1m"

def run_decoder(json_path):
    # 1. Chargement du dictionnaire
    if not os.path.exists(json_path):
        print(f"Erreur : Le fichier {json_path} est introuvable.")
        print("Avez-vous compilé le projet avec CMake ?")
        sys.exit(1)

    with open(json_path, 'r') as f:
        dico = json.load(f)

    print(f"{BLUE}--- Décodeur prêt ({len(dico)} messages chargés) ---{RESET}")
    print(f"{BLUE}--- Attente des logs sur stdin... ---{RESET}")

    # 2. Lecture des logs en boucle (Pipe)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # Format attendu : LEVEL:ADDR:N_ARGS:ARG1:ARG2...
        parts = line.split(':')
        if len(parts) < 3:
            # Si la ligne ne ressemble pas à un log binaire, on l'affiche brute
            print(f"Brut: {line}")
            continue

        try:
            level  = int(parts[0])
            addr   = parts[1]
            n_args = int(parts[2])
            args   = parts[3:]

            # 3. Récupération du message dans le dico
            fmt = dico.get(addr, f"{RED}ID INCONNU ({addr}){RESET}")

            # 4. Gestion du niveau de log (Couleurs)
            prefix = "[INFO]"
            color = RESET
            if level == 0: # ERROR
                prefix = "[ERR ]"
                color = BOLD + RED
            elif level == 1: # WARNING
                prefix = "[WRN ]"
                color = YELLOW

            # 5. Formatage des arguments
            output = fmt
            for arg in args:
                # On remplace le premier %d trouvé par l'argument suivant
                output = output.replace("%d", str(arg), 1)

            print(f"{color}{prefix} {output}{RESET}")
            sys.stdout.flush() # Force l'affichage immédiat

        except Exception as e:
            print(f"{RED}Erreur décodage ligne '{line}': {e}{RESET}")

if __name__ == "__main__":
    # Par défaut, on cherche dictionary.json dans le dossier courant
    path = sys.argv[1] if len(sys.argv) > 1 else "dictionary.json"
    run_decoder(path)