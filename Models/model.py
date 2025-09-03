from Models.base import Base

class Model:
    def __str__(self):
        chaine = ""
        for attr, value in self.__dict__.items():
            chaine += f"{attr:11s}: {value}\n"
        return chaine

    @classmethod
    def __close(cls):
        base = Base()
        if base.cur:
            base.cur.close()
        if base.con:
            base.con.close()

    @classmethod
    def get_all(cls):
        try:
            base  = Base()
            table = cls.__name__.lower()
            query = f"SELECT * FROM {table}e"
            base.cur.execute(query)
            list_dict = base.cur.fetchall()
            return list_dict
        except Exception as e:
            print(f"get all value error: {e}")
            return []

    @classmethod
    def get_by_id(cls, id):
        try:
            base = Base()
            table = cls.__name__.lower()
            pk = f"id_{table}e"
            query = f"SELECT * FROM {table} WHERE {pk} = %s"
            base.cur.execute(query, (id,))
            return base.cur.fetchone()
        except Exception as e:
            print(f"get single value error: {e}")
            return None

    @classmethod
    def insert(cls, data: dict):
        try:
            base = Base()
            table = f"{cls.__name__.lower()}e"
            query = f"INSERT INTO {table} "
            data = {"code": 1, "nomG": "Baobab"}
            # INSERT INTO groupe(code, nomG) VALUES(1, 'baobab')
            i = 0
            for attr in data:
                i = i + 1
                query = query + attr
                if i <len(data):
                    query = query + " , "
            query += " ) VALUES ("
            i = 0
            for _ in data:
                i = i + 1
                query = query + "%s "
                if i < len(data):
                    query = query + " , "
            query += " ) "

            lists = list()
            i = 0
            for attr in data.keys():
                lists.append(data[attr])

            tuples = tuple(lists)
            base.cur.execute(query, tuples)
            base.con.commit()
            
        except Exception as e:
            print(f"insert value error: {e}")


    @classmethod
    def delete(cls, id):
        try:
            base = Base()
            table = f"{cls.__name__.lower()}e"
            pk = f"id_{table}"
            query = f"DELETE FROM {table} WHERE {pk} = %s"
            base.cur.execute(query, (id,))
            base.con.commit()
        except Exception as e:
            print(f"deleting error: {e}")

    @classmethod
    def update(cls, query):
        try:
            base = Base()
            base.cur.execute(query)
            base.con.commit()
        except Exception as e:
            print(f"updating error: {e}")