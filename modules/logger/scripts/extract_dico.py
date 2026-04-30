# modules/logger/scripts/extract_dico.py
import sys
import json
from elftools.elf.elffile import ELFFile

def run(elf_path, output_json):
    with open(elf_path, 'rb') as f:
        elf = ELFFile(f)
        section = elf.get_section_by_name('.log_strings')
        if not section: return
        
        data = section.data()
        base_addr = section['sh_addr']
        dico = {}
        
        i = 0
        while i < len(data):
            if data[i] != 0:
                addr = hex(base_addr + i)
                end = data.find(b'\x00', i)
                msg = data[i:end].decode('utf-8')
                dico[addr] = msg
                i = end
            else: i += 1
            
        with open(output_json, 'w') as f_out:
            json.dump(dico, f_out, indent=4)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])