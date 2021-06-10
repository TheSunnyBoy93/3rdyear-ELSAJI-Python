import random
import string
import hashlib

#Generation password
## main programme
## Liste de caractères dispo
List_Caracter = string.ascii_letters+string.digits
print("Liste des caracteres disponobles : ",List_Caracter)

## Mot de passe vide
Password = ""
for i in range(10): ## Longueur : 10 caractères i va de 0 à 9
    #Password = Password+List_Caracter[random.randint(0, len(List_Caracter)-1)]
    Password+=List_Caracter[random.randint(0, len(List_Caracter)-1)]
print("Le mot de passe généré est : ", Password)


## hashing password avec MD5
#print(dir(hashlib))
Md_five = hashlib.md5() ## reversible ie besoin d'un salt(info complementaire)
Md_five.update(b'LPRS2019') ##on initialise password b=Bytes
Md_five.update(b'2e message') ## salt
print("l'empreinte du hashing : ", Md_five.digest)
print("La taille du hash :", Md_five.digest_size)
print("La taille du bloc utilisé par MD5 : ",Md_five.block_size)

##hashing password avec Sha224
Md_five = hashlib.sha224()
Md_five.update(b'LPRS2019') ## password
Md_five.update(b'2e message') ## salt
print("l'empreinte du hashing : ", Md_five.digest)
print("La taille du hash :", Md_five.digest_size)
print("La taille du bloc utilisé par SHA224 : ",Md_five.block_size)


## Génération password aleatoire
def password_generate(): ## Method fonction
    List_Caracter = string.ascii_letters + string.digits
    print("Liste des caracteres disponobles : ", List_Caracter)
    ## user renseigne la taille du pwd
    Taille_Pwd = int(input("Veillez entrer la taille de votre password compris entre 8 et 12 inclus : "))
    ## Mot de passe vide
    Password = ""
    for i in range(Taille_Pwd):
        # Password = Password+List_Caracter[random.randint(0, len(List_Caracter)-1)]
        Password += List_Caracter[random.randint(0, len(List_Caracter) - 1)]
    print("Le mot de passe généré est : ", Password)
    return Password
##ashing du password,fonction v1
def hasher_pwd(mdp): ## sans salt, pour le MD5
    Mdp_byte = mdp.encode("utf-8")
    Mdp_hash = hashlib.md5(Mdp_byte).hexdigest()
    return Mdp_hash

def hashing(Passwd,salt):
    md_five = hashlib.md5() ##md_five objet à hashé
    md_five.update(Passwd.encode()) # lier message
    md_five.update(salt.encode())
    print("Hash MD5 : \n", hashlib.md5(Passwd.encode()).hexdigest())
    ## ou alors en SHA224
    print("Hash Sha224 : \n", hashlib.sha224(Passwd.encode()).hexdigest())
    return hashlib.md5(Passwd.encode()).hexdigest() # ou hashlib.sha224(Passwd.encode()).hexdigest()

## Appel generation passwd dans un Main prog
Password = password_generate()

## Appel mdp hashé dans un Main prog
Password = hashing(Passwd, '3')
