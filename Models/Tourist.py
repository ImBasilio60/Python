from Models.model import Base

class Tourist:
    def __init__(self):
      self.db = Base()
      self.cursor = self.db.cur

    def create_tourist(self, nom=None):
        if nom:
            query= "INSERT INTO touriste (Nom) VALUES (%s)"
            self.cursor.execute(query, (nom,))
            self.db.con.commit()
            return self.cursor.fetchone()
        return None

    def read_tourist(self, numero = None):
        if numero:
            query= "SELECT * FROM touriste WHERE Numero = %s"
            self.cursor.execute(query, (numero,))
            return self.cursor.fetchone()
        return None

    def update_tourist(self, numero=None, nom=None):
        if numero:
            if nom:
                query= "UPDATE touriste SET Nom = %s WHERE Numero = %s"
                self.cursor.execute(query, (nom, numero))
                self.db.con.commit()

    def delete_tourist(self, numero):
        if numero:
            query= "DELETE FROM touriste WHERE Numero = %s"
            self.cursor.execute(query, (numero,))
            self.db.con.commit()
        return None

    def list_tourists(self):
        query= "SELECT * FROM touriste"
        self.cursor.execute(query)
        return self.cursor.fetchall()





