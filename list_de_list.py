"""
Listes de listes :
Dans une liste, on peut mettre beaucoup de choses différentes et entre autre 
des listes ce qui est bien pratique si on veut stocker comme dans un tableau. 
Par exemple une grille de morpion pourrait s’écrire : grille = [["O", "X", "O"], ["O", "X", "X"], ["X", "O", "O"]] 
Pour récupérer l'élément de la deuxième ligne troisième colonne il suffit que j'écrive grille[1][2] car les listes commencent à 0 donc il faut penser à décaler d'un cran et de plus, grille[1] est la liste ["O", "X", "X"], c'est donc naturel que pour récupéré le troisième élément, on écrive grille[1][2]. Les listes de listes servent souvent à représenter un tableau mais on n'est pas obligé de s’arrêter 
à une profondeur de deux. On peut faire des listes de listes de listes...
"""

liste = [ "T", "e", "x", "t", "e" ]
for i, c in enumerate(liste):
    print(i,c)

"""
grille= [[1,2,3],[4,5,6],[7,8,9]]
print(grille[2][1])
"""

def add_list(a,b):
    return a*b
"""
Pour cette fonction qui permet de faire la puissance de deux nombres
"""

outup = liste(map(add_list([4,3,6],[8,9,2])))
print(outup)
