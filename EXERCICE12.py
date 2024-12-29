# Ecrire une fonction compteMots(phrase) qui renvoie le nombre de mots contenus dans la phrase "phrase". On 
# considère comme mots les ensembles de caractères inclus entre des espaces.

def MOTS(phrase):
    mots=(phrase.strip()).split(" ")
    return len(mots)

p=input("entrer une phrase : ")
print(f"le nombre de mots dans cette phrases est : {MOTS(p)}")
