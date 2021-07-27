## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
#import main

#choix_continue = input("Tapez 'AC' pour excuter le code ou 'Q' pour quitter : ")
while True:
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
            if choix1 == 1:
                from mysql_connexion import ajout_users
                ajout_users()
            if choix1 == 2:
                from mysql_connexion import modif_users
                modif_users()
            if choix1 == 3:
                from mysql_connexion import supprim_users
                supprim_users()
            if choix1 == 4:
                from mysql_connexion import affiche_users
                affiche_users()
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
        if choix2 == 1 or choix2 == 2 or choix2 == 3:
            import FTP
            FTP
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