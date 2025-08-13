from Models.model import Model


class TouristeModel(Model):
    def __init__(self, num, nom, grp):
        self.numero = num
        self.nom = nom
        self.troupe = grp
        grp.membres.append(self)