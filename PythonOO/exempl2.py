class Achat:
    def __init__(self, client, produit, compte_bancaire):
        self.client = client
        self.produit = produit
        self.compte_bancaire = compte_bancaire

class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.comptes_bancaires = []
        self.achats = []

    def ajouter_compte_bancaire(self, compte_bancaire):
        self.comptes_bancaires.append(compte_bancaire)

    def ajouter_achat(self, produit, compte_bancaire):
        achat = Achat(self, produit, compte_bancaire)
        self.achats.append(achat)

class CompteBancaire:
    def __init__(self, numero, solde):
        self.numero = numero
        self.solde = solde