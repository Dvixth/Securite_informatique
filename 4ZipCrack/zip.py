import zipfile

# Chemin vers le fichier ZIP
fichier_zip = 'archive.zip'

# Chemin vers le fichier texte contenant les mots de passe à tester
fichier_mots_de_passe = 'zip_password.txt'

# Ouvrir le fichier ZIP
with zipfile.ZipFile(fichier_zip, 'r') as zip_file:
    # Lire la liste des mots de passe depuis le fichier texte
    with open(fichier_mots_de_passe, 'r') as passwords_file:
        for line in passwords_file:
            password = line.strip()
            try:
                # Essayer de décompresser le fichier ZIP avec le mot de passe actuel
                zip_file.extractall(pwd=password.encode())
                print(f"Mot de passe trouvé : {password}")
                break
            except Exception as e:
                pass

print("Fin de l'attaque par force brute.")