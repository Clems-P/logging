from elftools.elf.elffile import ELFFile

def extract_logs(elf_path):
    with open(elf_path, 'rb') as f:
        elf = ELFFile(f)
        section = elf.get_section_by_name('.log_strings')
        if not section: return {}

        data = section.data()
        base_addr = section['sh_addr']
        dictionary = {}
        
        i = 0
        while i < len(data):
            # On cherche le premier octet non nul (début d'une chaîne)
            if data[i] != 0:
                addr = base_addr + i
                # On extrait la chaîne jusqu'au prochain \0
                end = data.find(b'\x00', i)
                if end == -1: end = len(data)
                
                msg = data[i:end].decode('utf-8', errors='ignore')
                dictionary[hex(addr)] = msg
                
                # On saute à la fin de cette chaîne
                i = end
            else:
                # C'est un octet de padding (\0), on passe au suivant
                i += 1
        return dictionary

if __name__ == "__main__":
    dico = extract_logs('log_test')
    for addr, msg in dico.items():
        print(f"{addr} -> {msg}")