from Models.Group import  Group
from Models.Tourist import  Tourist
from Models.base import Base

# tourists = Tourist.get_all()
# for tourist in tourists:
#     print(tourist)

# groupes = Group.get_all()
# for group in groupes:
#     print(group)

tourist_6 = Tourist(6)
tourist_7 = Tourist(7)
tourist_8 = Tourist(8)
tourist_9 = Tourist(9)
tourist_10 = Tourist(10)

groupes = Group.all_instances()
for group in groupes:
    print("-----------------------------------------------------")
    print("Membres de la groupe: ", group.get_nom())
    print("-----------------------------------------------------")
    membersOfGroup =  group.get_members()
    for member in membersOfGroup:
        print(member.get_nom())


Base.close()