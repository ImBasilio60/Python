from Models.Group import Group
from Models.model import Model

class Tourist(Model):
    def __init__(self, numero):
        self.numero = numero
        self.nom = None
        self.id_groupe = None

        if self.numero:
            self._load_from_db()

    def _load_from_db(self):
        result = self.get_by_id(self.numero)
        if result:
            self.nom = result["Nom"]
            self.id_groupe = result["id_groupe"]
            self.group = Group(self.id_groupe)
            self.group.add_member(self)

    def get_nom(self):
        return self.nom

