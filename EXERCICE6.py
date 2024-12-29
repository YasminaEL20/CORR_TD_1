#Écrire un programme Python permettant de calculer la somme S=1+2+3+...+ N, où N saisi par l’utilisateur. Utilisant la 
#boucle while. 


# on demmande à l'utilisateur d'entrer le nombre 'N' 
N=int(input("donner le nombre N :"))
som=0
i=0
while i <= N:
    som=som+i
    i=i+1   
   

# on affiche ce résultat
print("la somme est ", som)
    



