# Ouvrez le fichier de l'image chiffrée en mode binaire
with open('encrypted_file_hard.jpg', 'rb') as encrypted_image_file:
    encrypted_data = bytearray(encrypted_image_file.read())

# Définissez la clé XOR en format hexadécimal (doit être répétée pour avoir la même longueur que l'image)
key_hex = "0x840c491a988252ba1f942415c4cb0f04"  # Changez cette clé par la clé réelle en format hexadécimal

# Convertissez la clé hexadécimale en octets
key = bytes.fromhex(key_hex[2:])  # [2:] pour ignorer le "0x" au début de la chaîne hexadécimale

# Répétez la clé pour qu'elle ait la même longueur que les données de l'image chiffrée
while len(key) < len(encrypted_data):
    key += key

# Appliquer la clé XOR pour déchiffrer les données
decrypted_data = bytes([a ^ b for a, b in zip(encrypted_data, key)])

# Enregistrez les données déchiffrées dans un nouveau fichier
with open('image_dechiffree.jpg', 'wb') as decrypted_image_file:
    decrypted_image_file.write(decrypted_data)

print("L'image a été déchiffrée avec succès et enregistrée sous image_dechiffree.jpg.")