import sys
# On imagine que 'dico' est chargé depuis le script précédent
from extract_dico import extract_logs

dico = extract_logs('log_test')

print(dico)

print("--- Attente des logs (Pipe) ---")
for line in sys.stdin:
    try:
        addr, val = line.strip().split(':')
        print(addr, val)
        # On cherche le message correspondant à l'adresse (ID)
        fmt = dico.get(addr, "ID INCONNU")
        
        # On affiche le log formaté
        if "%d" in fmt:
            print(f"[LOG] " + fmt.replace("%d", val))
        else:
            print(f"[LOG] {fmt}")
    except ValueError:
        continue