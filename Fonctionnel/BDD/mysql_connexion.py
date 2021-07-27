#! /usr/bin/python3

#importation des modules
import mysql.connector
#from MySQLdb._mysql import connection

#from server import connexion
from mysql.connector import errorcode, connection, cursor

## fonction qui renvoie la connexion
#def getconnection():
    # Connection à la base de données.
#from server import connexion

#server_name = input("Entrez le nom ou ip du serveur bdd : ")
def connexion_bdd():
    username = input("Entrez le d'utilisateur de la BDD(login) : ")
    password = input("Entrez le mot de passe du user : ")
    namebdd = input("Entrez le nom de la base des données : ")
    # Connection à la base de données
    config = {
        'user': username,
        'password': password,
        'host': '127.0.0.1',
        'database': namebdd,
    }
    try:
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
connexion_bdd()
curseur = connection.cursor()
def ajout_users():
    paragraphe = 1
    # Sélection des informations
    if paragraphe == 1:
            selectAction = ("SELECT nom FROM utilisateurs WHERE nom like %s")
            requet = ("INSERT INTO `utilisateurs` (`nom`, `prenom`, `login`, `mail`, `mdp_hash`, `ville`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)")# ('curtis', 'jacques', 'jcurtis', 'jcurtis@elsaji.fr', 'jhgsGSJJSP765544256sdhjid', 'Rennes', 'Ac')")
            #info = ("curtis", "jacques", "jcurtis", "jcurtis@elsaji.fr", "jhgsGSJJSP765544256sdhjid", "Rennes", "AC")
            #nom =input("entre nom ex: 'exemple': ")
            nom = input("entrez un nom ex: 'exemple': ")
            prenom = input("entrez un prenom ex: 'exemple': ")
            login = input("entrez un login ex: 'exemple': ")
            mail = input("entrez le mail ex: 'exemple': ")
            import gen_mdp
            mdphsher = gen_mdp
            ville = input("entrez la ville ex: 'exemple': ")
            status =input("entrez le status ex: 'AC' ou 'AS': ")
            info = (nom,prenom,login,mail,mdphsher,ville,status)
            curseur.execute(requet, info)
            connection.commit()
            print("Nouvel utilisateur ajouté")
            #curseur.execute(selectAction)
def affiche_users():
    curseur.execute("SELECT * FROM `utilisateurs`")
    resultSelect = curseur.fetchall()
    for i in resultSelect:
        print(i)

    curseur.close()
def modif_users():
    connexion_bdd()
    print("\n********** Vocici la liste des option !!! ***********\n")
    print("[Option 1] = Modifier le nom")
    print("[Option 2] = Modifier le prenom!")
    print("[Option 3] = Modifier le login")
    print("[Option 4] = Modifier le mail")
    print("[Option 5] = Modifier le mot de passe")
    print("[Option 6] = Modifier la ville")
    print("[Option 7] = Modifier le statut")
    print("[Option 8] = Modifier tous les champs utilisateurs")
    print("[Option 0] = Quittez !")
    id_user = input("Entrez l'id du user a modifier :")
    choix=input("Veuillez entrez votre choix :")
    if choix==1:
        nom=input("Veuillez entre le nouveau nom du user :")
        curseur.execute("UPDATE `utilisateurs` SET `nom`=%S WHERE `utilisateur`.`id_user`=%S", nom, id_user)
        connection.commit()
    if choix==2:
        prenom = input("Veuillez entre le nouveau prenom du user :")
        curseur.execute("UPDATE `utilisateurs` SET `prenom`=%S WHERE `utilisateur`.`id_user`=%S", prenom, id_user)
        connection.commit()
    if choix==3:
        login = input("Veuillez entre le nouveau login du user :")
        curseur.execute("UPDATE `utilisateurs` SET `login`=%S WHERE `utilisateur`.`id_user`=%S", login, id_user)
        connection.commit()
    if choix==4:
        mail = input("Veuillez entre le nouveau mail du user :")
        curseur.execute("UPDATE `utilisateurs` SET `mail`=%S WHERE `utilisateur`.`id_user`=%S", mail, id_user)
        connection.commit()
    if choix==5:
        import gen_mdp
        mdp = gen_mdp
        curseur.execute("UPDATE `utilisateurs` SET `mdp_hash`=%S WHERE `utilisateur`.`id_user`=%S", mdp, id_user)
        connection.commit()
    if choix==6:
        ville = input("Veuillez entre le nouveau ville du user :")
        curseur.execute("UPDATE `utilisateurs` SET `ville`=%S WHERE `utilisateur`.`id_user`=%S", ville, id_user)
        connection.commit()
    if choix==7:
        status = input("Veuillez entre le nouveau status du user :")
        curseur.execute("UPDATE `utilisateurs` SET `status`=%S WHERE `utilisateur`.`id_user`=%S", status, id_user)
        connection.commit()
    if choix==8:
        curseur.execute("ALTER TABLE `utilisateurs`")
        connection.commit()
    if choix==0:
        choix
    else:
        print("Choix invalide")

def supprim_users():
    id_user = input("Veillez entrer l'id du user a supprimer 'ex : 2': ")
    curseur.execute("DELETE FROM `utilisateurs` WHERE `utilisateurs`.`id_user` = %s;",id_user)
    connection.commit()

ajout_users()
modif_users()
affiche_users()
supprim_users()
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