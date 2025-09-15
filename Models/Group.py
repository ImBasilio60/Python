from Models.model import Model

class Group(Model):
    objects = {}

    def __new__(cls, code):
        if code not in list(cls._objects.keys()):
            cls.objects[code] = super(Group, cls).__new__(cls)
            return cls.objects[code]
        else:
            return cls._objects[code]

    def __init__(self, code):
        if not hasattr(self, "code"):
            self.code = code
            dico = Group.get_by_id(code)
            nomG = dico["nomG"]
            self.members = list()

