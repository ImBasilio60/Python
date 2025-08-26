from Models.model import Base
from Models.Group import Group

class Tourist:
    def __init__(self, id, base: Base):
        self.numero = id
        self.base = base
        self.nom = None
        self.codeG = None
        self.group = None

        if self.base.con is not None:
            self.load_from_db()

    def load_from_db(self):
        query = "SELECT Nom, CodeG FROM touriste WHERE Numero = %s"
        self.base.cur.execute(query, (self.numero,))
        result = self.base.cur.fetchone()
        if result:
            self.nom = result["Nom"]
            self.codeG = result["CodeG"]
            self.group = Group(self.codeG, self.base)
            self.group.add_member(self)

    def get_nom(self):
        return self.nom





