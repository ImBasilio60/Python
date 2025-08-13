class GroupeModel(object):
    def __init__(self, id, nom=""):
        self.code = id
        __class__.open()
        __class__.cur.execute("SELECT * FROM Groupes WHERE id = %s", (id,))
        dico = __class__.cur.fetchone()
        self.nom = nom
        self.members = []