import socket, sys # l'import de module necessaires

from socket import error

maxp = 100  # le numero de port maximum =&gt; de 0 jusqu'a 1000
timeout = 0.2  # si notre trame n'a pas pu etablir


# une connexion dans 2 secondes , donc le port est fermé
def scan(h):
    h = input("veillez entrez l'IP de la machine : ")
    print("Starting Scann ...nOpen Ports In %s Are :" % (h))
    print('&lt; Port &gt;')
    p = 0
    while p &lt != maxp :
        try:
            # creation de notre socket en TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)  # definition du timeout
            s.connect((h, p))  # ici la trame va essayer de se connecter
            print(' ', p)
            s.close()
            p += 1
    # exception levée quand la trame n'arrive pas a se connecté
        except socket.error :
            s.close()
            p += 1


    print("Scan Complete For : [%s]" % (h))


# deuxième fonction qui va nous retourner le HEADER d'un server web
def scansrv(h):
    # connexion avec le serveur
    con = httplib.HTTPConnection(h, 80)
    print("Trying To Scan : %s" % (h))
    try:
        con.request('HEAD', '/')  # on essaye d'avoir le HEADER
    # exception levée quand le port 80 est fermé ou quand l'IP est down
    except error:
        print("Can't Connect To : %s" % (h))
    else:
        # sinon si tout marche bien , on recupère la réponse
        response = con.getresponse()
        con.close
    # puis on recupere le HEADER et on l'affiche
    server = response.getheader('Server', 'Version du serveur inconnu')
    print("[%s], Is Running : %s" % (h, server))