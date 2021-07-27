#!/usr/bin/env python3
#Importer les modules socket et threading
import socket
import threading

#variable initialisé (liste dynamic)
threadsClients = []

#definition de la fonction recuperation des infos clients
def instanceServeur(client, infosClient):
    adresseIP = infosClient[0]
    port = str(infosClient[1])
    print("Instance de serveur prêt pour " + adresseIP + ":" + port)
    message = ""
    while message.upper() != "FIN":#msg au client pour terminer la connexion
        message = client.recv(255).decode("utf-8")#nbre des données envoyés
        print("Message reçu du client " + adresseIP + ":" + port + " : " + message)#afficher les infos recupérées
        client.send("Message reçu".encode("utf-8"))#envoi du msg au client
    print("Connexion fermée avec " + adresseIP + ":" + port)#msg de fin connexion
    client.close()

def envoyer(message):
    message = message.encode()
    connexion_avec_client.send(message)

def recevoir():
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu=msg_recu.decode()
    return msg_recu

def dialogue():
    while 1:
        msg_recu = recevoir()
        print(msg_recu)
        message = input("Entrez votre message: ")
        print(message)
        envoyer(message)
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('127.0.0.1', 50000))  # Écoute sur le port 50000
serveur.listen(5)#nobre de connexion simultané
while True:#si vrai on entre dans la boucle
    client, infosClient = serveur.accept()#le serveur accepte la connexion du client
    threadsClients.append(threading.Thread(None, instanceServeur, None, (client, infosClient), {}))
    threadsClients[-1].start()
serveur.close()
