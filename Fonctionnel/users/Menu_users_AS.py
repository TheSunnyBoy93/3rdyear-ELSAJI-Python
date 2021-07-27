## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
#import main

#choix_continue = input("Tapez 'AS' pour excuter le code ou 'Q' pour quitter : ")
while True:
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
        print("[Option 0] = Revenir au Menu Principal !")
        choix2 = eval(input("Veillez choisir une option : "))
        if choix2 == 1 or choix2 == 2 or choix2 == 3:
            import FTP
            FTP
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
            if choix31 == 1 or choix31 == 2:
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
                            ficher.write("\n")
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
                    Host = input("Entrer l'adresse ip: ")
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
                    choix = input("Voulez vous enregistrer le resultat: (O)ui | (N)on: ")
                    if (choix.upper() == "O"):
                        Enregistrer(report)
                        print("Resultat enregistre avec succes !")
                break
            if choix31 == 0:
                choix31
            else:
                print("Choix INVALID !!!")
                break
        if choix3 == 2:
            import Bruteforce_V1
            Bruteforce_V1
            break
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