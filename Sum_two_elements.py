import functools as fts

'''
Pour la somme de deux nombres
Cette fonction permet de faire la somme de plus élément passer dans une liste
'''
def sum_two_elements(a,b):
    return a+b
number = [1,5,7,9,3,2]
resultat = fts.reduce(sum_two_element, number)

print(resultat)
