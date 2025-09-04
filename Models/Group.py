from typing import reveal_type

from Models.model import Model


class Group(Model):
    _instances = {}

    def __new__(cls, id):
        if id in cls._instances:
            return cls._instances[id]
        instance = super().__new__(cls)
        cls._instances[id] = instance
        return instance

    def __init__(self, code):

        if hasattr(self, "_initialized") and self._initialized:
            return

        self.code = code
        self.nomG = None
        self.members = []

        if self.code:
            self._load_from_db()

        self._initialized = True

    def _load_from_db(self):
        result = self.get_by_id(self.code)
        if result:
            self.nomG = result["NomG"]

    def add_member(self, member):
        self.members.append(member)

    def get_members(self):
        return self.members

    def get_nom(self):
        return self.nomG

    @classmethod
    def all_instances(cls):
        return list(cls._instances.values())



