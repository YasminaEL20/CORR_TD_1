#Écrire un programme Python qui permet d'échanger le contenu de deux entiers A et B saisis par l'utilisateur. 
# Afficher ces entiers après l’échange.

# on demmande à l'utilisateur de donner ces deux entiers
A=int(input("Donner l'entier A : "))
B=int(input("Donner l'entier B : "))
# on effectue l'operation d'echange
A,B=B,A

# on affiche le resultat final

print(f"le nombre A est devenue : A={B} , et Best devenue : B={A} ")

#fin du programme