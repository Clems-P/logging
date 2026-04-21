import sys
# On imagine que 'dico' est chargé depuis le script précédent
from extract_dico import extract_logs

dico = extract_logs('log_test')

print(dico)

print("--- Attente des logs (Pipe) ---")

for line in sys.stdin:
    parts = line.strip().split(':')
    if len(parts) < 2: continue

    addr = parts[0]
    n_args = int(parts[1])
    args = parts[2:] # Récupère le reste des arguments

    fmt = dico.get(addr, "ID INCONNU")
    
    # Remplacement simple des %d par les valeurs reçues
    try:
        output = fmt
        for arg in args:
            output = output.replace("%d", arg, 1)
        print(f"[\x1b[31mLOG\x1b[0m] {output}")
    except Exception as e:
        print(f"Erreur décodage: {e}")
