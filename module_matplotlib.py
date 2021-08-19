'''
Les fonctions de base



plt.show() : Pour afficher le résultat. Toute les fonctions qui suivent servent à 
préparer le graphique mais si on ne demande pas de l'afficher, rien ne se passera 
(exactement comme la fonction print : aucun calcul ne s'affiche si on ne demande pas de 
l'afficher avec print).

plt.plot(liste_x,liste_y) : Où liste_x est une liste de nombres [x_1, x_2, ..., x_n] 
et liste_y une liste de nombres [y_1, y_2, ..., y_n] avec le même nombre d'éléments. Alors plt.plot(liste_x,liste_y) placera les points de coordonnées (x_1,y_1), (x_2,y_2), ..., (x_n, y_n) et les reliera de proche en proche par un 
segment. Voici un exemple où on relie les points (1;2), (3;1) et (4;6) :
'''

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,3,4],[2,1,6])

plt.show()