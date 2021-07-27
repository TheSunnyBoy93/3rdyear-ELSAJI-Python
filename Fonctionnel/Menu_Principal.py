## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
#import Menu_users_AC
#import Menu_users_AS
#import mysql_connexion
#mysql_connexion.connexion_bdd()
print('********** Bienvenue chez ELSAJI **********')
#import Menu_users_AC as grade
grade = input("Veuillez entrer votre status 'AS' ou 'AC' : ")
while grade == 'AS':
    mdp = input("Veuillez entrer un mot de passe AS : ")
    if mdp == "Elsaji2021":
        import Menu_users_AS
        Menu_users_AS
    else:
        print("Mot de passe incorrect, veuillez reessayer !!!")
        mdp
while grade == 'AC':
    mdp1 = input("Veuillez entrer un mot de passe AC : ")
    if mdp1 == "Elsaji21":
        import Menu_users_AC
        Menu_users_AC
    else:
        print("Mot de passe incorrect, veuillez reessayer !!!")
        mdp1