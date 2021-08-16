'''
Une des forces de Python : la possibilité de créer une liste à partir d'autres en rajoutant des conditions à la volée et le tout en une ligne !
Donnons des exemples : Pour augmenter de 3 tous les éléments d'une liste de nombres
'''

ma_liste_de_nombres = [1, 2, 3, 4, 5]
print([ n + 3 for n in ma_liste_de_nombres ])