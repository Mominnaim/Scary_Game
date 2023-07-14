import random

from skeleton_scary_game import Father
from skeleton_scary_game import Item
from skeleton_scary_game import Lore


users_bagpack_1 = ["Pistol","Gunpowder","Magazine"]
item_main = ['Pistol','Magazine','Gunpowder']
users_bagpack_2 = ['Battery']
item_list = ["Battery"]
demon = 1
lore_sto = ['The father was in the forrest with his child.  ','He turned around to see where his child went,'
        'as soon as he turned aorund, he saw a demon like figure take his child and disappear', 'Once he found his child, the demon was with her and asked him this question.',
        'The demon said "If you take my spot as the demon then your child will be set free, if not shes dies right here in front of you."']
    # If the user picks this path then they will find out who the demon was, and how he became that way.

Dad = Father()
story = Lore(lore_sto)

Dad.create_gun(users_bagpack_1,item_main)

if "Deagle" in users_bagpack_1:
    print("I can shoot that demon")
    print(item_main)
    print(users_bagpack_1)
else:
    print(users_bagpack_1)






