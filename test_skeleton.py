import random

from .skeleton_scary_game import Father,Item,Lore


item_list = ["Battery", "Matches", "Wooden stick", "Bullets", "Magazine", "Pistol", "Gunpowder"]
lore_sto = ['The father was in the forrest with his child.  ', 'He turned around to see where his child went,'
                                                               'as soon as he turned aorund, he saw a demon like '
                                                               'figure take his child and disappear',
            'Once he found his child, the demon was with her and asked him this question.',
            'The demon said "If you take my spot as the demon then your child will be set free, if not shes dies '
            'right here in front of you."']
lore_none = []
battery = "Battery"
torch = "Torch"
deagle = "Deagle"
matches = "Matches"
woodenstick = "Wooden stick"
bullets = "Bullets"
magazine = "Magazine"
pistol ="Pistol"
gunpowder = "Gunpowder"


def test_father_one():
    Dad = Father()
    users_bagpack_2 = ["Battery"]
    demon = 1
    Dad.use_item(users_bagpack_2,demon)
    assert len(users_bagpack_2) == 0


def test_father_two():
    Dad = Father()
    user_bp = [woodenstick,matches]
    Dad.create_torch(user_bp)
    assert torch in user_bp


def test_father_three():
    Dad = Father()
    users_bagpack_1 = [pistol,magazine,gunpowder]
    Dad.create_gun(users_bagpack_1)
    assert deagle in users_bagpack_1

def test_father_four():
    Dad = Father()
    users_bagpack_3 = [torch]
    item = 3
    Dad.use_torch(users_bagpack_3,item)
    assert len(users_bagpack_3) == 0


def test_father_five():
    Dad = Father()
    gun_bagpack = [bullets, deagle]
    Dad.use_pistol(gun_bagpack)
    assert len(gun_bagpack) == 1

def test_item_one():
    empty_bagpack = []
    pieces = Item(item_list, empty_bagpack)
    pieces.collect_item()
    assert len(empty_bagpack) == 1


def test_lore_one():
    story = Lore(lore_sto)
    story.lore_story()
    assert len(story.lore_collection) == 1


def test_lore_two():
    Book = Lore(lore_none)
    Book.lore_play()
    assert Book.lore_collection


    