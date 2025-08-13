from Models.model import Model

class TouristeModel(Model):
    def __init__(self, num=None, nom=None):
        self.numero = num
        self.nom = nom