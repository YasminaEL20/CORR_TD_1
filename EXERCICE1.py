# Écrire un programme Python qui demande à l'utilisateur de saisir deux nombres, puis effectue et affiche les opérations 
# suivantes : addition, soustraction, multiplication et division. 


# on demmande à l'utilisateur de taper deux nombres 
n1=float(input("donner le premiére nombre : "))
n2=float(input("donner le deuxiéme nombre : "))

# on affiche le résultat de la somme 
print(f"l'addition est : {n1+n2}")

# on affeche le résultat de la soustraction avec le condition d'avoire un résultat positif
if n1<n2:
    r=n2-n1
    print(f"la soustraction est : {r}")

# ainsi l'affichage du résultat de la multiplication 
print(f"la multiplication est : {n1*n2}")

# le divideur doit être different de 0 , donc on réalise les conditions suivantes
if n1==0:
    print(f"la division est {n1/n2}")
elif n1>n2:
    print(f"la division est {n2/n1}")
else:
    print("inpossible de diviser par '0' ")


# la fin du programme 