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

test_list = [magazine]


def test_father_one():
    Dad = Father()
    users_bagpack_2 = ["Battery"]
    users_bagpack_3 = ["Matches"]
    users_bagpack_4 = [deagle, bullets]
    demon = 1
    item = 2
    Dad.use_item(users_bagpack_2, demon, item, "1")
    Dad.use_item(users_bagpack_3, demon, item, "2")
    Dad.use_item(users_bagpack_4, demon, item, "3")
    assert len(users_bagpack_2) == 0
    assert len(users_bagpack_3) == 0
    assert len(users_bagpack_4) == 1


def test_father_two():
    dad = Father()
    backpack = [magazine, pistol]
    dad.create_gun(backpack)
    assert len(backpack) == 1


def test_item_one():
    empty_bagpack = []
    pieces = Item(item_list, empty_bagpack)
    pieces.collect_item()
    assert len(empty_bagpack) == 1

def test_item_two():
    empty_bagpack = []
    pieces = Item(test_list, empty_bagpack)
    pieces.collect_item()
    assert magazine not in test_list


