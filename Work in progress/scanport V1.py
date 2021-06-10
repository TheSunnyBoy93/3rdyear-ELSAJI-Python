#scanneur de port
import socket 
import threading
import time
import datetime

hote = '127.0.0.1'
f=open ('Scan.txt','w')   ##1ier fichier LOG

#  pour la date utilise ceci
now=datetime.datetime.now().date()
print("date :", now.strftime('%A %d %B %y'))

#  pour la date et le temps uitlise ceci
now1=datetime.datetime.now().time()
print("Horaire :", now1.strftime('%A %d %y, %H:%M:%S'))


##now = time.time()
##print("date=======", now)
 
##print ("L'heure et la date actuelle:", time.localtime(now))


f.write ("la date : "  +str(now) +"\n")
#  ou bien
f.write(" La date et l'heure :" +now1.strftime('%A %d %y, %H:%M:%S'))
f.write ("\n")
f.write ('+-----------+---------------+\n')
f.write ('|port       |   etat        |\n')
f.write ('+-----------+---------------+\n')


for i in range (20,60):
    try :
      
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.connect((hote, i))
        #connexion_principale.listen(5)
        print(" le port est ouvert ",i)
        f.write("le port TCP "+str (i)+ "  :ouvert \n")
       
    except:
        print ("le port est fermé",i)
        f.write(" le port TCP "+str (i)+ " :fermé \n")


f.close()

f=open ('Portouvert.txt','w')  ### 2ième fichier

for a in range (70,90):
    try :
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.connect((hote, a))
        connexion_principale.listen(20)
        print("Autre version :")
        print (" OK open port",a)
        f.write("le port TCP  "+str (a)+ "  :ouvert \n")
        connexion_principale.close()
    except :
        print ("Exception : port TCP "+str(a)+" fermé")
        connexion_principale.close()
        
f.close()
