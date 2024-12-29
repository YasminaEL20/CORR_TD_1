#Écrivez un programme Python pour afficher tous les nombres impairs de 1 à n en utilisant la boucle for et while. 



#on demmande à l'utilisateur d'entrer un nombre n 
n = int(input("Entrez la valeur de n : "))
for i in range(1, n+1, 2): 
        # on affiche les résultat 
        print(i)



# Exemple d'utilisation
n = int(input("Entrez la valeur de n : "))
i = 1
while i <= n:
    print(i)
    i += 2  # on ajoute 2 pour passer au nombre impair suivant