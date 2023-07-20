import random

from skeleton_scary_game import Father
from skeleton_scary_game import Item
from skeleton_scary_game import Lore


def father_test_one(Dad,users_bagpack_2,demon):
        print("Running Father test one:")
        Dad.use_item(users_bagpack_2,demon)
        if users_bagpack_2:
            print("Failed!")
        else:
            print("Passed")

def father_test_two(Dad,user_bp):
        print("Running Father test two:")
        Dad.create_torch(user_bp)
        if "Wooden stick" in user_bp:
            print("Passed!")
        else:
            print("Failed")

def father_test_three(Dad,users_bagpack_1):
        print("Running Father test three:")
        Dad.create_gun(users_bagpack_1)
        if "Deagle" in users_bagpack_1:
            print("Passed!")
        else:
            print("Failed")

def father_test_four(Dad,users_bagpack_3,item):
        print("Running Father test four:")
        Dad.use_torch(users_bagpack_3,item)
        if users_bagpack_3:
            print("Failed!")
        else:
            print("Passed")

def father_test_five(Dad,gun_bagpack):
        print("Running Father test five:")
        Dad.use_pistol(gun_bagpack)
        if "Bullets" in gun_bagpack:
            print("Pass!")
        else:
            print("Fail")

def item_test_one(pieces,empty_bagpack):
    print("Running Item test one ")
    pieces.collect_item()
    if empty_bagpack:
        print("passed")
    else:
        print("fail")

def lore_test_one(story,lore_sto):
    print("Running Lore test one")
    story.lore_story()
    if story.lore_collection:
        print("Fail")
    else:
        print("pass")

def lore_test_two(Book,lore_none):
    print("Running Lore test one")
    Book.lore_play()
    if Book.lore_collection:
        print("Pass")
    else:
        print("Fail")




def main():

    users_bagpack_1 = ["Pistol", "Gunpowder", "Magazine"]
    item_main = ['Pistol', 'Magazine', 'Gunpowder']
    users_bagpack_2 = ['Battery']
    user_bp = ["Wooden stick", "Matches"]
    users_bagpack_3 = ["Torch"]
    empty_bagpack = []
    gun_bagpack = ["Deagle","Bullets"]
    item_list = ["Battery", "Matches", "Wooden stick", "Bullets", "Magazine", "Pistol", "Gunpowder"]
    demon = 1
    item = 3
    where_is_item = 3
    lore_sto = ['The father was in the forrest with his child.  ', 'He turned around to see where his child went,'
                                                               'as soon as he turned aorund, he saw a demon like '
                                                               'figure take his child and disappear',
            'Once he found his child, the demon was with her and asked him this question.',
            'The demon said "If you take my spot as the demon then your child will be set free, if not shes dies '
            'right here in front of you."']
    lore_none = []
    lore_collect = []

    Dad = Father()
    Book = Lore(lore_none)
    story = Lore(lore_sto)
    pieces = Item(item_list, empty_bagpack)

    father_test_one(Dad,users_bagpack_2,demon)
    father_test_two(Dad,user_bp)
    father_test_three(Dad,users_bagpack_1)
    father_test_four(Dad,users_bagpack_3,item)
    father_test_five(Dad,gun_bagpack)
    item_test_one(pieces,empty_bagpack)
    lore_test_one(story,lore_sto)
    lore_test_two(Book,lore_none)






if __name__ == "__main__":
    main()
    

    

    