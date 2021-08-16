'''
Une des forces de Python : la possibilité de créer une liste à partir d'autres en rajoutant des conditions à la volée et le tout en une ligne !
Donnons des exemples : Pour augmenter de 3 tous les éléments d'une liste de nombres
'''

ma_liste_de_nombres = [1, 2, 3, 4, 5]
print([ n + 3 for n in ma_liste_de_nombres ])

'''
## Si je veux la somme des carrés des entiers de 1 à 10, je peux par exemple faire :

print(sum( [ n**2 for n in range(1,11) ] ))

##  je veux les longueurs des mots d'une liste de mots :

ma_liste_de_mots = [ "Cosinus", "Sinus", "Tangente", "Cotangente" ]
print([ len(mot) for mot in ma_liste_de_mots])

## Si je veux récupérer la première lettre des mots d'une liste commençant par une voyelle :

ma_liste_de_mots= ["maths", "info", "python", "exposant", "alpha", "fonction", "parabole", "equilateral", "orthogonal", "cercle", "isocèle" ]
print([ mot[0] for mot in ma_liste_de_mots if mot[0] in "aeiouy"])
'''