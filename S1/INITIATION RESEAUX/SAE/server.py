#!/usr/bin/python3

import socket
import threading
from bataille_navale import mkGridFromString, checkGrid, mkPlayer, shootAt, playerStr, parseCoord, boatSizes

players = {}  # Stocke les joueurs et leurs données
turn = 0      # Indique le joueur dont c'est le tour (0 ou 1)
player_count = 0  # Nombre de joueurs connectés
lock = threading.Lock()  # Empêche les accès concurrents


def listen_client(client, client_id):
    """
    Gère un client particulier.
    """
    global turn, player_count

    try:
        # Recevoir la grille du joueur
        client.send("Envoyez votre grille de bataille navale (format grille.txt) :\n".encode())
        grid_data = client.recv(4096).decode()

        # Si le client envoie une grille vide ou invalide
        if not grid_data.strip():
            client.send("Grille vide. Déconnexion.\n".encode())
            raise ValueError("Grille vide reçue")

        grid = mkGridFromString(grid_data)

        if not checkGrid(grid):
            client.send("Grille invalide. Déconnexion.\n".encode())
            raise ValueError("Grille invalide reçue")

        # Initialiser le joueur avec la structure complète
        with lock:
            players[client_id] = {
                "grid": grid,
                "history": [["?" for _ in range(10)] for _ in range(10)],
                "nboat": len(boatSizes),  # Nombre de bateaux restants
                "boat": boatSizes.copy(),  # État des bateaux
                "socket": client  # Associer le socket du joueur
            }
            player_count += 1
            client.send("Grille acceptée. En attente du deuxième joueur...\n".encode())

        # Attendre le deuxième joueur
        while player_count < 2:
            pass

        client.send("Début de la partie !\n".encode())

        already_informed = False  # Suivi pour éviter les répétitions
        # Boucle principale du jeu
        while True:
            if turn == client_id:
                already_informed = False  # Réinitialiser pour le prochain tour
                client.send(playerStr(players[client_id]).encode())
                client.send("C'est votre tour. Entrez vos coordonnées de tir (ex: A0) :\n".encode())
                coord = client.recv(1024).decode()

                try:
                    (x, y) = parseCoord(coord.strip())
                    result = shootAt(players[client_id], players[1 - client_id], (x, y))

                    if result == 0:
                        client.send("Raté !\n".encode())
                    elif result == 1:
                        client.send("Touché !\n".encode())
                    elif result == 2:
                        client.send("Coulé !\n".encode())

                    # Vérifiez si l'adversaire a perdu
                    if players[1 - client_id]["nboat"] == 0:
                        client.send("Vous avez gagné !\n".encode())
                        players[1 - client_id]["socket"].send("Vous avez perdu !\n".encode())  # Informer l'adversaire
                        break  # Sortir de la boucle pour terminer la partie

                    # Changer de tour
                    with lock:
                        turn = 1 - client_id
                except ValueError:
                    client.send("Coordonnées invalides. Réessayez.\n".encode())
            else:
                if not already_informed:  # Envoyer le message une seule fois
                    client.send("Ce n'est pas votre tour. Veuillez attendre...\n".encode())
                    already_informed = True
    except Exception as e:
        print(f"Erreur avec le joueur {client_id}: {e}")
    finally:
        print(f"Fermeture de la connexion pour le joueur {client_id}.")
        client.close()


# Initialisation du serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Réutilisation du port
    server.bind(('127.0.0.1', 12345))
    server.listen()
    print("Serveur en attente de connexions...")

    try:
        client_id = 0
        threads = []
        while client_id < 2:  # Limite à 2 joueurs
            client, _ = server.accept()
            print(f"Client {client_id} connecté.")
            thread = threading.Thread(target=listen_client, args=(client, client_id))
            thread.start()
            threads.append(thread)
            client_id += 1

        # Attendez que tous les threads se terminent
        for thread in threads:
            thread.join()

        print("La partie est terminée.")
    except KeyboardInterrupt:
        print("Arrêt du serveur.")
