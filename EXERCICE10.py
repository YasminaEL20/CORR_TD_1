# Écrire une fonction table_multiplication avec trois paramètres : mul(multiplicateur), bornInf et bornSup. 
# Cette fonction doit afficher la table de multiplication avec les trois paramètres. Tester la fonction par un appel dans le 
# programme principal. 
# Par exemple : si mul =3 et bornInf = 2 et bornSup = 5, on aura comme résultat : 
# 3*2=6  
# 3*3=9  
# 3*4=12  
# 3*5=15 

#on définit notre fonction table_multiplication
def table_multiplication(mul, bornInf, bornSup):
    # on fait un changement entre ces deux variables lorsque : bornInf>bornSup
    if bornInf>bornSup :
        bornInf, bornSup =  bornSup,bornInf
    for i in range(bornInf, bornSup + 1):
        print(f"{mul} * {i} = {mul * i}") 

mul = int(input("Entrez le multiplicateur (mul) : "))
bornInf = int(input("Entrez la borne inférieure (bornInf) : "))
bornSup = int(input("Entrez la borne supérieure (bornSup) : "))

table_multiplication(mul, bornInf, bornSup)
#fin de programme






