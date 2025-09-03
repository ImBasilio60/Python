from Models.model import Model


class Group(Model):
    def __init__(self, code, nomG):
        self.code = code
        self.nomG = nomG

    @classmethod
    def update(cls, code, nomG):
        if code and nomG:
            query = f"UPDATE groupe SET nomG = \"{nomG}\" WHERE id_groupe = {code}"
            Model.update(query)