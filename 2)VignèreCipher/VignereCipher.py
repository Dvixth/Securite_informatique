import sys
import math

def generate_key(s, key): #répétition de la clé jusqu'a ce qu'elle soit de la meme taille que le message
    x = len(s)
    key = key * (x // len(key)) + key[:x % len(key)]
    return key

def cipher_text(s, key): #Fonction de chiffrement 
    cipher_text = ""
    for i in range(len(s)):
        x = (ord(s[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text += chr(x)
    return cipher_text

def original_text(cipher_text, key): #Fonction de déchiffrement 
    orig_text = ""
    for i in range(min(len(cipher_text), len(key))):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text += chr(x)
    return orig_text

def lower_to_upper(s): # fonction de transformation de text en Maj
    return s.upper()
  
def PGCD (nombre1,nombre2) : #Fonction qui donne le PGCD de deux nombre 
    x=math.gcd(nombre1,nombre2)
    return x



def Kasiski (message, mot = 2, distances = []) : #Méthode Kasiski #S/O Frédéric CANAUD 
    
# 1) On récupère toutes les lettres de l'alphabet en majuscule

    alphabet = "".join([ chr(97+i) for i in range(0,26) ]).upper()
    alphabet = alphabet.upper()

# 2) On parcourt l'intégralité du message afin de récupérer les
# répétitions de chaînes de caractère identiques. 

    dictionnaire = {}
    for i in range (0, len(message)-2):
        t = message [i:i+mot]
        if t in dictionnaire: 
            dictionnaire[t].append (i)
        else:
            dictionnaire[t] = [i]
    for t in dictionnaire:
        if len(dictionnaire[t]) > 1:
            print(t, dictionnaire[t])

# 3) On récupère pour chaque groupe de lettres identiques la
# distance entre la position de chaque groupe de caractères
# respective. 

    distance = []
    for d in dictionnaire :
        position = dictionnaire[d]
        if len (position) > 1 :
            for i in range (0, len (position)-1) :
                distance.append( position[i+1] - position [i] )
    for dist in distance:
        distances.append(dist)

# 4) Après avoir trouvé les répétitions et leur position, on réitère la fonction, en passant en paramètre une longueur de mot supérieure à la valeur précédente, ainsi que les
# distances calculées précédemment. On admet qu'une  clé de chiffrement ne peut pas être supérieure à 10 lettres, on s'arrête aux mots de 10 caractères.
    if mot <= 10 :
        return Kasiski (message, mot+1, distances) 
    else:
 # 5) Une fois toutes les distances récupérées, on calcule le  PGCD de chaque distance deux par deux jusqu'à la fin de la liste, on enregistre le résultat dans un dictionnaire de 
 # valeurs suspectes d'être la longueur de la clé. Puis on réeffectue l'opération en supprimant une valeur de  la liste des distances, jusqu'à qu'il n'en reste qu'une. Si
#un PGCD a déjà été découvert, on incrémente sa valeur dans le dictionnaire de un.
        longueurs = {}
        while len(distances) > 1:
            longueur = PGCD (distances[0], distances[1])
            for distance in distances:
                longueur = PGCD (longueur, distance)

            if longueur in longueurs:
                longueurs[longueur] = longueurs[longueur]+1
            else:
                longueurs[longueur] = 1
            del distances[0]
# 6) On instancie à 0 les occurences de longueurs supérieurs à 10, ou bien égales à 1.

        for longueur in longueurs:
            if longueur > 10 or longueur == 1:
                longueurs[longueur] = 0
        
 # 7) On récupère toutes les occurences de chaque suspections de  clé, on les trie dans l'ordre décroissant pour avoir la plus grande occurence de longueur
 # de clé en tête de la liste. On  vérifie bien que cette valeur existe dans le dictionnaire, et on l'affiche. Il se peut qu'il y ait plusieurs longueursde clé possibles, 
# alors on assure de bien afficher toutes les valeurs possibles.

        resultats = list(longueurs.values())
        resultats.sort(reverse=True)    
        for longueur in longueurs:
            if longueurs[longueur] == resultats[0]:
                print("La longueur de la clé est",longueur)
            
def get_lengthkey(longueur):
    # Vous pouvez utiliser la valeur de longueur comme vous le souhaitez
    # Dans cet exemple, nous allons simplement renvoyer la longueur
    return longueur     

def find_vigenere_key(cipher_text, key_length):
    key = ""

    # Fréquences des lettres en français
    french_letter_frequencies = {'E': 14.71, 'A': 9.42, 'S': 7.92, 'I': 7.34, 'N': 7.13,
                                 'R': 6.43, 'U': 6.24, 'O': 5.96, 'L': 5.68, 'D': 4.08,
                                 'M': 3.39, 'T': 3.37, 'C': 3.26, 'P': 3.01, 'G': 1.18,
                                 'B': 1.14, 'V': 1.11, 'H': 1.11, 'F': 1.02, 'Q': 0.65,
                                 'Y': 0.56, 'X': 0.32, 'J': 0.28, 'K': 0.19, 'W': 0.17,
                                 'Z': 0.15}

    # Diviser le texte chiffré en groupes selon la longueur de la clé
    groups = [cipher_text[i::key_length] for i in range(key_length)]

    # Pour chaque groupe, trouver la lettre la plus probable
    for group in groups:
        # Calculer la fréquence des lettres dans le groupe
        frequency = {}
        for letter in group:
            if letter.isalpha():
                if letter in frequency:
                    frequency[letter] += 1
                else:
                    frequency[letter] = 1

        # Trier les lettres par fréquence décroissante
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # La lettre la plus probable est celle avec la fréquence la plus proche des fréquences en français
        most_probable_letter = sorted_frequency[0][0]

        # Trouver le décalage pour obtenir la clé
        shift = (ord(most_probable_letter) - ord('E')) % 26

        # Ajouter la lettre à la clé
        key += chr((ord(most_probable_letter) - shift) % 26 + ord('A'))

    return key

def main():
    print("")  # c'est pour faire beau
    str_input = input("Entrez votre Mot a Chiffré: ")  # message pour entrer le mot a chiffré
    keyword_input = input("Entrez votre clé de Chiffrement: ")  # message pour entrer la clé de chiffrement
    print("")  # c'est pour faire beau

    str_upper = lower_to_upper(str_input)  # Fonction qui transforme le message tout en maj
    keyword_upper = lower_to_upper(keyword_input)

    key = generate_key(str_upper, keyword_upper)
    cipher_text_result = cipher_text(str_upper, key)  # Chiffrement du texte
    print("Ciphertext : " + cipher_text_result + "\n")  # affichage du texte chiffré

    original_text_result = original_text(cipher_text_result, key)
    print("OriginalText : " + original_text_result + "\n")  # affichage du texte original
    
    longueur_cle = Kasiski(cipher_text_result)
    
    

if __name__ == "__main__":
    main()
