# This is where the actual game will run from
class game_engine(object):

    # This is the specific location. We will need to pass in three things for Four different paths. [demon,item,lore,father]
    def path(self):
        pass

#this will be the user playing the game 
class father(self):
    
    # The user will have the option to use an item if they desire too
    def use_item(self):
        pass

    #The user has to pick a path from one to three.
    def choose_path(self):
        pass

# This is the evil demon object, and it will be sent to the game_engine 
class evil_demon(self):
    
    #If  the user picks this path, the user dies 
    def death(self):
        pass

# This is the item object, and will be sent to the game engine as well.
class item(self):

    # If the user picks this path, the user collects the item and will be sent to his bagpack
    def collect_item(self):
        pass

# This is the lore object, and will be sent to the game engine also.
class lore(self):

    # If the user picks this path then they will find out who the demon was, and how he became that way.
    def lore_story(self):
        pass

