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

# compte = CompteBancaire(100)
#
# sold = compte.afficherSolde()
# print(sold)
#
# compte.deposer(50)
# sold = compte.afficherSolde()
# print(sold)
#
# compte.retirer(30)
# sold = compte.afficherSolde()
# print(sold)
#
# compte.retirer(130)
# sold = compte.afficherSolde()
# print(sold)

#Accès controlé avec des getters/setters

# class Personne:
#     def __init__(self, nom):
#         self.__nom = nom
#
#     def get_nom(self):
#         return self.__nom
#
#     def set_nom(self, nom):
#         if isinstance(nom, str) and nom != "":
#             self.__nom = nom
#
# personne_one = Personne("Basilio")
# print(personne_one.get_nom())
# personne_one.set_nom("Martial")
# print(personne_one.get_nom())

#Façon python moderne
class Personne:
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        if isinstance(nom, str) and nom:
            self.__nom = nom

personne_one = Personne("Basilio")
print(personne_one.nom)
