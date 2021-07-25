################################################
# Mise en place d'un client simple             #
# simulation d'une connexion client/serveur    #
#"""""""""""""""""  version basique """""""""""#
# Auteur : Céline OULMI                        #
# version  : Bétâ                              #
################################################

import socket, sys ## Importation / inclusion des librairies
  
# création d'un socket client pour la connexion avec le serveur en local
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

### Gestion des exceptions avec 2 blocs try et except
try:
# connexion au serveur, bloc surveillé, et gestion de l'exception
    sock.connect(('192.168.1.10',9999))

except socket.error:
    print("la connexion a échoué.......")
    sys.exit()

print(">>> Connexion établie avec le serveur...")
# Envoi et réception de messages
sock.send(b"hello serveur") ## envoi du hello version Byte
msgServer=sock.recv(1024) # taille par défaut

print(">>> S :", msgServer.decode())## decode du byte au texte unicode
 
while 1:  ## ou True
 
         if msgServer==b'FIN' or msgServer==b'':
              break

         msgClient=input(">>> ")
         msgClient=msgClient.encode()
         print(">>> Envoi vers le serveur")
         sock.send(msgClient)         
         msgServer=sock.recv(100)
         print(">>> Reception du serveur")
         print(msgServer.decode())
       
print (">>> Connexion interrompue par le serveur!!!")
sock.close()
