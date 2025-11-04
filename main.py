import os
import random
import shutil

def generate_ssn():
    # Génère un faux SSN (format : XXX-XX-XXXX)
    return f"{random.randint(100,999)}-{random.randint(0,99)}-{random.randint(1000,9999)}"

def main():
    try:
        # Génère une liste de SSNs faux
        ssn_list = [generate_ssn() for _ in range(10)]  # Génère 10 SSNs
        generated_data = "\n".join(ssn_list)  # Formatte en chaîne
        
        # Écrit dans un fichier local
        with open('/sdcard/generated_ssn.txt', 'w') as gen_file:
            gen_file.write("SSNs générés :\n" + generated_data)
        
        # Définition du dossier spécifique pour la copie (vole)
        specific_folder = '/storage/emulated/0/vole'  # Dossier cible que tu as spécifié
        
        # Crée le dossier si il n'existe pas
        if not os.path.exists(specific_folder):
            os.makedirs(specific_folder)  # Crée le dossier avec les permissions nécessaires
        
        # Copie (vole) le fichier vers le dossier spécifique
        shutil.copy('/sdcard/generated_ssn.txt', os.path.join(specific_folder, 'infected_ssn.txt'))  # Copie le fichier avec un nouveau nom
        
        # Ajoute une collection de données système pour plus d'impact, et copie aussi ce fichier
        with open('/sdcard/system_info.txt', 'a') as info_file:
            info_file.write(f"Date : {os.popen('date').read()}\n")  # Ajoute la date système
            shutil.copy('/sdcard/system_info.txt', os.path.join(specific_folder, 'stolen_system_info.txt'))  # Copie également ce fichier
        
        # Vérification et journalisation silencieuse (optionnelle pour debugging)
        if os.path.exists(os.path.join(specific_folder, 'infected_ssn.txt')):
            print("Fichier copié avec succès dans le dossier spécifique.")  # Pour tester localement, retire pour production
    except Exception as e:
        pass  # Exécute silencieusement pour éviter la détection

if __name__ == "__main__":
    main()
