from Models.model import Model


class Group(Model):
    def __init__(self, code, nomG):
        self.code = code
        self.nomG = nomG
