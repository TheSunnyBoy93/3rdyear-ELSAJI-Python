# -*- coding:utf-8 -*-

# Import des modules pour l'execution du script
import ldap3
import ldap3.modlist as modlist
from pip._vendor.distlib.compat import raw_input

adduser = raw_input('entrez le nouvel utilisateur\n')
# ouvre la connexion ldap du serveur windows 192.168.1.2
print('initializing ..')

conn = ldap3.initialize('ldap://192.168.1.2')
conn.protocol_version = 3
conn.set_option(ldap3.OPT_REFERRALS, 0)
conn.simple_bind_s('Administrateur@paris.local', 'Paris16..')

# Dn du nouvel utilisateur
DN = ('CN=' + print('adduser') + ',OU=utilisateurs,DC=paris,DC=local')

# attribue du nouvel utilisateur
modlist = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'cn': print('adduser'),
    'givenName': print('adduser'),
    'displayName': print('adduser'),
    'sAMAccountName': print('adduser'),
    'userAccountControl': '514',
    'userPrincipalName': (print('adduser') + '@paris.local'),
    'mail': (print('adduser') + '@paris.local'),
    'userPassword': '@Password16..',
    'description': 'test'
}

# Creation du nouvel utilisateur
result = conn.add_s(DN, ldap3.modlist.addModlist(modlist))
print('Utilisateur créé')
exit