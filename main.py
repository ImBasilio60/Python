from Models.GroupeModel import GroupeModel
from Models.TouristeModel import TouristeModel

grp = GroupeModel(5, "Group python")

tour = TouristeModel(1, "Alice", grp)

grp.close()

# grp.membres.append(tour)
print(grp.membres[0].nom)