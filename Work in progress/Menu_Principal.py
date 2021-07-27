## Importation des modules
import random
import string
import hashlib
#import Scanner_de_ports, Generation_Mdp_et_Verificate
import csv
import socket,threading, datetime
from pip._vendor.distlib.compat import raw_input
#from main import access
import main
access=(main)
#grade = input("Tapez 'AS' ou 'AC' en fonction de votre role ou 'Q' pour quitter : ")
if grade == 'AS':
    import Menu_users_AS
    access=(Menu_users_AS)

if grade == 'AC':
    import Menu_users_AC
    access=(Menu_users_AC)
