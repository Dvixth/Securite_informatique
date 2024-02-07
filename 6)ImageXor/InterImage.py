# Ouvrez et lisez les deux fichiers image en tant que fichiers binaires
with open('fichier_dechiffre_simple.jpg', 'rb') as file1, open('encrypted_file_hard.jpg', 'rb') as file2:
    # Lisez les données binaires des deux fichiers
    data1 = file1.read()
    data2 = file2.read()

    result_data = bytes(x ^ y for x, y in zip(data1, data2))

        # Enregistrez le résultat dans un nouveau fichier image
    with open('result.jpg', 'wb') as result_file:
            result_file.write(result_data)

    print("L'opération XOR a été effectuée et le résultat a été enregistré dans 'result.jpg'.")
