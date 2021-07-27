#!/usr/bin/env python3
import socket

adresseIP = "127.0.0.1"  # Ici, le poste local
port = 50000  # Se connecter sur le port 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))  # le client se connecte avec ip et port
print("Connecté au serveur")  # si connecter on affiche ce msg
print("Tapez FIN pour terminer la conversation. ")  # on afficher ce msg pour terminer on tappe FIN
message = ""
while message.upper() != "FIN":
    message = input("Entrez votre message > ")
    client.send(message.encode("utf-8"))
    reponse = client.recv(255)
    print(reponse.decode("utf-8"))
print("Connexion fermée")
client.close()
