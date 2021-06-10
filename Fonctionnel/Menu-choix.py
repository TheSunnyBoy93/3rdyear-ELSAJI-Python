## Importation des modules
import random
import string
import hashlib
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input


choix_continue = input("Tapez 'Y' pour excuter le code ou 'Q' pour quitter : ")
while choix_continue == 'Y':
    print("\n********** Vocici la liste des option !!! ***********\n")
    print("[Option 1] = Generation des mots de passe aléatoire !")
    print("[Option 2] = scan des ports !")
    print("[Option 0] = Quittez !")

    choix = eval(input("Veillez choisir une option : "))
    if choix == 1:

        # generation mdp alea
        def gen_mdp(nbre_caracter):
            caracter_list = string.ascii_letters + string.digits  # +string.punctuation
            pwd = ""
            for i in range(nbre_caracter):
                pwd += caracter_list[random.randint(0, len(caracter_list) - 1)]
            return (pwd)


        # hashé le mdp genere aleatorement
        def hash_mdp(pwd):
            salt = "un salt"  ##info redondante pour le MD5(reversible)
            hash_passwd = hashlib.md5(pwd.encode() + salt.encode()).hexdigest()
            return (hash_passwd)


        ## verification mdp user
        def verif_mdp(input_pwd, generate_pwd):
            hash_test = hash_mdp(input_pwd)
            if (hash_test == generate_pwd):
                return True
            else:
                return False


        ## programme principal
        # long_passwd = input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
        print("\n\n ***** Generateur de mot de passe ELSAJI *****\n\n")
        choix = eval(input("\nveillez choisir 1 pour commencer à générer un mdp ou 0 pour quitter : "))
        while choix != 1 and choix != 0:
            print("choix invalid, veillez recommencer !!!")
            choix = eval(input("veillez choisir 1 pour continuer ou 0 pour quitter : "))
            if choix == 0:
                break
        else:
            while choix == 1:
                long_passwd = input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
                while long_passwd < '8' and long_passwd > '12':
                    print("Trop court ou trop long veuillez retenter")
                    long_passwd = input("Veillez entre la longueur de votre mdp entre 8 et 12 inclus : \n")
                else:
                    mdp = gen_mdp(int(long_passwd))  # on genere un mdp de la longueur renseigner
                    print(" Le mot de passe est : ", mdp)
                    hashing_pwd = hash_mdp(mdp)  # on hashe le mdp genere
                    print("Le mot de passe hashé est : ", hashing_pwd)  # on affiche le mdp hashé
                    # break
                ##Creer un fichier pour stocker les mot de passe
                # chemin du repertoire du fichier ou sont stocher les password en
                destFile = r"stock_password.csv"r"C:/Users/Abdalaye konate/OneDrive/ESGI/Projet Python/BON/Pwd_ID.csv"
                with open(destFile, 'a', newline="") as f:
                    f.write("{}, {}\n".format(mdp, hashing_pwd))  ##Ajouter le mot dans le fichier csv
                # chemin du repertoire du fichier ou sont stocher les password en txt
                destFile1 = r"stock_password.txt"#r"C:/Users/Abdalaye konate/OneDrive/ESGI/Projet Python/BON/Pwd_ID.txt"
                with open(destFile1, "a") as f:
                    f.write("{}, {}\n".format(mdp, hashing_pwd))  ##Ajouter l'empreinte dans le fichier txt

                ##Test de verification de connection
                print("Veillez vous authentifier pour une vérification !!!")
                nbre_tentative = 1  # on initialise la variable à 1
                while nbre_tentative <= 3:  # boucle de tentative jusqu'a 3 fois
                    inpu_pwd = input("Entrez votre mot de passe : ")  # user renseigne son password
                    print("Veillez patienté, comparaison des empreintes MD5 en cour...")
                    # mdp_hash = hash_mdp(inpu_pwd)
                    # si mot de passe entrer correspond on passe
                    if (verif_mdp(inpu_pwd, hashing_pwd) == True):
                        print("Mot de passe correct \n")
                        print("Vous pouvez à présent continuer ...")
                        continuer = input(
                            "Tapez 1 pour un scan des ports ou 2 pour quitter: ")  # choix de continuer ou pas
                        # while continuer == 1:
                        #   from Scanner_de_ports import Thread_Scan
                        # else:
                        break
                    else:  # si mot de passe est incorrect on redemande
                        print("Mot de passe incorrect !\n")
                        nbre_tentative += 1
                if nbre_tentative > 3:  # si nombre de tentative superieur a 3 on verouille le compte
                    print("Vous êtes blacklisté, contactez un administrateur !")
                break

    if choix == 2:
        ## Definition de la classe Thread

        class Thread_Scan(threading.Thread):
            "Definition d'une classe Thread"

            ## Constructeur
            def __init__(self, h, p):
                threading.Thread.__init__(self)
                self.host = h
                self.port = p

            ## Methode run du Thread
            def run(self):
                global report
                for rang in range(self.port, self.port + 5):
                    self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.mysocket.settimeout(0.2)
                    try:
                        self.mysocket.connect((self.host, rang))
                    except:
                        self.mysocket.close()
                    else:
                        report[rang] = "ouvert."
                        self.mysocket.close()


        ## Fonction qui affiche les ports ouvert
        def Affiche_port(report):
            lstreport = report.items()
            for port in lstreport:
                print("Port %s ouvert" % (port[0]))


        ## Fonction qui enregistre le resultat
        def Enregistrer(report):
            #  pour la date utilise ceci
            now = datetime.datetime.now()
            print("date et l'heure du scan :", now.strftime('%A %d %m %y , %H:%M:%S'))
            lstreport = report.items()
            ficher = open("Scan_rapport.txt", "a")
            ficher.write("\n\n*****\-ELSAJI Report-/*****\n\n")
            ficher.write("la date et l'heure du scan : " + now.strftime('%A %d - %m - %y, %H:%M:%S') + "\n")
            #  ou bien
            # ficher.write(" La date et l'heure :" + now1.strftime('%A %d %y, %H:%M:%S'))
            if (len(lstreport) == 0):
                ficher.write("Aucun ports ouvert.")
            else:
                for rport in lstreport:
                    ficher.write("\n@ip du client : {}".format(Host))
                    ficher.write('\n+-----------+---------------+')
                    ficher.write('\n|port       |   etat        |')
                    ficher.write('\n+-----------+---------------+')
                    # service = socket.getservbyport(port)
                    # on affiche le port et le protocol associé a ce port
                    # print("[ * {} * EST OUVERT ---> {} ]".format(port, service))
                    ficher.write("\n| %s       |   ouvert      |" % (rport[0]))
                    ficher.write('\n+-----------+---------------+')
            ficher.close()


        ## Programme principale
        if __name__ == "__main__":

            ## Creation des variables
            report, i, lstth = {}, 0, []

            ## Menu à renseigner pour l'utilitisateur
            print("****\-Scanner de ports ELSAJI/****\n")
            Host = raw_input("Entrer l'adresse ip: ")
            Portd = eval(input("Entrer le port de debut: "))
            Portf = eval(input("Entrer le port de fin: "))

            ## Creation des Threads scannant 5 ports chacun
            for port in range(Portd, Portf + 1, 5):
                lstth.append(Thread_Scan(Host, port))
                lstth[i].start()
                i += 1

            ## Attente fin des Threads
            for c in lstth:
                c.join()

            ## Affiche port si 0 ouvert
            if (len(report) == 0):
                print("Aucun ports ouvert.")
            else:
                Affiche_port(report)
                ## Demande d'enregistrement du resultat
            choix = raw_input("Voulez vous enregistrer le resultat: (O)ui | (N)on: ")
            if (choix.upper() == "O"):
                Enregistrer(report)
                print("Resultat enregistre avec succes !")

        Temp = raw_input("Appuyez sur une touche pour continuer...")

    if choix == 0:
        break

    else:
        print(" Choix invalid !!! ")