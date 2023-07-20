import random

from skeleton_scary_game import Father
from skeleton_scary_game import Item
from skeleton_scary_game import Lore
"""
users_bagpack_1 = ["Pistol", "Gunpowder", "Magazine"]
item_main = ['Pistol', 'Magazine', 'Gunpowder']
users_bagpack_2 = ['Battery']
users_bagpack_3 = ["Torch"]
empty_bagpack = []
item_list = ["Battery", "Matches", "Wooden stick", "Bullets", "Magazine", "Pistol", "Gunpowder"]
demon = 1
where_is_item = 3
lore_sto = ['The father was in the forrest with his child.  ', 'He turned around to see where his child went,'
                                                               'as soon as he turned aorund, he saw a demon like '
                                                               'figure take his child and disappear',
            'Once he found his child, the demon was with her and asked him this question.',
            'The demon said "If you take my spot as the demon then your child will be set free, if not shes dies '
            'right here in front of you."']
lore_none = []
lore_collect = []
# If the user picks this path then they will find out who the demon was, and how he became that way.

Dad = Father()
Book = Lore(lore_none)
story = Lore(lore_sto)
pieces = Item(item_list, empty_bagpack)


user_input = input(str("Pick a class to test\n1. --> Father\n2. --> Item\n3. --> Lore\n"))

if user_input == "1":
    father_user_input = input(str("Pick a function to test\n1. --> use_item\n2. --> create_torch\n3. --> create_gun"
                                  "\n4. --> use_torch\n5. --> use_pistol\n"))
    if father_user_input == "1":
        print("I passed in a Battery in the bagpack, and the demon path -- This should work.\n")
        Dad.use_item(users_bagpack_2,demon)
        if users_bagpack_2:
            print(users_bagpack_2)
        else:
            print("Works and the Baterry is removed!!!\n")
    elif father_user_input == "2":
        print("This bagpack does not have a requirements to make a torch --> it should Fail Successfully\n")
        Dad.create_torch(users_bagpack_2)
        if "Torch" in users_bagpack_2:
            print("It doesn't work!")
        else:
            print("Fail Successfully!!\n")
    elif father_user_input == "3":
        print("This bagpack does have everything to make the gun --> I can shoot the demon\n")
        Dad.create_gun(users_bagpack_1, item_list)
        if "Deagle" in users_bagpack_1:
            print("I can shoot that demon\n")
            print(item_main)
            print(users_bagpack_1)
        else:
            print(users_bagpack_1)
    elif father_user_input == "4":
        print("This bagpack does have a torch --> It should remove and print an empty list\n")
        Dad.use_torch(users_bagpack_3,where_is_item)
        if users_bagpack_3:
            print("Doesnt work")
        else:
            print("Works and the torch is removed")
            print(users_bagpack_3, "\n")
    elif father_user_input == "5":
        pass
elif user_input == "2":
    print("Passed in a empty list --> should have something after the execution (random Item).\n")
    pieces.collect_item()
    if empty_bagpack:
        print("It works and Item has been added")
        print(empty_bagpack, "\n")
    else:
        print("Doesn't work")
elif user_input == "3":
    lore_user_input = input(str("Pick a function from the lore class\n1. --> lore_story\n2. --> lore_play\n"))
    if lore_user_input == "1":
        print("Passed in a list with 0-4 --> after the execution there should be 0-3 --> it works")
        story.lore_story()
        if story.lore_size() == 3:
            print("It works, one piece was removed and now there is one less.\n")
        else:
            print("Nope")
    elif lore_user_input == "2":
        print("We have a different object for this lore class that has no lore pieces.\n")
        if Book.lore_play():
            print("There is something here, dont know how")
        else:
            print("There is nothing here, and that is how it should be. WORKS!!\n")

"""

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
        Dad.use_item(users_bagpack_1)
        if "Deagle" in users_bagpack_1
            print("Passed!")
        else:
            print("Failed")

def father_test_four(Dad,users_bagpack_3,item):
        print("Running Father test four:")
        Dad.use_item(users_bagpack_2,item)
        if users_bagpack_3:
            print("Failed!")
        else:
            print("Passed")

def father_test_five(Dad,gun_bagpack):
        print("Running Father test five:")
        Dad.use_item(users_bagpack_2,item)
        if "Bullets" in gun_bagpack:
            print("Pass!")
        else:
            print("Fail")

def item_test_one(Pieces,empty_bagpack):
    print("Running Item test one ")
    pieces.collect_item()
    if empty_bagpack:
        print("passed")
    else:
        print("fail")

def lore_test_one(story,lore_sto):
    print("Running Lore test one")
    story.lore_story()
    if lore_collection:
        print("Fail")
    else:
        print("pass")

def lore_test_two(Book,lore_none):
    print("Running Lore test one")
    book.lore_play()
    if lore_collection:
        print("Pass")
    else:
        print("Fail")




def main():

    users_bagpack_1 = ["Pistol", "Gunpowder", "Magazine"]
    item_main = ['Pistol', 'Magazine', 'Gunpowder']
    users_bagpack_2 = ['Battery"]
    user_bp
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
# If the user picks this path then they will find out who the demon was, and how he became that way.

    Dad = Father()
    Book = Lore(lore_none)
    story = Lore(lore_sto)
    pieces = Item(item_list, empty_bagpack)

    father_test_one(Dad,users_bagpack_2,demon)
    father_test_two(Dad,user_bp)
    father_test_three(Dad,users_bagpack_1)
    father_test_four(Dad,users_bagpack_3,item)
    father_test_five(Dad,gun_bagpack)
    item_test_one(Pieces,empty_bagpack)
    lore_test_one(story,lore_sto)
    lore_test_two(Book,lore_none)






if __name__ == "__main__":
    main()
    

    

    