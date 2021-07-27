#import option as option

granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_detail.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("connexion avec succès")
        grant()
    else:
        print("login ou mot de passe incorrect")
        
def register(name,password):
    file = open("user_detail.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Entrez votre login: ")
        password = input("Entrez votre password: ")
        login(name,password)
    else:
        print("Entrez votre nom et mot de passe pour enregister")
        name = input("Entrez votre login: ")
        password = input("Entrez votre password: ")
        register(name,password)

def begin():
    global option
    print("welcome to ELSAJI's programming club")
    option = input("Login or Enregistrer (Login,Reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    print("BienVenue chez ELSAJI")
    print("### USER DETAILS ###")
    print("nom user: ",name)


    
