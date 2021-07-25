class Salarié(object):  ## qui hérite de object, classe racine
    """Classe des salariés"""           # Documentation de la classe
### un salarié étant défini par un Nom, et un Prenom
### Constructeur de la classe : construite et initialiser un  objet
    def __init__(self, nom, pnom):
        print ("Création d'un objet salarié...")
        self.Nom = nom
        self.Prenom=pnom
### Les méthodes get et set , plus d'autres méthodes de traitement dont l'affichage 
    def get_nom(self):  # Méthode 'get' pour retourner le nom
        return self.Nom
    def get_pnom(self):
        return self.Prenom
  ### pour toutes les caratéristiques ou attributs de la classe
    def set_nom(self, nouveau_nom):   # Méthode 'set' pour modifier le nom
        if nouveau_nom == "":
            print ("Le nom de l'employé ne peut pas être vide!!!!")
        else:
            self.Nom = nouveau_nom
            print ("Le Nom à été modifié.") 
    def set_pnom(self, nouveau_pnom):   # Méthode 'set' pour modifier le nom
        if nouveau_pnom == "":
            print ("Le prénom de l'employé ne peut pas être vide!!!!")
        else:
            self.Prenom = nouveau_pnom
            print ("Le Nom à été modifié.")
            
    def afficher(self):
        print (self.Nom, " a été ajouté(e)")
        
### User est une classe qui hérite de la classe Salarié#

### Les attributs pour la classe User : Nom et Prenom hérités, puis Login et Password
###class Users():
    
class User(Salarié):
    ### constructeur de la nouvelle classe User
    def __init__(self, nom, pnom, login, pwd):
        print ("Création d'un objet User...")
        ## Construction/création d'un salarié d'abord
        Salarié.__init__(self,nom, pnom)
        ## équivalent à:
        ##self.Nom = nom
        ##self.Prenom=pnom
        self.Login=login
        self.Password=pwd
    ### Fin construction/création/initialisation d'un User
        
    ### les get et les set pour les attributs login et pwd   
    def Afficher_User(self):
        print("User : ", self.get_nom(),"", self.get_pnom())
        ## les attributs get et set pour login et password
        # get method pour return le nom
        def get_login(self):
            return self.Login
        # get method pour return le mot de passe
        def get_Password(self):
            return self.Password
        #on affiche le nom et prenom
        def display_User(self):
            print("Utilisateur : ", self.get_nom(), " ", self.get_pnom())
    
##    def GenPWD(self): génaration aléatoire
##    def hashPWD(self, pwd): MD5+salt, Sha
##    def VerifPWD(self), hashpwd): comparaison des empreintes de hashage

#####################################   Fin des classes 
    
# main, programme principal
## Classe mère : Salarié
salarié1 = Salarié(input("veillez entre le Nom et Prenom : "))#("HENO","Martin")  # Initialiser un objet de la classe vide
salarié1.afficher()               # Accéder à une méthode de la classe
 
print ("Nom de l'employé est:", salarié1.get_nom()) # Accéder à une propriété de la classe
print ("Modification du nom de la classe :")
salarié1.set_nom("") # Génération d'une erreur, si Nom est vide
### Refaire avec le bon paramètre : nom pas vide 
salarié1.set_nom("ESGI")
salarié1.afficher()

## classe qui dérive : User
### Au prélable génération du login et pwd
User1=User("OULMI", "Céline", "coulmi", "Mypass")
User1.Afficher_User()
print("Nom de User:",User1.get_nom())


