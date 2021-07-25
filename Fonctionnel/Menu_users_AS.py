## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
import main

#choix_continue = input("Tapez 'AS' pour excuter le code ou 'Q' pour quitter : ")
while grade == 'AS':
    print("\n********** Vocici la liste des option !!! ***********\n")
    print("[Option 1] = Gestion utilisateurs !")
    print("[Option 2] = Gestion FTP !")
    print("[Option 3] = Boite à outils !")
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
        print("[Option 0] = Revenir au Menu Principal !")
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
    if choix == 3:
        print("\n********** Vocici la liste des option !!! ***********\n")
        print("[Option 1] = Scanner des ports !")
        print("[Option 2] = Simuler une attaque force brute !")
        print("[Option 0] = Revenir au Menu Principal !")
        choix3 = eval(input("Veillez choisir une option : "))
        if  choix3 == 1:
            print("\n********** Vocici la liste des option !!! ***********\n")
            print("[Option 1] = Scanner un port !")
            print("[Option 2] = Scanner une plage des ports !")
            print("[Option 0] = Revenir au Menu Precedant !")
            choix31 = eval(input("Veillez choisir une option : "))
            if choix31 == 1:
                import Scan_port_1
                Scan_port_1
            if choix31 == 2:
                print("ce programme n'est pas encore mis en place !!!")
                choix31
            if choix31 == 0:
                choix31
            else:
                print("Choix INVALID !!!")
                break
        if choix3 == 2:
            print("ce programme n'est pas encore mis en place !!!")
            choix2
        if choix3 == 0:
            choix2
        else:
            print("Choix INVALID !!!")
            break
    #if choix == 4:
        #print("ce programme n'est pas encore mis en place !!!")
    if choix == 0:
        break
    else:
        print("Choix INVALID !!!")
        choix