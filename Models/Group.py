from Models.model import Base
class Group:
    __base = Base() #class
    def __init__(self, code):
        self.base = Base() #objet
        self.code = code
        self.nomG = None

        self.base.cur.execute("SELECT NomG FROM groupe WHERE code = %s", (self.code,))
        dico = self.base.cur.fetchone()

        if dico:
            self.nomG = dico["NomG"]

    def __str__(self):
        chaine = f"Code: {self.code}\n Nom: {self.nomG}\n"
        return chaine

    @classmethod
    def get_all(cls):
        cls.__base.cur.execute("SELECT * FROM groupe")
        return cls.__base.cur.fetchall()

    @classmethod
    def get_by_id(cls, id):
            cls.__base.cur.execute("SELECT * FROM groupe WHERE code = %s", (id,))
            return cls.__base.cur.fetchone()

    @classmethod
    def insert(cls, nom):
        cls.__base.cur.execute("INSERT INTO groupe VALUES (NULL, %s)", (nom,))
        cls.__base.con.commit()

    @classmethod
    def update(cls, id, nom):
        cls.__base.cur.execute("UPDATE groupe SET nomG = %s WHERE code = %s", (nom, id))
        cls.__base.con.commit()

    @classmethod
    def delete(cls, id):
        cls.__base.cur.execute("DELETE FROM groupe WHERE code = %s", (id,))
        cls.__base.con.commit()



