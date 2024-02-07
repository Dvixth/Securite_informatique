import socket


def padding_oracleserver(chaine):  # Fonction du serveur Oracle qui renvoie True si le Padding et correct sinon Faux
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("51.195.253.124", 11111)) #connection au serveur
            s.sendall(chaine.encode())  #envoie de la chaine de caractère
            data = s.recv(1024).decode().strip() #réception de la réponse
            if data == "Successfully decrypted.":
                return True
            else:
                return False
    except Exception as e:
        print("Erreur :", type(e), e)


def padding_oracle_attack(kbloc,cbloc): 
    #Fonction qui Itère les ocetets et trouve le bon octets qui donne un bon padding et qui fais l'itération des autres ocetes relativement au autres
    K = bytearray.fromhex(kbloc)
    S = []
    for i in range(len(K) - 1, -1, -1):
        for j in range(15,i,-1):
            K[j] = (S[15 - j] ^ (16 - i))
            print(K[j])
        for X in range(256):
            K[i] = X
            bloc = K.hex() + cbloc
            print(bloc)
            response_server = padding_oracleserver(bloc)
            print(response_server)
            if response_server:
                print(i)
                print(X)
                S.append(X ^ (16-i))
                print(S)
                break
    return S  # Retourne la liste des valeurs S2 trouvées

def xor_bytes(a, b): #Fonction qui fais le XOR pour déchiffré les Bloc
    return bytes(x ^ y for x, y in zip(a, b))

K = "00000000000000000000000000000000" # La valeur K qu'on ajoute a C2 et C2
C2 ="d5a2d9101d0abc1c371152d49b04a7a4" # C2 dernier bloc chiffré
C1="fb484eaaa0adcb76c712ee85d26913e2" # C1 premier bloc chiffré
IV="d034423685a080a3521c6c7509dbeaeb"

S2 = padding_oracle_attack(K, C2)
S1 = padding_oracle_attack(K, C1)

#Inverser les S2 et S1
S2_inverse=S2[::-1]
S1_inverse=S1[::-1]

# Convertir S1 et S2 en tableaux d'octets
S1_bytes = bytes(S1_inverse)
S2_bytes = bytes(S2_inverse)

# Convertir IV et C1 en tableaux d'octets
IV_bytes = bytes.fromhex(IV)
C1_bytes = bytes.fromhex(C1)

# XOR pour obtenir P1 et P2
P1 = xor_bytes(S1_bytes, IV_bytes)
P2 = xor_bytes(S2_bytes, C1_bytes)

# Décoder P1 et P2 en texte
plaintext1 = P1.decode('utf-8')
plaintext2 = P2.decode('utf-8')

print("P1 (déchiffré) :", plaintext1)
print("P2 (déchiffré) :", plaintext2)

# Combinez P1 et P2 pour obtenir le message complet
message = plaintext1 + plaintext2
print("Message déchiffré complet :", message)

