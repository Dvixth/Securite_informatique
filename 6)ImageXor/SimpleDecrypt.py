def dechiffrer_fichier_xor(fichier_entree, fichier_sortie, cle_xor):
    # Lire le fichier chiffré
    with open(fichier_entree, 'rb') as fichier_chiffre:
        donnees_chiffrees = fichier_chiffre.read()

    # Déchiffrer les données en effectuant un XOR avec la clé
    donnees_dechiffrees = bytes([octet ^ cle_xor for octet in donnees_chiffrees])

    # Enregistrer les données déchiffrées dans le fichier de sortie
    with open(fichier_sortie, 'wb') as fichier_dechiffre:
        fichier_dechiffre.write(donnees_dechiffrees)

def est_jpeg(chemin_fichier):
    try:
        with open(chemin_fichier, 'rb') as f:
            # Vérifier les premiers octets pour voir si le fichier commence par le marqueur JPEG
            return f.read(2) == b'\xFF\xD8'
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    fichier_entree = "encrypted_file_simple.jpg"  # Le nom du fichier chiffré
    fichier_sortie = "fichier_dechiffre_simple.jpg"  # Le nom du fichier de sortie déchiffré

    for cle_xor in range(256):  # Essayer toutes les clés possibles (de 0 à 255)
        dechiffrer_fichier_xor(fichier_entree, fichier_sortie, cle_xor)

        # Vérifier si le fichier déchiffré est un fichier JPEG valide
        if est_jpeg(fichier_sortie):
            print(f"Clé XOR probable : {cle_xor}")
            print(f"Le fichier a été déchiffré avec succès et enregistré sous {fichier_sortie}.")
            break
