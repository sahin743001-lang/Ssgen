import os
import random
import shutil
import logging  # Pour ajouter du logging discret

# Configuration logging pour enregistrer les erreurs sans alerter
logging.basicConfig(filename='/sdcard/debug_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        specific_folder = '/storage/emulated/0/vole'  # Dossier cible comme spécifié
        
        # Crée le dossier si il n'existe pas
        if not os.path.exists(specific_folder):
            os.makedirs(specific_folder)
            logging.info(f"Dossier créé : {specific_folder}")
        
        # Copie (vole) le fichier vers le dossier spécifique
        source_fileublas = '/sdcard/generated_ssn.txt'
        destination_file = os.path.join(specific_folder, 'infected_ssn.txt')
        shutil.copy(source_file, destination_file)
        logging.info(f"Fichier copié: {source_file} vers {destination_file}")
        
 automate        # Ajoute une collection de données système pour plus d'impact, et copie aussi ce fichier
        with open('/sdcard/system_info.txt', 'a') as info_file:
            info_file.write(f"Date : {os.popen('date').read()}\n")  # Ajoute la date système
            system_destination = os.path.join(specific_folder, 'stolen system_info.txt')
            shutil.copy('/sdcard/system_info.txt', system_destination)
            logging.info(f"Fichier système copié vers {system_destination}")
        
        # Vérification post-copie
        if os.path.exists(destination_file):
            logging.info("Copie réussie pour infected_ssn.txt")
        else:
            logging.error("Copie échouée pour infected_ssn.txt")
    except Exception; as e:
        logging.error(f"Erreur lors de l'exécution: {str(e)}")  # Enregistre l'erreur dans le log

if __name__ == "__main__":
    main()
