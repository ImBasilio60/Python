from Models.model import Base
class Group:
    _instances = {}

    def __new__(cls, id, base:Base):
        if id in cls._instances:
            return cls._instances[id]
        instance = super().__new__(cls)
        cls._instances[id] = instance
        return instance


    def __init__(self, id, base: Base):

        if hasattr(self, "_initialized") and self._initialized:
            return

        self.code = id
        self.base = base
        self.nomG = None
        self.members = []

        if self.base.con is not None:
            self._load_from_db()

        self._initialized = True

    def _load_from_db(self):
        query = "SELECT NomG FROM groupe WHERE Code = %s"
        self.base.cur.execute(query, (self.code,))
        result = self.base.cur.fetchone()
        if result:
            self.nomG = result["NomG"]


    # def __setattr__(self, attr, val):
    #     if attr in ["nomG"]:
    #         self.__dict__[attr] = val
    #         self.base.cur.execute("UPDATE groupe SET nomG = %s WHERE code = %s",(val, self.code))
    #         self.base.con.commit()
    #     elif attr in ["base", "code"]:
    #         self.__dict__[attr] = val

    def add_member(self, member):
        self.members.append(member)

    def get_members(self):
        return self.members

    def get_nom(self):
        return self.nomG

    @classmethod
    def all_instances(cls):
        return list(cls._instances.values())