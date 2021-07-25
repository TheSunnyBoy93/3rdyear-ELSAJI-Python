#! /usr/bin/python3

#importation des modules
import mysql.connector
from mysql.connector import errorcode, connection, cursor

## fonction qui renvoie la connexion
#def getconnection():
    # Connection à la base de données.
#from server import connexion

#server_name = input("Entrez le nom ou ip du serveur bdd : ")
#username = input("Entrez le d'utilisateur (login) : ")
#password = input("Entrez le mot de passe si vous en avez : ")
#namebdd = input("Entrez le nom de la base des données : ")

# info pour la connection à la base de données
config = {
    'user': 'root',#username,
    'password': '',#password,
    'host': '127.0.0.1',
    'database': 'python',#namebd
    'raise_on_warnings': True
}
try:#gestion d'erreur lors de la connection a la base
    connection = mysql.connector.connect(**config)
    print("connect successful!!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("L'utilisateur ou le mot de passe n'est pas correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas!")
    else:
        print(err)

    #exit()

paragraphe = 1

# Sélection des informations
if paragraphe == 1:
    curseur = connection.cursor()

    #rechercher une valeur dans la table utilisateur
    selectAction = ("SELECT nom FROM utilisateurs WHERE nom like %s")
    selectValue = ('%'+"abda"+'%',)
    print("Affichage des nom qui contiennent le mot ", selectValue)
    #inserer une valeur dans la table utilisateur
    requet = ("INSERT INTO `utilisateurs` (`nom`, `prenom`, `login`, `mail`, `mdp_hash`, `ville`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)")# ('curtis', 'jacques', 'jcurtis', 'jcurtis@elsaji.fr', 'jhgsGSJJSP765544256sdhjid', 'Rennes', 'Ac')")
    #info = ("curtis", "jacques", "jcurtis", "jcurtis@elsaji.fr", "jhgsGSJJSP765544256sdhjid", "Rennes", "AC")
    #nom =input("entre nom ex: 'exemple': ")

    #l'utilisateur renseigne les infos a ajouter
    nom = input("entre nom ex: 'exemple': ")
    prenom = input("entre prenom ex: 'exemple': ")
    login = input("entre login ex: 'eexemple': ")
    mail = input("entre nom ex: 'exemple': ")
    mdphsher = input("entre mdp hashé ex: 'qihUISHOHSazdjkpd46+46': ")
    ville = input("entre ville ex: 'exemple': ")
    status =input("entre status ex: 'AC' ou 'AS': ")

    #on recupere les infos renseigner et commit
    info = (nom,prenom,login,mail,mdphsher,ville,status)
    curseur.execute(requet, info)
    connection.commit()
    print("Nouvel utilisateur ajouté")#on affiche cela
    curseur.execute(selectAction, selectValue)
    curseur.execute("SELECT * FROM `utilisateurs`")#on recupere toute la table et on affiche
    resultSelect = curseur.fetchall()
    for i in resultSelect:
        print(i)

    curseur.close()

#getconnection()
# création nouvel user
#curser = connection.cursor()
#info = input("""Entrez les informations utilisateurs. Exemple : "MENISSIEUR", "Loic", "lmenissieur","lmenissieur@myges.fr", "slmenissieur@myges", "Lyon", "AC":""")
#new_user = ( "MENISSIEUR", "Loic", "lmenissieur","lmenissieur@myges.fr", "slmenissieur@myges", "Lyon", "AC" )
#cursor.execute("INSERT INTO `utilisateurs` (`nom`, `prenom`, `login`, `mail`, `mdp_hash`, `ville`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)", info ) #('curtis', 'jacques', 'jcurtis', 'jcurtis@elsaji.fr', 'jhgsGSJJSP765544256sdhjid', 'Rennes', 'Ac')")
#connection.commit()
#print("un nouvel user ajouté")
#lire des infos dans la base
#Login = ("curtis",)
#resultat = curser.execute("SELECT * FROM `utilisateurs`")
#resultat = curser.fetchall()
#affcher en mode une seule donnée avec tous les infos du user
#print(f"la tables ets ", resultat)
#curser.execute("SELECT * FROM utilisateurs")
#for result in curser.fetchall():
   # print(result)

#nom_user = ("MENISSIEUR",)
#curser.execute("SELECT * FROM `utilisateurs` WHERE 'nom' = %s",nom_user)
#donner = curser.fetchone()
#print(donner)

#connection.close()
#curser.close()
#print("La connexion a MySQL est d´esormais fermee")