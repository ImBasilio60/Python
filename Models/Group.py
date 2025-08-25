from .model import Base

class Group:
    def __init__(self):
        self.db = Base()
        self.cursor = self.db.cur

    def create_group(self, nom):
        query = "INSERT INTO groupe (NomG) VALUES (%s)"
        if nom:
            self.cursor.execute(query, (nom,))
            self.db.con.commit()

    def delete_group(self, code):
        query = "DELETE FROM groupe WHERE code = %s"
        if code:
            self.cursor.execute(query, (code,))
            self.db.con.commit()

    def list_groups(self):
        query = "SELECT * FROM groupe"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_group(self, code, nom):
        if code:
            query = "UPDATE groupe SET NomG = %s WHERE Code = %s"
            if nom:
                self.cursor.execute(query, (nom, code))
                self.db.con.commit()

    def read_group(self, code):
        query = "SELECT * FROM groupe WHERE code = %s"
        if code:
            self.cursor.execute(query, (code,))
            return self.cursor.fetchone()
        return None



