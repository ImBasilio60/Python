from Models.model import Base

class Tourist:
    __base = Base()
    def __init__(self, id, base: Base):
        self.base = base
        self.numero = id
        self.nom = None
        self.codeG = None

        self.base.cur.execute("SELECT Nom, CodeG FROM touriste WHERE Numero = ?", (self.numero,))
        dico = self.base.cur.fetchone()

        if dico:
            self.nom = dico["Nom"]
            self.codeG = dico["CodeG"]

    def __str__(self):
        chaine = f"Numero: {self.numero}\nNom: {self.nom}\nGroup {self.codeG}"
        return chaine

    @classmethod
    def get_all(cls):
        cls.__base.cur.execute("SELECT * FROM touriste")
        return cls.__base.cur.fetchall()

    @classmethod
    def get_by_id(cls, id):
        cls.__base.cur.execute("SELECT * FROM touriste WHERE Numero = ?", (id,))
        return cls.__base.cur.fetchone()

    @classmethod
    def insert(cls, nom, group_code):
        cls.__base.cur.execute("INSERT INTO touriste VALUES (%s, %s)", (nom, group_code))
        cls.__base.con.commit()

    @classmethod
    def update(cls, id, nom, group_code):
        cls.__base.cur.execute("UPDATE touriste SET Nom = %s, CodeG = %s WHERE Numero = %s", (nom, group_code, id))
        cls.__base.con.commit()

    @classmethod
    def delete(cls, id):
        cls.__base.cur.execute("DELETE FROM touriste WHERE Numero = %s", (id,))
        cls.__base.con.commit()









