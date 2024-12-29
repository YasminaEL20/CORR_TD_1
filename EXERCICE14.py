# Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère s et de lui renvoyer un 
# message indiquant si la chaine contient la lettre 'a' tout en indiquant sa position sur la chaine.  
# Exemple si l’utilisateur tape la chaine s = ‘langage’, le programme lui renvoie : La lettre 'a' se trouve à la position : 1 ; 
# La lettre 'a' se trouve à la position : 4

s = input("Saisissez une chaîne de caractères : ")

# Parcourir chaque caractère de la chaîne
for i in range(len(s)):
    if s[i] == 'a':
        print(f"La lettre 'a' se trouve à la position : {i}")
else:
    print("La lettre 'a' ne se trouve pas dans cette chaîne de                    caractérecaractére")

