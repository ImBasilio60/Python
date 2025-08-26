from Models.model import Base
from Models.Tourist import Tourist
from Models.Group import Group

base = Base()

tourist_6 = Tourist(6, base)
tourist_7 = Tourist(7, base)
tourist_8 = Tourist(8, base)
tourist_9 = Tourist(9, base)

groupes = Group.all_instances()
for group in groupes:
    print("-----------------------------------------------------")
    print("Membres de la groupe: ", group.get_nom())
    print("-----------------------------------------------------")
    membersOfGroup =  group.get_members()
    for member in membersOfGroup:
        print(member.get_nom())


base.close()