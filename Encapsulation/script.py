#Encapsulation simple avec attributs privés

# _attribut: protegé
# __attribut: privé

class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde  #private

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print(f"Le montant n'est pas valide {self.__solde} < {montant} ")

    def afficherSolde(self):
        return self.__solde

compte = CompteBancaire(100)

sold = compte.afficherSolde()
print(sold)

compte.deposer(50)
sold = compte.afficherSolde()
print(sold)

compte.retirer(30)
sold = compte.afficherSolde()
print(sold)

compte.retirer(130)
sold = compte.afficherSolde()
print(sold)
