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
            table = f"{cls.__name__.lower()}e"
            pk = f"id_{table}"
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

            columns = tuple(data.keys())
            columns = str(columns)
            columns = columns.replace("'", "")
            columns = columns.replace(",)", ")")

            values = tuple(data.values())
            values = str(values)
            values = values.replace(",)", ")")

            query = f"INSERT INTO {table} {columns} VALUES {values}"
            base.cur.execute(query)
            base.con.commit()
            
        except Exception as e:
            print(f"insert value error: {e}")

    @classmethod
    def update(cls, data: dict):
        try:
            base = Base()
            table = f"{cls.__name__.lower()}e"
            pk = f"id_{table}"
            pk_value = None
            query = f"UPDATE {table} SET "
            if pk in data:
                for i, (key, value) in enumerate(data.items()):
                    if pk != key:
                        if isinstance(value, (int, float)):
                            if i != len(data) - 1:
                                query += f"{key} = {value}, "
                            else:
                                query += f"{key} = {value}"
                        if isinstance(value, str):
                            if i != len(data) - 1:
                                query += f"{key} = \"{value}\", "
                            else:
                                query += f"{key} = \"{value}\""
                    else:
                        pk_value = value
            query += f" WHERE {pk} = {pk_value}"
            base.cur.execute(query)
            base.con.commit()
        except Exception as e:
            print(f"update value error: {e}")

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