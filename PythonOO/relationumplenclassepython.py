class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.comptes_bancaires = []

    def ajouter_compte_bancaire(self, compte_bancaire):
        self.comptes_bancaires.append(compte_bancaire)

class CompteBancaire:
    def __init__(self, numero, solde):
        self.numero = numero
        self.solde = solde

class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Paiement:
    def __init__(self, client, produit, compte_bancaire):
        self.client = client
        self.produit = produit
        self.compte_bancaire = compte_bancaire
    def effectuer(self):
        if self.compte_bancaire.solde >= self.produit.prix:
            self.compte_bancaire.solde -= self.produit.prix
            # print(f"Votre achat a ete effectuer avec success")
            return True
        else:
            # print(f"Votre ballance est inssufisant")
            return True


c = Client("Narcisse","Lubesse")
c.ajouter_compte_bancaire("Vodacom")
print(c.comptes_bancaires)
cb = CompteBancaire(1, 90)
p = Produit("Samsung", 100)
pp = Paiement(c,p,cb)
print(pp.effectuer())