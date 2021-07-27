## Importation des modules
import random
import string
import hashlib
import csv

#generation mdp aleatoire
caracter_list = string.ascii_letters+string.digits#+string.punctuation
pwd = ""
for i in range(10):
    pwd += caracter_list[random.randint(0, len(caracter_list)-1)]
print(pwd)

# hashé le mdp genere aleatoirement
salt = "un salt" ##info redondante pour le MD5(reversible)
hash_passwd = hashlib.md5(pwd.encode()+salt.encode()).hexdigest()
print(hash_passwd)

