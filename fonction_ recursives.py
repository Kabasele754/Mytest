'''
Une fonction récursive est tous simplement une fonction qui s'appelle elle même.
Prenons un exemple : Le calcul de la somme des entiers entre 1 et n.
L'idée est d'expliquer comment il faut commencer et ce qu'il faut faire pour passer de l'étape n-1 à l'étape n. Python s'occupe du reste.
Pour commencer, si n vaut 1, la somme vaut 1. Ensuite si j'ai déjà calculé la somme de 1 à n-1, il suffit de lui ajouter n pour obtenir 
la somme de 1 à n. Cela donnerait le programme suivant :
'''

def somme(n):
    if n==1:
        return 1
    else :
        return somme(n-1)+n