import os
import random
import string

def generate_ssn():
    # Génère un faux SSN (format : XXX-XX-XXXX)
    return f"{random.randint(100,999)}-{random.randint(00,99)}-{random.randint(1000,9999)}"

def main():
    try:
        # Génère une liste de SSNs faux
        ssn_list = [generate_ssn() for _ in range(10)]  # Génère 10 SSNs
        generated_data = "\n".join(ssn_list)  # Formatte en chaîne
        
        # Écrit dans un fichier local
        with open('/sdcard/generated_ssn.txt', 'w') as gen_file:
            gen_file.write("SSNs générés :\n" + generated_data)
        
        # Propagation : Copie le fichier dans un autre répertoire pour se propager
        os.system('cp /sdcard/generated_ssn.txt /sdcard/../Documents/infected_ssn.txt')
        
        # Ajoute une collection de données système pour plus d'impact
        with open('/sdcard/system_info.txt', 'a') as info_file:
            info_file.write(f"Date : {os.popen('date').read()}\n")  # Ajoute la date système
    except Exception as e:
        pass  # Exécute silencieusement

if __name__ == "__main__":
    main()
