from Models.model import Model

class Tourist(Model):
    def __init__(self, numero, nom, code):
        self.numero = numero
        self.code = code
        self.nom = nom
