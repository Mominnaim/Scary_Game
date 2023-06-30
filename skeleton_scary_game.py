import time
import random

# This is where the actual game will run from
class game_engine(object):

    # This is the constructer method, this is what will be passed to the play() for the game to run
    def __init__(self,demon,item,father):
        self.demon = demon
        self.item = item
        self.father = father
        self.paths = ["Path 1", "Path 2", "Path 3"]    
    
    # This is the actual game where everything will run
    def play(self,):

        # how many rounds you have survived,
        loop_count = 0

        # Loop until 7 rounds have been reach and you win, the game is on a finite condition.
        while loop_count < 7:

            # The path the demon will be on - randomizes every round
            demon_path = random.choice(self.paths)


            # Randomly assign the item path
            item_paths = [path for path in self.paths if path != demon_path]
            item_path = random.choice(item_paths)

            #Ask the user if they want to use their flashlight to see where the demon is.
            need_help = input(str("Would you like to use your flashlight? (y/n) -> "))

            # If the user picks an option that is not y or n, they have to repick.
            if need_help.lower() != "y" and need_help.lower() != "n":
                print("Pick yes or no")
                continue


            # If the user picks 'y' and they have a battery, it will call the father class and execute the use_item function. -> brings in users_bagpack from the item class and demon_path
            # This is because the 'father' needs to check if he has batteries or not, and if he does, the demon path will be known. This will be executed in the father class.
            if need_help.lower() == "y":
                if "Battery" in item.users_bagpack:
                    self.father.use_item(self.item.users_bagpack,demon_path)
                else:
                    print("You don't have any batteries \n")
                    pass
            elif need_help.lower() == "n":
                pass

            # Display the available paths
            for i, path in enumerate(self.paths):
                print(f"{i + 1}. {path}\n")
            
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

            # If the user picks this path, then it will call the demon class
            if chosen_path == demon_path:
                self.demon.death()
            
            # If the user picks this path it will call the item class.
            elif chosen_path == item_path:
                self.item.collect_item()
            
            # If the user picks this path then nothing happens but just run the loop again.
            else:
                print("You have survived.\n")
            
        # Once the user has survived 7 rounds then they win the game and get their daugther back.
        if loop_count >= 7:
            print("The demon said thank you for playing and returned your child")
            exit(0)

# The father class, and the only thing this class can do is use and item.
class father(object):
    
    # This is where the item is acutally used and then removed after the usage.
    def use_item(self,bagpack,demon):
        print(f"The demon is on {demon}. \n")
        bagpack.remove("Battery")


# This is the evil demon object, and it will be sent to the game_engine 
class evil_demon(object):
    
    #If  the user picks this path, the user dies 
    def death(self):
        print("The demon ate you for dinner and let your child go back home parentless.")
        exit(1)
    

# This is the item object, and will be sent to the game engine as well.
class item(object):

    # These are the variables that are in this class. and will only be in this class.
    items_list = ["Battery"]
    users_bagpack = ["Battery"]

    # If the user picks this path, the user collects the item and will be sent to his bagpack
    def collect_item(self):
        prize_item = random.choice(self.items_list)
        print(f"You have survived and you have found => {prize_item}")
        self.users_bagpack.append(prize_item)
        print(f"You have {self.users_bagpack} \n")

        return self.users_bagpack

# This is the lore object, and will be sent to the game engine also.
class lore(object):

    # If the user picks this path then they will find out who the demon was, and how he became that way.
    def lore_story(self):
        pass

# instanciating all the classes to objects
a = evil_demon()
b = item()
c = father()
d = lore()

# calling the actual game with the given parameters
start = game_engine(a,b,c)
start.play()
