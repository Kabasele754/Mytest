class ErreurDeSaisie(Exception):
    def __init__(self, message):
        super().__init__(message)

    def saisir_nombre(self):
        nombre = input("Entrez un nombre : ")
        try:
            nombre = float(nombre)
        except ValueError:
            raise ErreurDeSaisie("La saisie n'est pas un nombre valide")
        return nombre

    def diviser(self, nombre1, nombre2):
        if nombre2 == 0:
            raise ErreurDeSaisie("Impossible de diviser par zéro")
        return nombre1 / nombre2

erreur = ErreurDeSaisie("Message d'erreur")

nombre1 = erreur.saisir_nombre()
nombre2 = erreur.saisir_nombre()
resultat = erreur.diviser(nombre1, nombre2)
print(resultat)