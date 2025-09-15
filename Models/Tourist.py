from Models.Group import Group
from Models.model import Model

class Tourist(Model):
    def __init__(self, numero):
        self.numero = numero
        dico = Tourist.get_by_id(numero)
        self.nom = dico["nom"]
        code = dico["id_groupe"]
        self.groupe = Group(code)
        self.groupe.members.append(self)




# Aona ny fomba ahafahana mi-controller attribut static
# Meta class
# Controle d'acces aux attributs statique en Python
# equivalentes:
# __setattr__ et __getattr__ pour les attributs de classmethod
# => class Meta()


