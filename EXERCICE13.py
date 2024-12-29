# Ecrire un programme en langage Python qui permet de parcourir et afficher les caractères d’une variable du type chaine 
# de caractères. Exemple pour s = « PYTHON », le programme affiche les caractères :  
# P 
# Y 
# T 
# H 
# O 
# N

c=input("donner un mot : ").split()
for i in range(0,len(c)):
    for j in range(0,len(c[i])):
        print(c[i][j])



