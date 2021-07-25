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
        message = client.recv(255).decode("utf-8")# données recu
        print("Message reçu du client " + adresseIP + ":" + port + " : " + message)#afficher les infos recupérées
        client.send("message reçu".encode("utf-8"))
        #message1 = input(">")
        #client.send(message1.encode("utf-8"))#envoi du msg
    print("Connexion fermée avec " + adresseIP + ":" + port)#msg de fin connexion
    client.close()

#Fonction pour envoyer le msg
def envoyer():
    message = input(">")
    message= client.send(message.encode("utf-8"))
    #message = message.encode("utf-8")
    return message

#Fonction pour recevoir le msg
def recevoir():
    msg_recu = client.recv(1024)
    msg_recu = msg_recu.decode()
    return msg_recu

#fontion dialogue entre le serveur et le client
def dialogue():
    while 1:
        msg_recu = recevoir()
        print(msg_recu)
        message = input("Entrez votre message: ")
        print(message)
        envoyer(message)
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('127.0.0.1', 50000))  # Écoute sur le port 50000
serveur.listen(5)#nobre de tentative de connection
print("Servuer en attente d'un client ...")
while True:#si vrai on entre dans la boucle
    client, infosClient = serveur.accept()#le serveur accepte la connexion du client
    thread= threading.Thread(None, instanceServeur, None, (client, infosClient), {})
    thread.start()#demarrage du thread
    print("\nle client",(thread),"connecté")
    #dialogue()
serveur.close()
