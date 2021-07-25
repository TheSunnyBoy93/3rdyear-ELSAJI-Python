import socket
from tkinter import *
from tkinter.messagebox import *


def connexion():
    global connexion_avec_client, infos_connexion, connexion_principale

    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((HOST.get(), PORT.get()))
    connexion_principale.listen(5)
    print("Le serveur écoute à présent sur le port {}".format(PORT.get()))
    connexion_avec_client, infos_connexion = connexion_principale.accept()
    dialogue()

def envoyer(message):
    message=message.encode()
    connexion_avec_client.send(message)

def recevoir():
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu=msg_recu.decode()
    return msg_recu

def dialogue():
    while 1:
        msg_recu=recevoir()
        print(msg_recu)
        message = input("Entrez votre message: ")
        print(message)
        envoyer(message)

    print("Fermeture de la connexion")
    connexion_avec_client.close()
    connexion_principale.close()


# Création de la fenêtre principale (pop window)
Mafenetre = Tk()

Mafenetre.title('Mise en réseau - Serveur')

# Cadre1 : paramètres serveur
cadre1 = Frame(Mafenetre,borderwidth=2,relief=GROOVE)
cadre1.grid(row=0,column=0,padx=10,pady=10,sticky=W+E)

Label(cadre1, text = "Hôte").grid(row=0,column=0,padx=5,pady=5,sticky=W)
HOST = StringVar()
HOST.set('192.168.1.10')
Entry(cadre1, textvariable= HOST).grid(row=0,column=1,padx=5,pady=5)

Label(cadre1, text = "Port").grid(row=1,column=0,padx=5,pady=5,sticky=W)
PORT = IntVar()
PORT.set(50026)
Entry(cadre1, textvariable= PORT).grid(row=1,column=1,padx=5,pady=5)

ButtonConnexion = Button(cadre1, text ='Ouvrir le serveur',command=connexion)
ButtonConnexion.grid(row=0,column=2,rowspan=2,padx=5,pady=5)

Mafenetre.mainloop()