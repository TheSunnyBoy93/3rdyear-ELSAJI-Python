import option as option

granted = False
def grant():
    global granted
    granted = True
def login(name,password,grade):
    success = False
    file = open("C:/Users/jacqu/Reseau-GES/ELSAJI - Documents/Python/user_detail.txt","r")
    for i in file:
         a,b,c = i.split(",")
         b = b.strip()
         if(a==name and b==password and c==grade):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")
        
def register(name,password,grade):
    file = open("C:/Users/jacqu/Reseau-GES/ELSAJI - Documents/Python/user_detail.txt","a")
    file.write("\n"+name+","+password+","+grade)
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Entrez votre  name: ")
        password = input("Entrez votre  password: ")
        grade = input("Entrez votre status : ")
        login(name,password,grade)
    else:
        print("Enregistrer un utilisateur ")
        name = input("Enter votre nom: ")
        password = input("Enter votre password: ")
        grade = input("Entrez votre status : ")
        register(name,password,grade)

def begin():
    global option
    print("welcome to ELSAJI's programming club")
    option = input("Login or Register (login,Reg): ")
    if(option!="login" and option!="reg" and option!="grade"):
        begin()
        
begin()

if(granted):
    print("Welcome to ELSAJI's Programming club")
    print("### USER DETAILS ###")
    print("Username: ",name)
    access(Menu_Principal)

    
