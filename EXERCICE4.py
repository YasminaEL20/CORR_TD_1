#Écrire un programme Python qui permet d'afficher le plus grand de trois entiers saisis au clavier. 

# on demmande à l'utilisateur d'enter trois entiers 

a=int(input("donner l'entier 1 : "))
b=int(input("donner l'entier 2 : "))
c=int(input("donner l'entier 3 : "))

# on utilise une structure conditionnelle pour trouver le plus grand nombre 

if a>b and a>c:
    print("le plus grand nombre est :", a)
elif b>a and b>c:
    print("le plus grand nombre est :", b)
else:
    print("le plus grand nombre est :", c)

# fin du prgramme 
