#! /usr/bin/python3
# -*- coding:utf-8 -*-
## Scanner de ports
## By ELSAJI

#import Mdp_et_Verif, csv
## Importation des modules
import socket,threading, datetime


## Definition de la classe Thread
from pip._vendor.distlib.compat import raw_input



class Thread_Scan(threading.Thread):
    "Definition d'une classe Thread"
    ## Constructeur
    def __init__(self,h,p):
        threading.Thread.__init__(self)
        self.host = h
        self.port = p

    ## Methode run du Thread
    def run(self):
        global report
        for rang in range(self.port,self.port+5):
            self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.mysocket.settimeout(0.2)
            try:
                self.mysocket.connect((self.host,rang))
            except:
                self.mysocket.close()
            else:
                report[rang] = "ouvert."
                self.mysocket.close()

## Fonction qui affiche les ports ouvert
def Affiche_port(report):
    lstreport = report.items()
    for port in lstreport:
        print("Port %s ouvert"%(port[0]))

## Fonction qui enregistre le resultat
def Enregistrer(report):
    #  pour la date utilise ceci
    now = datetime.datetime.now()
    print("date et l'heure du scan :", now.strftime('%A %d %m %y , %H:%M:%S'))
    lstreport = report.items()
    ficher = open("Scan_rapport.txt","a")
    ficher.write("\n\n*****\-ELSAJI Report-/*****\n\n")
    ficher.write("la date et l'heure du scan : " + now.strftime('%A %d - %m - %y, %H:%M:%S') + "\n")
    #  ou bien
    #ficher.write(" La date et l'heure :" + now1.strftime('%A %d %y, %H:%M:%S'))
    if(len(lstreport) == 0):
        ficher.write("Aucun ports ouvert.")
    else:
        for rport in lstreport:
            ficher.write("\n")
            ficher.write('\n+-----------+---------------+')
            ficher.write('\n|port       |   etat        |')
            ficher.write('\n+-----------+---------------+')
            #service = socket.getservbyport(port)
            # on affiche le port et le protocol associé a ce port
            #print("[ * {} * EST OUVERT ---> {} ]".format(port, service))
            ficher.write("\n| %s       |   ouvert      |"%(rport[0]))
            ficher.write('\n+-----------+---------------+')
    ficher.close()

## Programme principale
if __name__ == "__main__":

    ## Creation des variables
    report,i,lstth = {},0,[]

    ## Menu à renseigner pour l'utilitisateur
    print("****\-Scanner de ports ELSAJI/****\n")
    Host = raw_input("Entrer l'adresse ip: ")
    Portd = eval(input("Entrer le port de debut: "))
    Portf = eval(input("Entrer le port de fin: "))

    ## Creation des Threads scannant 5 ports chacun
    for port in range(Portd, Portf+1, 5):
        lstth.append(Thread_Scan(Host,port))
        lstth[i].start()
        i += 1

    ## Attente fin des Threads
    for c in lstth:
        c.join()

    ## Affiche port si 0 ouvert
    if(len(report) == 0):
        print ("Aucun ports ouvert.")
    else:
        Affiche_port(report)
        ## Demande d'enregistrement du resultat
    choix = raw_input("Voulez vous enregistrer le resultat: (O)ui | (N)on: ")
    if(choix.upper() == "O"):
        Enregistrer(report)
        print ("Resultat enregistre avec succes !")

Temp = raw_input("Appuyez sur une touche pour continuer...")



