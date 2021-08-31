# Générateurs Python
'''Les générateurs Python sont très puissants pour gérer les opérations qui nécessitent une grande quantité de mémoire.
Commençons par un exemple simple. La fonction ci-dessous imprime une séquence infinie de nombres.'''

def  generator_example1 (): 
    count  =  0 
    while  True : 
        return  count 
        count += 1
'''
Performances du générateur Python

Une chose à noter ici est que les générateurs Python sont plus lents que la compréhension de liste Python si la mémoire est assez grande pour le calcul. Regardons ci-dessous deux exemples 
du point de vue de la performance.

import sys


'''

