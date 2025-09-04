from Models.Group import  Group
from Models.Tourist import  Tourist
from Models.base import Base

tourists = Tourist.get_all()
for tourist in tourists:
    print(tourist)

# groupes = Group.get_all()
# for group in groupes:
#     print(group)



Base.close()