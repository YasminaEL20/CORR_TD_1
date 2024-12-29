# Écrivez un programme Python pour entrer un nombre et vérifiez si le nombre est parfait ou non. Un nombre parfait 
# est un entier positif qui est égal à la somme de ses diviseurs positifs appropriés.  
# Par exemple : 6 est le premier nombre parfait Les diviseurs appropriés de 6 sont 1, 2, 3. 
# Somme de ses diviseurs stricts = 1 + 2 + 3 = 6. 
# Par conséquent, 6 est un nombre parfait.  

# on demmande à l'utilisateur d'enter un nombre entier
n=int(input("donner un nombre n : "))
som=0
for i in range(1,n):
    if n%i==0:
        som=som+i
if som==n:
    print("ce nombre est parfait")
else:
    print("ce nombre n'est pas parfait")

# la fin du programme