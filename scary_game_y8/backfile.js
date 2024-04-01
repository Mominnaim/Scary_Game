// Defining the global variables
const battery = "battery";
const deagle = "deagle";
const matches = "matches";
const bullets = "bullets";
const magazine = "magazine";
const pistol = "pistol";


// This is the Evil demon class 
class Evil_demon {

    // This is if the user picks the demon path, game lost
    getDeath() {
        console.log("You have died")
        process.exit(1)
    }

    //This is if the user picked the gun option and ends up picking the demon path, Game won
    getKillDemon() {
        console.log("You have shot the demon and killed him. Congrats you got back you daughter")
        process.exit(0)
    }

    // If the user picks the gun option and does not pick the demon path
    getMissedDemon() {
        console.log("You have shot but missed the demon.")
    }
}

// This is the item class where all the items come from 
class Item {
    // There are two object in this class which are the items in the game, and the user backpack
    constructor(items_list, users_backpack) {
        this.items_list = items_list;
        this.users_backpack = users_backpack;
    }

    // if the user picks the the item path then this method will randomly select an item in the items_list
    getItem() {
        // Generate a random index to select a random element from the items_list array
        const randomIndex = Math.floor(Math.random() * this.items_list.length);

        // Get the random item from the items_list array
        const prizeItem = this.items_list[randomIndex];

        // Just adds the item in the backpack
        console.log(`You have survived and you have found ${prizeItem}`)
        this.users_backpack.push(prizeItem)
        this.users_backpack.sort()

        // Since it wouldnt make sense to collect multiple of the same gun parts, it will delete the item once collected
        if ([magazine, pistol].includes(prizeItem)) {
            // Remove prize_item from items_list
            const index = this.items_list.indexOf(prizeItem);
            if (index !== -1) {
                this.items_list.splice(index, 1);
            }
        }
    }

}


// This is the father class
class Father {

    // Since the father is the one that wears the backpack, the method useItem will be used here.
    // Depending on what the user picks, it will use that item, and then delete it afterwards
    useItem(backpack, demon, item, pick) {
        if (pick === "1") {
            if (backpack.includes(battery)) {
                console.log(`The demon is on path: ${demon}.`)
                const index = backpack.indexOf(battery);
                if (index !== -1) {
                    backpack.splice(index, 1);
                } else {
                    console.log("You do not have any batteries left to use")
                }
            }
        } else if (pick === "2") {
            if (backpack.includes(matches)) {
                console.log(`The item is on ${item}`)
                const index = backpack.indexOf(matches);
                if (index !== -1) {
                    backpack.splice(index, 1);
                } else {
                    console.log("Sorry you do not have this item")
                }
            } 
        } else if (pick === "3") {
            if (backpack.includes(deagle) && (backpack.includes(bullets))) {
                console.log("You need to pick the path where the demon is at")
                const index = backpack.indexOf(bullets);
                if (index !== -1) {
                    backpack.splice(index, 1);
                }
            } else if (backpack.includes(deagle) && (!backpack.includes(bullets))) {
                console.log("You do not any bullets to shoot")
            } else if (!backpack.includes(deagle) && (backpack.includes(bullets))) {
                console.log("You do not have a deagle to shoot with")
                }
            }
        }


    // The creation of the gun.
    create_gun(backpack) {
        const mags = backpack.indexOf(magazine)
        const gun = backpack.indexOf(pistol)
        if ((mags !== -1) && (gun !== -1)) {
            backpack.splice(gun,1)
            backpack.splice(mags,1)
            backpack.push(deagle)
        }

        
    }
}

// This is a function that brings in all the path from the button 
function bringInPath() {

    // This takes all the button from the .game-container and pushes it to buttonsID
    var buttons = document.querySelectorAll('.game-container button');
    var buttonIds = [];

    buttons.forEach(function(button) {
        buttonIds.push(button.id);
    });

    return buttonIds

}


var survivalCounter = 0; // Variable to keep track of survival counter

        function updateSurvived() {
            survivalCounter++; // Increment the survival count
            document.getElementById('survived').textContent = survivalCounter; // update the span content
        }


// The Game_engine class
class Game_engine {
    // Constructor is a special method to define the objects within an class. In this case the objects in this Game engine are Demon, Item, Father, and paths.
    // One of which we pass in, which is the item object, the other three are created.
    constructor(item,paths) {
        this.demon = new Evil_demon();
        this.item = item;
        this.father = new Father();
        this.paths = paths;
    }

    play() {

        // This is the loop of the game, and keeps track of the rounds.
        let loopCount = 0;

        // Create the loop of the game
        while (true) {

            // guns = 0 means that we have not created the deagle for us to kill the demon.
            let guns = 0;
        
            // This sets each object in different paths each loop.
        
            //Math.random picks a number from 0 to 1, then * by 3 (3 paths), then rounds down to the nearest whole number.
            const demonPath = this.paths[Math.floor(Math.random() * this.paths.length)];
        
            //This code filters out the path that has the demon in it, and multiple it by 2 and round down
            const itemPaths = this.paths.filter(path => path !== demonPath)[Math.floor(Math.random() * 2)];
        
            // This filters out all the paths that has been taken and assigns the last remaining path to safepath
            const safePath = this.paths.filter(path => path !== demonPath && path !== itemPaths)[0];

            this.handlepathSelection= pathID => {
                if (pathID === demonPath) {
                    this.demon.getDeath();
                } else if (pathID === itemPaths) {
                    this.item.getItem();
                } else if (pathID === safePath) {
                    console.log('You are safe');
                }
            }


        
        }
    }
}

// The initial backpack and items
const theBackpack = [battery, matches, bullets, magazine, pistol];
const allItems = [bullets, magazine, pistol, matches, battery];

// Creating an instance of the Item class
const stuff = new Item(allItems, theBackpack);
const theWay = bringInPath()

const start = new Game_engine(stuff,theWay)
document.addEventListener('DOMContentLoaded', () => {
    start.play();
})

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }


  function buttonClick(pathId) {
    
    // Call a method on the start object based on the pathId
    start.handlepathSelection(pathId);
}

  