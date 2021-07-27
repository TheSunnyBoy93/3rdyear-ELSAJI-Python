## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
import main

#choix_continue = input("Tapez 'AC' pour excuter le code ou 'Q' pour quitter : ")
while grade == 'AC':
    print("\n********** Vocici la liste des option !!! ***********\n")
    print("[Option 1] = Gestion utilisateurs !")
    print("[Option 2] = Gestion FTP !")
    print("[Option 0] = Quittez !")

    choix = eval(input("Veillez choisir une option : "))
    if choix == 1:
        print("\n********** Vocici la liste des option !!! ***********\n")
        print("[Option 1] = Créer un utilisateur !")
        print("[Option 2] = Modifier un utilisateur !")
        print("[Option 3] = Supprimer un utilisateur !")
        print("[Option 4] = consulter la liste utilisateur !")
        print("[Option 0] = Revenir au Menu Principal !")
        choix1 = eval(input("Veillez choisir une option : "))
        if choix1 == 1:
            print("ce programme n'est pas encore mis en place !!!")
            choix
        if choix1 == 2:
            print("ce programme n'est pas encore mis en place !!!")
            choix
        if choix1 == 3:
            print("ce programme n'est pas encore mis en place !!!")
            choix
        if choix1 == 4:
            print("ce programme n'est pas encore mis en place !!!")
            choix
        if choix1 == 0:
            choix
        else:
            print("Choix INVALID !!!")
            choix
    if choix == 2:
        print("\n********** Vocici la liste des option !!! ***********\n")
        print("[Option 1] = Gestion des repertoires !")
        print("[Option 2] = Gestion des fichiers!")
        print("[Option 3] = Lister les fichiers !")
        print("[Option 0] = Revenir au Menu Precedent !")
        choix2 = eval(input("Veillez choisir une option : "))
        if choix2 == 1:
            print("ce programme n'est pas encore mis en place !!!")
            choix2
        if choix2 == 2:
            print("ce programme n'est pas encore mis en place !!!")
            choix2
        if choix2 == 3:
            print("ce programme n'est pas encore mis en place !!!")
            choix2
        if choix2 == 0:
            choix2
        else:
            print("Choix INVALID !!!")
            choix

    #if choix == 4:
        #print("ce programme n'est pas encore mis en place !!!")
    if choix == 0:
        break
    else:
        print("Choix INVALID !!!")
        choix