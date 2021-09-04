"""
Une fonction récursive est tous simplement une fonction qui s'appelle elle même.
Prenons un exemple : Le calcul de la somme des entiers entre 1 et n.
L'idée est d'expliquer comment il faut commencer et ce qu'il faut faire pour passer de l'étape n-1 à l'étape n. Python s'occupe du reste.
Pour commencer, si n vaut 1, la somme vaut 1. Ensuite si j'ai déjà calculé la somme de 1 à n-1, il suffit de lui ajouter n pour obtenir 
la somme de 1 à n. Cela donnerait le programme suivant :
"""

def somme(n):
    if n==1:
        return 1
    else :
        return somme(n-1)+n

"""
Détaillons ce qu'il se passe lorsqu'on le lance :

    Pour calculer somme(3) :
   1 3 ne vaut pas 1 donc on exécute le else. On renvoie somme(2)+3. mais comme on ne connait pas encore somme(2), on met le calcul en mémoire le temps de le calculer.
   2 On exécute somme(2) : comme 2 ne vaut pas 1 donc on exécute le else. On renvoie somme(1)+2. mais comme on ne connait pas encore somme(1), on met de calcul en mémoire le temps de le calculer.
   3 On exécute somme(1) : comme 1 == 1, on renvoie 1.
   4  Maintenant qu'on connait le résultat de somme(1), on peut calculer somme(1)+2. de l'étape 2 ce qui nous donne 3 comme valeur pour somme(2).
   5  Maintenant qu'on connait le résultat de somme(2), on peut calculer somme(2)+3. de l'étape 1 ce qui nous donne 6 comme valeur pour somme(3). Comme c'était la valeur demandée initialement, le programme renvoie 6.
    Comme on peut le voir les calculs effectués sont plus long à expliquer que le programme en lui même. C'est l'intérêt d'une écriture récursive : c'est l'ordinateur qui a à gérer la complexité de ce qu'il se passe, nous on a juste à lui expliquer comment passer d'une étape à l'autre.

"""
