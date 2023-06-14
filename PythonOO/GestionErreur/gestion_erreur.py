
class ErreurDeSaisie(Exception):
    pass

class ErreurDeCalcul(Exception):
    pass

def saisir_nombre():
    try:
        nombre = int(input("Entrez un nombre entier : "))
        if nombre < 0:
            raise ErreurDeSaisie("Le nombre doit être positif")
        return nombre
    except ValueError:
        raise ErreurDeSaisie("Vous devez entrer un nombre entier")

def diviser(a, b):
    try:
        resultat = a / b
        if resultat == float('inf'):
            raise ErreurDeCalcul("Division par zéro")
        return resultat
    except ZeroDivisionError:
        raise ErreurDeCalcul("Division par zéro")

try:
    nombre1 = saisir_nombre()
    nombre2 = saisir_nombre()
    resultat = diviser(nombre1, nombre2)
    print("Le résultat de la division est :", resultat)
except (ErreurDeSaisie, ErreurDeCalcul) as e:
    print("Une erreur est survenue :", e)
