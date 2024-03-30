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

            // Another loop incase the user decides to enter something they are not supposed to.
            while (true) {

                // This checks to see if the user has a magazine and a pistol, and if they do then they will a gun will be created automatically
                if (this.item.users_backpack.includes(magazine) && this.item.users_backpack.includes(pistol)) {
                    this.father.create_gun(this.item.users_backpack);
                    const deletePistol = this.item.items_list.indexOf(pistol);
                    const deleteMagazine = this.item.items_list.indexOf(magazine);

                    // The two lines up above are basically saying that if there is a pistol or Mag found then it will have the index position assigned to it.
                    // If there is nothing found then it will be -1 and so the if statement below will not run.
                    if ((deletePistol !== -1) && (deleteMagazine !== -1)) {

                        // (deletePistol,1) --> Is saying that deleted the first instance of pistol.
                        this.item.items_list.splice(deletePistol,1);
                        this.item.items_list.splice(deleteMagazine,1);
                    }
                }

                // This is for the user to know what they have in their backpack
                console.log(`You have ${this.item.users_backpack}`);

                // The user has to enter in an input 
                const useAnItem = readlineSync.question("Would you like to use an Item (y/n) or type (h) for item usage info\n => ").toLowerCase();

                // If the user selects Y then they come here.
                if (useAnItem === 'y') {
                    console.log("\nWhich Item would you like to use?\n1. ---> Flashlight\n2. ---> Fire lamp\n3. ---> Gun");
                    const itemUsage = readlineSync.question("==> ");

                    // If the user enters one or two they will come here and then get sent to the father class, specifically the useItem method
                    if (itemUsage === "1" || itemUsage === "2") {
                        this.father.useItem(this.item.users_backpack, demonPath, itemPaths, itemUsage);
                        break;
                    
                    // If the user enters 3 then it will go here
                    } else if (itemUsage === "3") {
                        if (this.item.users_backpack.includes(deagle) && this.item.users_backpack.includes(bullets)) {
                            this.father.useItem(this.item.users_backpack, demonPath, itemPaths, itemUsage);
                            // The user picked the use gun option, so now the rounds will change where if the demon path is picked then the demon dies and the use wins the game 
                            guns = 1;
                            break;
                        } else {
                            break;
                        }

                    // In case the user picks something that is not a option
                    } else {
                        console.log("That is not an option.\n");
                    }

                // If the user needs help with what is going on.
                } else if (useAnItem === "h") {
                    console.log("\nFlashlight -> You need 'Batteries' to use the flashlight and it reveals the demon path\n" +
                                "Fire lamp -> You need 'Matches' to light the fire lamp and it reveals the item path\n" +
                                "Gun -> You need a 'Magazine' & 'Pistol' but need 'Bullets' to actually use the gun, you have the " +
                                "ability to kill the demon and win the game.\n");

                // If the user does not want to pick anything
                } else if (useAnItem === "n") {
                    console.log(`These are the items you have in your backpack ${this.item.users_backpack}\n`);
                    break;

                // Again if the user types something they are not supposed to.
                } else {
                    console.log("PLEASE ENTER y, n ,h!");
                }
            }


        
    
            // This is the starting of the game, where the user will acutally pick the path
            console.log("Walk your Path:");

            // This is a for loop where it will display each path.
            this.paths.forEach((path, index) => console.log(`${index + 1}. ${path}\n`));

            // This will add 1 to loopCount for every loop
            loopCount++;

            // This is if the user did not pick the number 3 the gun
            if (guns === 0) {
                console.log("Be careful and choose the right path\n");
                while (true) {

                    // Counts the loop 
                    const userChoice = readlineSync.questionInt(`Round #${loopCount} Choose your path => `);

                    if (userChoice >= 1 && userChoice <= 3) {
                        const chosenPath = this.paths[userChoice - 1];

                        // if the demon path is chosen then the user dies
                        if (chosenPath === demonPath) {
                            this.demon.getDeath();

                        // If the itemPath is chosen then user gets an item
                        } else if (chosenPath === itemPaths) {
                            this.item.getItem();

                        // If the safePath is chosen then math.random will pick a number from 0 - 1 and if it is greater than .5 then matches will be assigned otherwise battery.
                        } else if (chosenPath === safePath) {
                            const safeItem = Math.random() < 0.5 ? matches : battery;
                            this.item.users_backpack.push(safeItem);
                            console.log(`You have survived!\nand also collected a ${safeItem}`);
                        }
                        break;
                    } else {
                        console.log(`There is no ${userChoice}, please pick a valid path!`);
                    }
                }
            


            // This is if the user does pick number 3, and so they have a chance to kill the demon.
            } else if (guns === 1) {
                console.log("You have a loaded Deagle, aim wisely!\n");
                while (true) {
                    const userChoice = readlineSync.questionInt(`Tunnel #${loopCount} Walk your path => `);

                    
                    if (userChoice >= 1 && userChoice <= 3) {
                        const chosenPath = this.paths[userChoice - 1];

                        // If the demon path gets picked, then the user wins
                        if (chosenPath === demonPath) {
                            this.demon.getKillDemon();

                        // If the itempath gets picked, it will print you have missed, but you will get an item
                        } else if (chosenPath === itemPaths) {
                            this.item.getItem();
                            this.demon.getMissedDemon();

                        // Same thing here as the one up above
                        } else if (chosenPath === safePath) {
                            const safeItem = Math.random() < 0.5 ? matches : battery;
                            this.item.users_backpack.push(safeItem);
                            console.log(`You have survived!\nand also collected a ${safeItem} but,`);
                            this.demon.getMissedDemon();
                        }
                        break;
                    } else {
                        console.log('oof')
                    }
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