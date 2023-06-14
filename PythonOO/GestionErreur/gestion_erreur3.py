class ErreurDeFichier(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            contenu = f.read()
            return contenu
    except FileNotFoundError:
        raise ErreurDeFichier("Le fichier spécifié est introuvable : {}".format(nom_fichier))
    except PermissionError:
        raise ErreurDeFichier("Vous n'avez pas les permissions nécessaires pour accéder au fichier : {}".format(nom_fichier))


# Exemple d'utilisation
try:
    contenu = lire_fichier("mon_fichier.txt")
    print(contenu)
except ErreurDeFichier as e:
    print("Une erreur s'est produite : {}".format(e))

