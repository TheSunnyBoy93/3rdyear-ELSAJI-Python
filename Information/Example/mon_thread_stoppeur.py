import threading
from time import time, ctime, sleep

# cas d'héritage de la classe Thread du module Threading

class mon_thread(threading.Thread):
    def __init__(self, nom, delai):
        self.delay=delai
        self.job_ended= False
        threading.Thread.__init__(self, name=nom)

    def run(self):
        for i in range(10):
            if self.job_ended:
                print("Arrêt focé de la tâche de : %s" %(self.getName()))
                return
            print("%s : Appel %s, %s " %(self.getName(), i, ctime(time())))
            sleep(self.delay)
        print(" Arrêt normal de : %s" %(self.getName()))


# classe stoppeur qui hérite de la classe Thread

class Stoppeur(threading.Thread):
    def __init__(self, threads, delai):
        print(" Création du stoppeur de tâches ...")
        self.delay=delai
        self.threads=threads
        threading.Thread.__init__(self)
    def run(self):
        sleep(self.delay)
        print("Demande l'arret des tâches :")
        for t in self.threads:
            t.job_ended=True
             

# le programme principal
# avec gestion des exceptions

try:
#   instanciation de 3 threads
    t1=mon_thread("T1", 2)    # en 2 secondes
    t2=mon_thread("T2", 3)    # en 3 secondes
    t3=mon_thread("T3", 1)    # en 1 secondes
    s=Stoppeur((t1, t2, t3), 15)
    
#  lancement des taches 
    t1.start()   
    t2.start()
    t3.start()
    s.start()
    
except :
    print("Erreur : Impossible de lancer les threads")

 
