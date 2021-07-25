#! /usr/bin/python3
#importer des modules


#from mysql.connector import connection, cursor
import mysql

#from BDD.mysql_connexion import curser
from mysql.connector import cursor


def connecxion_bdd():
    #les informations a renseigner par l'utilisateur
    server_name= input("Entrez le nom ou ip du serveur bdd : ")
    username = input("Entrez le d'utilisateur (login) : ")
    password = input("Entrez le mot de passe si vous en avez : ")
    namebdd = input("Entrez le nom de la base des données : ")

    # se connecter a la base des données
    connection = mysql.connector.connect(host=server_name, user=username, password=password, db=namebdd)
    curseur = connection.cursor()
    return connection
try:
    #recuperer les inforamtions d'une table
    #connecxion_bdd()
    server_name = input("Entrez le nom ou ip du serveur bdd : ")
    username = input("Entrez le d'utilisateur (login) : ")
    password = input("Entrez le mot de passe si vous en avez : ")
    namebdd = input("Entrez le nom de la base des données : ")

    # se connecter a la base des données
    connection = mysql.connector.connect(host=server_name, user=username, password=password, db=namebdd)
    curseur = connection.cursor()
    #name_table = input("Entrez le nom de la table : ")
    #if connection.is_connected():
     #   db_Info = connection.get_server_info()
      #  print("Connected to MySQL Server version ", db_Info)
       # cursor = connection.cursor()
        #cursor.execute("select database();")
        #record = cursor.fetchone()
        #print("You're connected to database: ", record)
    requet = cursor.execute("SELECT * FROM 'utilisateur'")

    affiche = cursor.fetchall()

    for affichage in affiche:
        print(affichage)
    # faire une recherche dans la base des onnées
    curseur = connection.cursor()
    nom_user = ("MENISSIEUR",)
    curseur.execute("SELECT * FROM `utilisateurs` WHERE nom = {}".format(nom_user))
    donner = curseur.fetchone()
    print(donner)
except Error as e:
    print(e)
finally:
    if (connection.is_connected()):
        connection.close()






