"""
Les variables locales et globales.

La chose importante à comprendre sur les variables est : 
Toutes les variables que l'on crée et utilise à l'intérieur d'une fonction n'existent qu'à l'intérieur de cette fonction.
Par exemple si je lance ceci :
"""
a=18
def fonction(n):
    a=n+1
fonction(3)
print(a)

"""
J'obtiendrais que sa n'existe pas. Le a à l'intérieur de la fonction est ce qu'on appelle une variable locale qui n'existe que dans la fonction pas en dehors.
Encore pire :
"""
