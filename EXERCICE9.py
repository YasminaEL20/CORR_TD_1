# Un palindrome est un mot dont l'ordre des lettres reste le même si on le lit de gauche à droite ou de droite à gauche. 
# Par exemple : 'laval' , 'radar, 'sos'... sont des palindromes. Ecrire un programme en Python qui demande à l'utilisateur 
# de saisir un mot et de lui renvoyer s'il s'agit d'un palindrome ou non?

# on demmande à l'utilisateur d'enter un mot 

mot =input("Entrez un mot : ")
list_mot=[]
if list_mot==list_mot[::-1]:
    print("Le mot est un palindrome")
else:
    print("Le mot n'est pas un palindrome")

