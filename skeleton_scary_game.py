import random

# This is where the actual game will run from
class Game_engine(object):

    # This is the constructer method, this is what will be passed to the play() for the game to run
    def __init__(self,demon,item,father,lore):
        self.demon = demon
        self.item = item
        self.father = father
        self.paths = ["Path 1", "Path 2", "Path 3"]
        self.lore = lore    
    
    # This is the actual game where everything will run
    def play(self):

        # how many rounds you have survived,
        loop_count = 0

        # Loop until 7 rounds have been reach and you win, the game is on a finite condition.
        while True:

            # The path the demon will be on - randomizes every round
            demon_path = random.choice(self.paths)
            

            # Randomly assign the item path
            item_paths = [path for path in self.paths if path != demon_path]
            item_path = random.choice(item_paths)
    
            # This is where the lore is
            lore_paths = [path for path in self.paths if (path != demon_path and path not in item_path)]
            lore_path = random.choice(lore_paths)
            
            

            #Ask the user if they want to craft an item.
            need_help = input(str("Would you like to craft an item? (y/n) -> "))


            # If the user picks an option that is not y or n, they have to repick.
            try:
                if need_help.lower() != "y" and need_help.lower() != "n":
                    raise ValueError("Invalid input. Please pick 'y' or 'n'.")
            except ValueError as e:
                print(str(e))
                continue


            # If the user picks 'y' and they have a battery, it will call the father class and execute the use_item function. -> brings in users_bagpack from the item class and demon_path
            # This is because the 'father' needs to check if he has batteries or not, and if he does, the demon path will be known. This will be executed in the father class.
            if need_help.lower() == "y":
                print("Pick an item you would like to craft.")
                pick_an_item = input(str("1.----->   Torch \n2.----->   Pistol \n==> "))
            elif need_help.lower() == "n":
                print("You have these items on your bagpack:", self.item.users_bagpack)

            # Display the available paths
            for i, path in enumerate(self.paths):
                print(f"{i + 1}. {path}\n")
            
            # User picks their path
            loop_count += 1


            # If the user picks a path number that is not valid, they have to re-pick
            while True:
                try:
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
                self.demon.death()
            
            # If the user picks this path it will call the item class.
            elif chosen_path == item_path:
                self.item.collect_item()
            
            # If the user picks this path then nothing happens but just run the loop again.
            elif chosen_path == lore_path:
                self.lore.lore_play()
            
        # Once the user has survived 7 rounds then they win the game and get their daugther back.
        if loop_count >= 7:
            print("The demon said thank you for playing and returned your child")

class Father(object):

    """
    This class is the father class and essentially the user can reveal the position of the demon
    IF they have batteries.

    """
    
    # This is where the item is acutally used and then removed after the usage.
    def use_item(self,bagpack,demon):
        print(f"The demon is on {demon}. \n")
        bagpack.remove("Battery")

    def create_torch(self,items):
        if "Wooden stick" in items and "Matches" in items:
            print("Torch created!")
            # Remove the torch stick and matches from the inventory
            items.remove("torch stick")
            items.remove("matches")
            items.append("Torch")
            # Additional code to handle creating the torch
        else:
            print("You don't have all the required items to create a torch.")

    def create_gun(self,items):
        if "Pistol" in items and "Bullets" in items and "Magazine" in items:
            print("You have a gun. Ready to kill the demon, and get your daughter back?")
            items.remove("Bullets")
            items.remove("Magazine")
            items.remove("Pistol")
            items.append("Loaded Pistol")
        else:
            print("You don't have all the parts yet")

    def use_torch(self,bagpack,demon):
        print(f"The demon is on {demon}. \n")
        bagpack.remove("Torch")

    def use_pistol(self,bagpack):
        pass

# This is the evil demon object, and it will be sent to the game_engine 
class Evil_demon(object):

    """
    This class is the demon class and really you just die if you encounter the demon.
    """
    
    #If  the user picks this path, the user dies 
    def death(self):
        print("The demon ate you for dinner and let your child go back home parentless.")
        exit(1)
    

# This is the item object, and will be sent to the game engine as well.
class Item(object):
    
    """
    This is the item class where the item list and the user bagpack is intialized and if
    you walk the item path then you collect that item. Once the item has been used then it gets removed.
    """

    # These are the variables that are in this class. and will only be in this class.
    def __init__(self):
        self.items_list = ["Battery","Matches","Wooden stick","Bullets","Magazine","Pistol"]
        self.users_bagpack = []

    # If the user picks this path, the user collects the item and will be sent to his bagpack
    def collect_item(self):
        prize_item = random.choice(self.items_list)
        print(f"You have survived and you have found => {prize_item}")
        self.users_bagpack.append(prize_item)
        print(f"You have {self.users_bagpack} \n")

        return self.users_bagpack

# This is the lore object, and will be sent to the game engine also.
class Lore(object):

    """
    This is the lore class and essentially if you walk the lore path then you find a piece of info of who 
    the demon was and how he became that way.

    """

    lore_collection = []

    def __init__(self):
        self.lorelist = ['The father was in the forrest with his child.  ','He turned around to see where his child went,'
        'as soon as he turned aorund, he saw a demon like figure take his child and disappear', 'Once he found his child, the demon was with her and asked him this question.',
        'The demon said "If you take my spot as the demon then your child will be set free, if not shes dies right here in front of you."']
    # If the user picks this path then they will find out who the demon was, and how he became that way.
    def lore_story(self):
        lore_piece = random.choice(self.lorelist)
        self.lore_collection.append(lore_piece)
        print(lore_piece, '\n')
        print('Your current lore collection: ' , self.lore_collection)
        self.lorelist.remove(lore_piece)

    def lore_play(self):
        if self.lorelist:
            self.lore_story()
        else:
            print("You have found all the pieces to the lore. Now put them in order to understand the story.")

# instanciating all the classes to objects
Anunnaki = Evil_demon()
stuff = Item()
Ali = Father()
The_story = Lore()

# calling the actual game with the given parameters
start = Game_engine(Anunnaki,stuff,Ali,The_story)
start.play()


# Need to create test for the game -- use if statements. ------> 
# What are the new things you are going to add to this game.------> 
