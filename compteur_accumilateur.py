
def compteur_accumulateur(nbr:int):
    # initialisation de variables compteur et à accumulateur
    compteur = 0
    accumulateur = 0
    
    while compteur < nbr:
       # tant que le compteur est inférieure au nombre passé dans le paramètre de la fonction 
       compteur = compteur +1
       # l'accumulateur conserve le résultat de la boucle
       accumulateur = accumulateur + compteur
    

    return accumulateur
