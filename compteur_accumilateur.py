
def compteur_accumulateur(nbr:int):
    # initialisation de variables compteur et à accumulateur
    compteur = 0
    accumulateur = 0
    
    while compteur < nbr:
       compteur = compteur +1
       accumulateur = accumulateur + compteur
    

   return accumulateur
