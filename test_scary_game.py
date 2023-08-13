
from .scary_game import Father, Item

item_list = ["Battery", "Matches", "Wooden stick", "Bullets", "Magazine", "Pistol", "Gunpowder"]

lore_none = []
battery = "Battery"
deagle = "Deagle"
matches = "Matches"
bullets = "Bullets"
magazine = "Magazine"
pistol = "Pistol"
gunpowder = "Gunpowder"


def test_father_one():
    Dad = Father()
    users_bagpack_2 = ["Battery"]
    demon = 1
    Dad.use_item(users_bagpack_2, demon)
    assert len(users_bagpack_2) == 0


def test_father_two():
    Dad = Father()
    users_bagpack_3 = [matches]
    item = 3
    Dad.use_fire_lamp(users_bagpack_3, item)
    assert len(users_bagpack_3) == 0


def test_father_three():
    Dad = Father()
    gun_bagpack = [bullets, deagle]
    Dad.use_pistol(gun_bagpack)
    assert len(gun_bagpack) == 1


def test_father_four():
    dad = Father()
    backpack = [magazine, pistol]
    dad.create_gun(backpack)
    assert len(backpack) == 1


def test_item_one():
    empty_bagpack = []
    pieces = Item(item_list, empty_bagpack)
    pieces.collect_item()
    assert len(empty_bagpack) == 1
