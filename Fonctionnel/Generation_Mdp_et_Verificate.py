## Importation des modules
import random
import string
import hashlib
import csv

#generation mdp alea
def gen_mdp (nbre_caracter):
    caracter_list = string.ascii_letters+string.digits#+string.punctuation
    pwd = ""
    for i in range(nbre_caracter):
        pwd+=caracter_list[random.randint(0, len(caracter_list)-1)]
    return (pwd)

# hashé le mdp genere aleatorement
def hash_mdp(pwd):
    salt = "un salt" ##info redondante pour le MD5(reversible)
    hash_passwd = hashlib.md5(pwd.encode()+salt.encode()).hexdigest()
    return (hash_passwd)

## verification mdp user
def verif_mdp(input_pwd,generate_pwd):
    hash_test = hash_mdp(input_pwd)
    if (hash_test == generate_pwd):
        return True
    else:
        return False

## programme principal
#long_passwd = input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
choix = eval(input("veillez choisir 1 pour continuer ou 0 pour quitter : "))
while choix != 1 and choix != 0 :
    print("choix invalid, veillez recommencer !!!")
    choix = eval(input("veillez choisir 1 pour continuer ou 0 pour quitter : "))
    if choix == 0:
        break
else:
    while choix == 1:
        long_passwd = input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
        while long_passwd < '8' and long_passwd  > '12':
            print("Trop court ou trop long ressayer")
            long_passwd =  input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
        else:
            mdp = gen_mdp(int(long_passwd)) #on genere un mdp de la longueur renseigner
            print(" Le mot de passe est : ", mdp)
            hashing_pwd = hash_mdp(mdp)#on hashe le mdp genere
            print("Le mot de passe hashé est : ", hashing_pwd)#on affiche le mdp hashé
            #break
        ##Creer un fichier pour stocker les mot de passe
        # chemin du repertoire du fichier ou sont stocher les password en
        destFile = r"C:/Users/Abdalaye konate/OneDrive/ESGI/Projet Python/BON/Pwd_ID.csv"
        with open(destFile, 'a', newline="") as f:
            f.write("{}, {}\n".format(mdp,hashing_pwd)) ##Ajouter le mot dans le fichier csv
        #chemin du repertoire du fichier ou sont stocher les password en txt
        destFile1 = r"C:/Users/Abdalaye konate/OneDrive/ESGI/Projet Python/BON/Pwd_ID.txt"
        with open(destFile1, 'a',) as f:
            f.write("{}, {}\n".format(mdp,hashing_pwd)) ##Ajouter l'empreinte dans le fichier txt

        ##Test de verification de connection
        print("Veillez vous authentifier pour une vérification !!!")
        nbre_tentative = 1 #on initialise la variable à 1
        while nbre_tentative <= 3 : #boucle de tentative jusqu'a 3 fois
            inpu_pwd = input("Entrez votre mot de passe : ") #user renseigne son password
            print("Veillez patienté, comparaison des empreintes MD5 en cour...")
            #mdp_hash = hash_mdp(inpu_pwd)
            #si mot de passe entrer correspond on passe
            if (verif_mdp(inpu_pwd,hashing_pwd) == True):
                print("Mot de passe correct \n")
                print("Vous pouvez à présent continuer ...")
                continuer= input("Tapez 1 pour un scan des ports ou 2 pour quitter: ") #choix de continuer ou pas
                #while continuer == 1:
                #   from Scanner_de_ports import Thread_Scan
                #else:
                break
            else:#si mot de passe est incorrect on redemande
                print("Mot de passe incorrect !\n")
                nbre_tentative += 1
        if nbre_tentative > 3 : #si nombre de tentative superieur a 3 on verouille le compte
            print("Vous êtes blacklisté, contactez un administrateur !")
        break
