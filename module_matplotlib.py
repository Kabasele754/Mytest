"""
Les fonctions de base



plt.show() : Pour afficher le résultat. Toute les fonctions qui suivent servent à 
préparer le graphique mais si on ne demande pas de l'afficher, rien ne se passera 
(exactement comme la fonction print : aucun calcul ne s'affiche si on ne demande pas de 
l'afficher avec print).

plt.plot(liste_x,liste_y) : Où liste_x est une liste de nombres [x_1, x_2, ..., x_n] 
et liste_y une liste de nombres [y_1, y_2, ..., y_n] avec le même nombre d'éléments. Alors plt.plot(liste_x,liste_y) placera les points de coordonnées (x_1,y_1), (x_2,y_2), ..., (x_n, y_n) et les reliera de proche en proche par un 
segment. Voici un exemple où on relie les points (1;2), (3;1) et (4;6) :

"""

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,3,4],[2,1,6])

plt.show()

"""
Vous pouvez modifier les listes de points dans le programme ci-dessus pour voir le résultat.
L'idée pour tracer une fonction va donc être de placer beaucoup de points de la courbe 
qu'on veut représenter assez proches pour qu'on ne voit pas qu'ils sont reliés par une droite.

np.linspace(debut, fin, N) : C'est ici que le module numpy intervient. 
Pour tracer correctement une fonction, il va nous falloir beaucoup de points qu'il est hors de question de rentrer à la main comme dans l'exemple précédent. La fonction np.linspace(debut, fin, nombre) permet de créer une liste de N nombres qui commencent à la valeur debut et s'arrête à la valeur fin et uniformément répartis.
De plus, si on fait une opération sur cette liste comme par exemple multiplier par 2, alors 
cette opération sera automatiquement appliquée à chaque terme de la liste (ce qui n'est pas vrai si on utilise une liste classique).
Par exemple, traçons la fonction définie par y = 2x²+3x-4 entre -2 et 2 en utilisant 100 points :
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = 2*x**2+3*x-4

plt.plot(x,y)
plt.show()

"""
Tracé de fonctions plus complexes

Supposons qu'on veuille tracer des fonctions faisant intervenir autre chose 
que les opérations +, -, *, / et ** comme par exemple des cosinus, sinus, exponentielle, 
logarithme... Dans ce cas on ne peut pas faire exactement comme dans l'exemple précédent.

    Une première façon de faire est de créer "à la main" la liste des y 
    correspondants aux x c'est à dire créer une liste composée des f(x) pour x dans la liste des abscisses.
    Par exemple si on veut tracer la fonction y = cos(x) + 3 sin(2x) entre -4 et 4, on pourra faire ainsi :
"""

import matplotlib.pyplot as plt
import numpy as np
from math import *

abscisses = np.linspace(-4,4,100)
ordonnées = [cos(x)+3*sin(2*x) for x in abscisses]
plt.plot(abscisses,ordonnées)
plt.show()
