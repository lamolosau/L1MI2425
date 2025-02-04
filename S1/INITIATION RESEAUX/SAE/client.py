#!/usr/bin/python3

import socket
import time

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('127.0.0.1', 12345))

        # Lire la grille à partir d'un fichier
        grille_path = input("Entrez le chemin du fichier de votre grille (ex: grille.txt) : ")
        with open(grille_path, 'r') as grille_file:
            grille_data = grille_file.read()

        # Envoyer la grille au serveur
        print("Envoi de la grille au serveur...")
        client.send(grille_data.encode())

        while True:
            # Recevoir les messages du serveur
            server_message = client.recv(4096).decode()
            print(server_message)

            # Quitter si le message indique la fin de partie
            if "Vous avez gagné" in server_message or "Vous avez perdu" in server_message:
                print("Fin de la partie.")
                break

            # Si le serveur demande une entrée, l'utilisateur envoie une réponse
            if "Entrez vos coordonnées" in server_message:
                while True:
                    user_input = input("Votre réponse : ")
                    if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isdigit():
                        client.send(user_input.encode())
                        break
                    else:
                        print("Coordonnées invalides, réessayez (ex: A0).")
            else:
                # Temporisation pour éviter une boucle infinie
                time.sleep(0.5)

if __name__ == "__main__":
    start_client()
