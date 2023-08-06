import random
import time
"""
print("Narrator: The father and his daughter are on vacation in a log cabin in the forrest. ")
time.sleep(1)
print("Daddy: Would you like to go on a late night walk and clear our mind?")
time.sleep(1)
print("Sheena: yes daddy, the weather is really nice too!")
time.sleep(1)
print("Daddy: Make sure you don't leave my side ok, and do not let go of my hand.")
time.sleep(1)
print("Sheena: Yes daddy, I will make sure to never leave your sight! Now can we go dad!")
time.sleep(1)
print("Narrator: They set off for a walk not knowing that this might be their last.")
"""

battery = "Battery"
fire_lamp = "Lamp"
deagle = "Deagle"
matches = "Matches"
bullets = "Bullets"
magazine = "Magazine"
pistol = "Pistol"


# This is where the actual game will run from
class Game_engine(object):

    # This is the constructor method, this is what will be passed to the play() for the game to run
    def __init__(self, demon, item, father, ):
        self.demon = demon
        self.item = item
        self.father = father
        self.paths = ["Path 1", "Path 2", "Path 3"]

        # This is the actual game where everything will run

    def play(self):

        # how many rounds you have survived,
        loop_count = 0

        while True:

            # This will be used later if the user has a gun or not.
            guns_or_noguns = 0

            # The path the demon will be on - randomizes every round
            demon_path = random.choice(self.paths)

            # Randomly assign the item path
            item_paths = random.choice([path for path in self.paths if path != demon_path])

            # This is where the lore is
            lore_path = random.choice([path for path in self.paths if (path != demon_path and path not in item_paths)])

            # The user can craft an item if they have all the required parts for it. If they click y the they will be
            # prompted to pick what item they want to craft. If the user picks n then it will just display their
            # current backpack.
            while True:

                # Ask the user if they want to craft an item.
                need_help = input(str(
                    "\nIf you need to see the crafting manual, press (h) \nWould you like to craft an item? (y/n)\n=> "))

                # If the user picks an option that is not y or n, they have to repick.
                try:
                    if need_help.lower() != "y" and need_help.lower() != "n" and need_help.lower() != "h":
                        raise ValueError("Invalid input. Please pick 'y', 'n', or 'h'.")
                except ValueError as e:
                    print(str(e))
                    continue

                if need_help.lower() == 'h':
                    print(
                        "\nFlashlight -> You already have a flashlight, you just need to collect [Batteries] to use "
                        "it = Reveals the demon path\n")
                    print("Fire lamp -> You need [Matches] & [Wooden stick] = reveals what path the item is on\n")
                    print(
                        "Deagle -> You need [Pistol] & [Magazine] = You can kill the demon but only if "
                        "you have [Bullets]\n")
                elif need_help.lower() == "y":
                    print("\nPick an item you would like to craft.")
                    pick_an_item = input(str("1.----->   Fire Lamp \n2.----->   Pistol \n==> "))
                    print()
                    if pick_an_item == "1":
                        self.father.create_fire_lamp(self.item.users_backpack)
                        break
                    elif pick_an_item == "2":
                        self.father.create_gun(self.item.users_backpack)
                        break
                    else:
                        print("You did not pick one of the options given!")
                elif need_help.lower() == "n":
                    self.item.users_backpack.sort()
                    print("You have these items on your backpack:", self.item.users_backpack)
                    print()
                    break

            # The user will be asked if they would like to use an item, if they pick y then they will choose what item,
            # If they pick n then they will n, it will continue on with the game.
            try:
                use_an_item = input(str("\nWould you like to use an Item (y/n) => "))
                if use_an_item.lower() != 'y' and use_an_item.lower() != 'n':
                    raise ValueError("PLEASE ENTER y or n!")
            except ValueError as d:
                print(str(d))
                continue

            # User input on what item they would like to use, and from there call in the function of the father class.
            if use_an_item == 'y':
                print("\nWhich Item would you like to use?\n1. ---> Flashlight\n2. ---> Fire lamp\n3. ---> Gun")
                item_usage = input(str("==> "))
                print()
                if item_usage == "1":
                    self.father.use_item(self.item.users_backpack, demon_path)
                elif item_usage == "2":
                    self.father.use_fire_lamp(self.item.users_backpack, item_paths)
                elif item_usage == "3":
                    if "Deagle" in self.item.users_backpack and "Bullets" in self.item.users_backpack:
                        self.father.use_pistol(self.item.users_backpack)
                        guns_or_noguns = 1
                    else:
                        print("You do not have all the gun parts")
                else:
                    print("That is not an option.\n")

            # Display the available paths
            for i, path in enumerate(self.paths):
                print(f"{i + 1}. {path}\n")

            # User picks their path
            loop_count += 1

            # This if will run if the user did not use the gun to kill the demon
            if guns_or_noguns == 0:
                print("Be careful and choose the right path\n")
                while True:
                    try:

                        # If the user picks a path number that is not valid, they have to re-pick
                        user_choice = int(input(f"Round #{loop_count} "
                                                f"Choose your path => "))
                        if user_choice < 1 or user_choice > 3:
                            raise ValueError(f" There is no {user_choice}, please pick a valid path! \n")
                        break
                    except ValueError as e:
                        print(str(e))

                # Evaluate the chosen path
                chosen_path = self.paths[user_choice - 1]

                # If the user picks this path, then it will call the demon class
                if chosen_path == demon_path:
                    self.demon.death()

                # If the user picks this path it will call the item class.
                elif chosen_path == item_paths:
                    self.item.collect_item()


                # If the user picks this path then nothing happens but just run the loop again.
                elif chosen_path == lore_path:
                    print("You have survived!\nand also collected a battery")
                    self.item.users_backpack.append("Battery")

            # This if will run if the user does have a gun to kill the demon.
            if guns_or_noguns == 1:
                print("You have a loaded Deagle, aim wisely!\n")
                while True:
                    try:
                        # If the user picks a path number that is not valid, they have to re-pick
                        user_choice = int(input(f"Tunnel #{loop_count} "
                                                f"Walk your path => "))
                        if user_choice < 1 or user_choice > 3:
                            raise ValueError(f" There is no {user_choice}, please pick a valid path! \n")
                        break
                    except ValueError as e:
                        print(str(e))

                # Evaluate the chosen path
                chosen_path = self.paths[user_choice - 1]

                # If the user picks this path, then it will call the demon class
                if chosen_path == demon_path:
                    self.demon.kill_demon()

                # If the user picks this path it will call the item class.
                elif chosen_path == item_paths:
                    self.item.collect_item()
                    self.demon.missed_demon()

                # If the user picks this path then nothing happens but just run the loop again.
                elif chosen_path == lore_path:
                    print("You have survived!\nand also collected a battery")
                    self.item.users_backpack.append(battery)
                    self.demon.missed_demon()


class Father(object):
    """
    This class is the father class and essentially the user can reveal the position of the demon
    IF they have batteries.

    """

    # This is where the item is acutally used and then removed after the usage.
    def use_item(self, backpack, demon):
        if "Battery" in backpack:
            print(f"The demon is on {demon}. ")
            backpack.remove("Battery")
        else:
            print("You do not have any batteries left to use.\n")

    # This is where the Fire lamp is created
    def create_fire_lamp(self, backpack):
        if matches in backpack:
            print("Fire lamp created!")
            # Remove the Fire lamp stick and matches from the inventory
            backpack.remove(matches)
            backpack.append(fire_lamp)
            backpack.sort()
            # Additional code to handle creating the Fire lamp
        else:
            print("You don't have all the required items to create a Fire lamp.")

    # This is where the gun is created, and once created the parts of the gun get removed from the list.
    def create_gun(self, backpack):
        if pistol in backpack and magazine in backpack:
            print("You have a gun. Ready to kill the demon, and get your daughter back?")
            print("Now that you have a Deagle, you will only have to collect the bullets. Don't miss!")
            # This are the items being removed from the backpack
            backpack.remove(magazine)
            backpack.remove(pistol)

            # The user gains a item since he had all the required parts
            backpack.append(deagle)
            backpack.sort()

        else:
            print("You don't have all the parts yet")

    # This is where you can use the Fire lamp
    def use_fire_lamp(self, backpack, item_path):
        if "Lamp" in backpack:
            print(f"The item is on {item_path}. \n")
            backpack.remove(fire_lamp)
        else:
            print("You do not have a fire lamp\n")

    # This is where you can use the pistol.
    def use_pistol(self, backpack):
        if "Deagle" in backpack and "Bullets" in backpack:
            print("You need to pick the path with the demon and you will kill him and get your daughter back\n")
            backpack.remove("Bullets")
        else:
            print("You do not have all the ")


# This is the evil demon object, and it will be sent to the game_engine
class Evil_demon(object):
    """
    This class is the demon class and really you just die if you encounter the demon.
    """

    # If  the user picks this path, the user dies
    def death(self):
        print("The demon ate you for dinner and let your child go back home parentless.")
        exit(1)

    def kill_demon(self):
        print("You have killed the demon")
        print("Daughter: DADDY you saved me, I knew you would come rescue me!!")
        exit(0)

    def missed_demon(self):
        print("You shot but missed the demon. You will have to find another bullet and try again.")


# This is the item object, and will be sent to the game engine as well.
class Item(object):
    """
    This is the item class where the item list and the user backpack is intialized and if
    you walk the item path then you collect that item. Once the item has been used then it gets removed.
    """

    # These are the variables that are in this class. and will only be in this class.
    def __init__(self, items_list, users_backpack):
        self.items_list = items_list
        self.users_backpack = users_backpack

    # If the user picks this path, the user collects the item and will be sent to his backpack
    def collect_item(self):
        prize_item = random.choice(self.items_list)
        print(f"You have survived and you have found => {prize_item}")
        self.users_backpack.append(str(prize_item))
        self.users_backpack.sort()
        print(f"You have {self.users_backpack} \n")

        # The user should not collect the same gun parts twice. It is a one and done thing
        if prize_item in [magazine, pistol]:
            self.items_list.remove(prize_item)


# instanciating all the classes to objects

def main():
    # instanciating all the classes to objects
    Anunnaki = Evil_demon()
    Ali = Father()

    This_the_backpack = [battery, matches, battery, deagle]
    This_the_backpack.sort()
    this_are_the_items = [battery, matches, bullets, magazine, pistol]
    stuff = Item(this_are_the_items, This_the_backpack)

    # calling the actual game with the given parameters
    start = Game_engine(Anunnaki, stuff, Ali)
    start.play()


if __name__ == "__main__":
    main()
