class GroupeModel(object):
    def __init__(self, code = None, nom_g = None):
        self.code = code
        self.nom = nom_g
        self.members = []