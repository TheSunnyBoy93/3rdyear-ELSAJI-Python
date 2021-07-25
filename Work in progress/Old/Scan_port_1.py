import pyfiglet
import sys
import socket
from datetime import datetime

#Afficher un titre en ascii
ascii_banner = pyfiglet.figlet_format("CODE STAR BOY")
print(ascii_banner)
print(" ################  BIENVENUE DANS SCANNER DE PORTS ################\n")

#Le choix d'executer ou pas une action
action = input("Si voulez-vous executer une action taper 'Y' pour oui ou 'N' pour sortir: ")

#La boucle While permettant de continuer ou pas
while action == "Y":
        #choix d'effectuer un scan de port ou pas
        choix = eval(input("Veillez choisir 1 si vous voulez effectuer un scan sinon tapper 0: "))
        #tant que choix est egal a 1 on entre dans la boucle
        while choix == 1:
            # definir l'adresse ip de la machine ou serveur a scanner
            target = str(input("Entrez une @IP :"))
            # je definis les ports a scanner
            ports = [19, 20, 30, 21, 22, 23, 25, 53, 80, 443]
            # condition de scan
            for port in range(ports):
                # on definit la variable scan
                scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scan.settimeout(0.2) #temps de scan par port en seconde
                # on affiche le port scanner
                print(port, "PORT SCANNER!")
                connect = scan.connect_ex((target, port))
                # si le port est ouvert on rentre dans cette condition
                if connect == 0:
                    # on definit la var service qui definit le protocole associé au port
                    service = socket.getservbyport(port)
                    # on affiche le port et le protocol associé a ce port
                    print("[ * {} * EST OUVERT ---> {} ]".format(port, service))
                    scan.close()
        #si choix est defferent de 1 et 0 on affiche choix invalid et on recommence
        if choix != 1 and choix != 0:
            print("CHOIX INVALID !!!")
#return scan.connect_ex((target, port)),socket.getservbyport(port)
scan = portscan()
print("FIN DU SCAN !!!")
#fin du programme