from Models.model import Model

class Tourist(Model):
    def __init__(self, numero, nom, code):
        self.numero = numero
        self.code = code
        self.nom = nom

    @classmethod
    def update(cls, code, nom, id_groupe):
        if code and nom and id_groupe:
            query = f"UPDATE touriste SET Nom = \"{nom}\", id_groupe = {id_groupe} WHERE id_touriste = {code}"
            Model.update(query)