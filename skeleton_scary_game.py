import time
import random

# This is where the actual game will run from
class game_engine(object):


    def __init__(self,demon,item,father):
        self.demon = demon
        self.item = item
        self.father = father
        self.paths = ["Path 1", "Path 2", "Path 3"]    
    
    
    def play(self,):

        loop_count = 0

        while loop_count < 7:

            # The path the demon will be on - randomizes every round
            demon_path = random.choice(self.paths)


            # Randomly assign the item path
            item_paths = [path for path in self.paths if path != demon_path]
            item_path = random.choice(item_paths)

            # Display the available paths
            for i, path in enumerate(self.paths):
                print(f"{i + 1}. {path}\n")

            
            need_help = input("Would you like to use an item? (y/n)")

            # If the user picks a path number that is not valid, they have to re-pick
            if need_help.lower() == "y" or need_help.lower() == "n":
                print("Pick yes or no")
                continue

            if need_help.lower() == "y":
                self.father.use_item()
            elif need_help.lower() == "n"
                pass
            
            # User picks their path
            loop_count += 1
            user_choice = int(input(f"Tunnel #{loop_count} "
                                            f"Walk your path => "))


            # If the user picks a path number that is not valid, they have to re-pick
            if user_choice < 1 or user_choice > 3:
                print("Invalid choice! Please enter a valid path number.")
                continue

            # Evaluate the chosen path
            chosen_path = self.paths[user_choice - 1]
            if chosen_path == demon_path:
                self.demon.death()
            elif chosen_path == item_path:
                self.item.collect_item()
            else:
                print("You have survived.")
            

        if loop_count >= 7:
            print("The demon said thank you for playing and returned your child")
            exit(0)

#this will be the user playing the game 
class father(object):
    
    # The user will have the option to use an item if they desire too
    def use_item(self):
        if ""


# This is the evil demon object, and it will be sent to the game_engine 
class evil_demon(object):
    
    #If  the user picks this path, the user dies 
    def death(self):
        print("The demon ate you for dinner and let your child go back home parentless.")
        exit(1)
    

# This is the item object, and will be sent to the game engine as well.
class item(object):

    items_list = ["Battery"]
    users_bagpack = ["Battery"]

    # If the user picks this path, the user collects the item and will be sent to his bagpack
    def collect_item(self):
        prize_item = random.choice(self.items_list)
        print(f"You have survived and you have found => {prize_item}")
        self.users_bagpack.append(prize_item)
        print(f"You have {self.users_bagpack}")

    return users_bagpack

# This is the lore object, and will be sent to the game engine also.
class lore(object):

    # If the user picks this path then they will find out who the demon was, and how he became that way.
    def lore_story(self):
        pass

a = evil_demon()
b = item()
c = father()
d = lore()


start = game_engine(a,b,c)
start.play()


