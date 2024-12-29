#Écrire un programme Python qui permet d'évaluer une note saisie au clavier (si la note est supérieure à 10 alors
# il affiche validé sinon non validé (NB : la note comprise entre 0 et 20). 

# on demmande à l'utilisateur d'enter une note

note = float(input("Entrez une note : "))

if note > 10 and note < 20  :
    print("Validé")
elif note < 10 and note > 0 :
    print("non validé") 


#fin du programme 




