import hashlib #bibliothèque de hachage incluse dans python 
from tqdm import tqdm #barre de progression pour faire beau ! 

# Le haché MD5
passwordhach = "5a74dd4eef347734c8a0a9a3188abd11"

# Ouvrir le fichier rockyou.txt en mode lecture
#utilisation de l'encodage utf-8 pour lire le fichier
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as password_file: 
    try : 
        for line in tqdm(password_file, unit='word'):
            password = line.strip()  # Retirer les espaces et sauts de ligne
            md5_hash = hashlib.md5(password.encode()).hexdigest() # résumé de la concaténation des données et hachage de toutes le contenue de rockyou.txt

            if md5_hash == passwordhach: #si un hachage est égale au hachage donné alors on arrete 
                print(f"Mot de passe trouvé : {password}")
                break 
    except Exception as e: 
        print("mot de passe non trouvé")