# Écrire une fonction « premier » qui affiche tous les nombres premiers entre limite inférieure et limite supérieure ; les 
# deux limites sont deux paramètres saisis par l’utilisateur.

def premier(limite_inf, limite_sup):
    if limite_inf > limite_sup :
        limite_inf, limite_sup = limite_sup, limite_inf
    elif limite_inf == limite_sup :
        print("Les deux nombres sont égaux")
    
    for i in range(limite_inf, limite_sup + 1):
        if i > 1:  # les nombres premiers sont supérieurs à 1
            # Vérifier si i est divisible par un autre nombre que 1 et lui-même
            est_premier = True
            for j in range(2, int(i**0.5) + 1):  # Optimisation: vérifier jusqu'à la racine carrée de i
                if i % j == 0:
                    est_premier = False
                    break
            if est_premier:
                print(i, end=" ")

x = int(input("Donner le nombre supérieur : "))
y = int(input("Donner le nombre inférieur : "))
premier(x, y)
