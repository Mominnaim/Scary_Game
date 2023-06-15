import time
import random


def play_game(items):
    # The three defined paths for the user to pick from
    paths = ["Path 1", "Path 2", "Path 3"]
    game_over = False
    users_bagpack = []
    loop_count = 0

    # While loop to repeat the selection of paths
    while not game_over:
        # The path the demon will be on - randomizes every round
        demon_path = random.choice(paths)

        # Randomly assign the item path
        item_paths = [path for path in paths if path != demon_path]
        item_path = random.choice(item_paths)
        prize_item = random.choice(items)

        first_Action = input("What would you like to do \nA) Create an item or \nB) pick a path\n =>")

        if first_Action.upper() == "A":
            print("Which item would you like to create? 1. or 2.\n")
            item_creating = int(input("1. Torch \n2. Flashlight =>"))

            if item_creating == 1:
                create_torch(users_bagpack)
            elif item_creating == 2:
                create_flashlight(users_bagpack)


        elif first_Action.upper() == "B":
            sec_option = input("What would you like to use an item (y/n)? \n")

            if sec_option == "y":
                specifics_item = input("Which item would you like to use \n")
                if specifics_item == "Torch" or specifics_item == "Flashlight":
                    print(f"You used the {specifics_item} to reveal the position of the demon.\n")
                    print(f"The demon is on {demon_path}.")
                else:
                    print("Invalid item! Please use either 'Torch' or 'Flashlight'.\n")


        # User picks their path
        print("Choose a path:")

        # Display the available paths
        for i, path in enumerate(paths):
            print(f"{i + 1}. {path}")

        # User picks their path
        loop_count += 1
        user_choice = int(input(f"\nTunnel #{loop_count} "
                                        f"Walk your path => "))
        print("\n")
        # If the user picks a path number that is not valid, they have to re-pick
        if user_choice < 1 or user_choice > 3:
            print("Invalid choice! Please enter a valid path number.")
            continue

        # Evaluate the chosen path
        chosen_path = paths[user_choice - 1]
        if chosen_path == demon_path:
            print("Oh no! You encountered the demon. Game over!\n")
            game_over = True
        elif chosen_path == item_path:
            print(f"You have survived and you found {prize_item}")
            users_bagpack.append(prize_item)
            print(f"You have {users_bagpack}\n")
        else:
            print("You have survived.\n")

    print("Thanks for playing!")


def create_torch(items):
    if "torch stick" in items and "matches" in items:
        print("Torch created!")
        # Remove the torch stick and matches from the inventory
        items.remove("torch stick")
        items.remove("matches")
        # Additional code to handle creating the torch
    else:
        print("You don't have all the required items to create a torch.")


def create_flashlight(items):
    if "battery" in items and "flashlight" in items:
        print("Flashlight created!")
        # Remove the battery and flashlight from the inventory
        items.remove("battery")
        items.remove("flashlight")

        # Additional code to handle creating the flashlight
    else:
        print("You don't have all the required items to create a flashlight.")


item_list = ["Battery", "Flashlight", "torch stick", "matches"]

play_game(item_list)