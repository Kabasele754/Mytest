
def compteur_accumulateur(nbr:int):
    # initialisation de variables compteur et à accumulateur
    compteur = 0
    accumulateur = 0
    
    while compteur < nbr:
       # tant que le compteur est inférieure au nombre passé dans le paramètre de la fonction 
       compteur = compteur +1
       accumulateur = accumulateur + compteur
    

   return accumulateur
