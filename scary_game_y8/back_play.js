// Importing required modules
const readlineSync = require('readline-sync');

// The narrative phrase
const phraseOne = `NARRATOR: The father and his daughter are on vacation in a log cabin in the forest.
DADDY: Would you like to go on a late night walk and clear our mind?
SHEENA: Yes DADDY, the weather is really nice too!
DADDY: Make sure you don't leave my side ok, and do not let go of my hand.
SHEENA: Yes DADDY, I will make sure to never leave your sight! Now can we go dad!
NARRATOR: They set off for a walk not knowing that this might be their last.
NARRATOR: On the walk they go. While on the walk the father looks behind to see if her daughter is there,
but what he sees terrifies him.
Monster: I have your daughter, and the only way to get her back, is to play my little game!`;

// Prompting the user to skip the cutscene
const skip = readlineSync.question("Would you like to skip the cutscene? (y/n)\n=> ");


// Checking user input
if (skip === "n") {
    bufferPrint(phraseOne);
}

// Defining the global variables
const battery = "battery";
const deagle = "deagle";
const matches = "matches";
const bullets = "bullets";
const magazine = "magazine";
const pistol = "pistol";

// The Game_engine class
class Game_engine {
    constructor(item) {
        this.demon = new Evil_demon();
        this.item = item;
        this.father = new Father();
        this.paths = ["Path 1", "Path 2", "Path 3"];
    }

    play() {
        let loopCount = 0;

        while (true) {
            let guns = 0;
            const demonPath = this.paths[Math.floor(Math.random() * this.paths.length)];
            const itemPaths = this.paths.filter(path => path !== demonPath)[Math.floor(Math.random() * 2)];
            const safePath = this.paths.filter(path => path !== demonPath && path !== itemPaths)[0];

            while (true) {

                if (this.item.users_backpack.includes(magazine) && this.item.users_backpack.includes(pistol)) {
                    this.father.create_gun(this.item.users_backpack);
                    const deletePistol = this.item.items_list.indexOf(pistol);
                    const deleteMagazine = this.item.items_list.indexOf(magazine);
                    if ((deletePistol !== -1) && (deleteMagazine !== -1)) {
                        this.item.items_list.splice(deletePistol,1);
                        this.item.items_list.splice(deleteMagazine,1);
                    }
                }

                console.log(`You have ${this.item.users_backpack}`);

                const useAnItem = readlineSync.question("Would you like to use an Item (y/n) or type (h) for item usage info\n => ").toLowerCase();

                if (useAnItem === 'y') {
                    console.log("\nWhich Item would you like to use?\n1. ---> Flashlight\n2. ---> Fire lamp\n3. ---> Gun");
                    const itemUsage = readlineSync.question("==> ");

                    if (itemUsage === "1" || itemUsage === "2") {
                        this.father.useItem(this.item.users_backpack, demonPath, itemPaths, itemUsage);
                        break;
                    } else if (itemUsage === "3") {
                        this.father.useItem(this.item.users_backpack, demonPath, itemPaths, itemUsage);
                        if (this.item.users_backpack.includes(deagle) && this.item.users_backpack.includes(bullets)) {
                            let guns = 1;
                        break;
                        }
                    } else {
                        console.log("That is not an option.\n");
                    }
                } else if (useAnItem === "h") {
                    console.log("\nFlashlight -> You need 'Batteries' to use the flashlight and it reveals the demon path\n" +
                                "Fire lamp -> You need 'Matches' to light the fire lamp and it reveals the item path\n" +
                                "Gun -> You need a 'Magazine' & 'Pistol' but need 'Bullets' to actually use the gun, you have the " +
                                "ability to kill the demon and win the game.\n");
                } else if (useAnItem === "n") {
                    console.log(`These are the items you have in your backpack ${this.item.users_backpack}\n`);
                    break;
                } else {
                    console.log("PLEASE ENTER y, n ,h!");
                }
            }


        
    

            console.log("Available paths:");
            this.paths.forEach((path, index) => console.log(`${index + 1}. ${path}\n`));

            loopCount++;

            if (guns === 0) {
                console.log("Be careful and choose the right path\n");
                while (true) {
                    const userChoice = readlineSync.questionInt(`Round #${loopCount} Choose your path => `);

                    if (userChoice >= 1 && userChoice <= 3) {
                        const chosenPath = this.paths[userChoice - 1];

                        if (chosenPath === demonPath) {
                            this.demon.getDeath();
                        } else if (chosenPath === itemPaths) {
                            this.item.getItem();
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
            }

            if (guns === 1) {
                console.log("You have a loaded Deagle, aim wisely!\n");
                while (true) {
                    const userChoice = readlineSync.questionInt(`Tunnel #${loopCount} Walk your path => `);

                    if (userChoice >= 1 && userChoice <= 3) {
                        const chosenPath = this.paths[userChoice - 1];

                        if (chosenPath === demonPath) {
                            this.demon.getKillDemon();
                        } else if (chosenPath === itemPaths) {
                            this.item.getItem();
                            this.demon.getMissedDemon();
                        } else if (chosenPath === safePath) {
                            const safeItem = Math.random() < 0.5 ? matches : battery;
                            this.item.users_backpack.push(safeItem);
                            console.log(`You have survived!\nand also collected a ${safeItem}`);
                            this.demon.getMissedDemon();
                        }
                        break;
                    } else {
                        console.log('oof')
                    }
                }
            }
            console.log(this.item)
        }
    }
}


class Evil_demon {

    getDeath() {
        console.log("You have died")
        process.exit(1)
    }

    getKillDemon() {
        console.log("You have shot the demon and killed him. Congrats you got back you daughter")
        process.exit(0)
    }

    getMissedDemon() {
        console.log("You have shot but missed the demon.")
    }
}

class Item {
    constructor(items_list, users_backpack) {
        this.items_list = items_list;
        this.users_backpack = users_backpack;
    }

    getItem() {
        // Generate a random index to select a random element from the items_list array
        const randomIndex = Math.floor(Math.random() * this.items_list.length);

        // Get the random item from the items_list array
        const prizeItem = this.items_list[randomIndex];

        console.log(`You have survived and you have found ${prizeItem}`)
        this.users_backpack.push(prizeItem)
        this.users_backpack.sort()

        if ([magazine, pistol].includes(prizeItem)) {
            // Remove prize_item from items_list
            const index = this.items_list.indexOf(prizeItem);
            if (index !== -1) {
                this.items_list.splice(index, 1);
            }
        }
    }

}

class Father {

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

// The initial backpack and items
const theBackpack = [battery, matches, bullets, magazine, pistol];
const allItems = [bullets, magazine, pistol, matches, battery];

// Creating an instance of the Item class
const stuff = new Item(allItems, theBackpack);

// Creating an instance of the Game_engine class with the given parameters
const start = new Game_engine(stuff);
start.play();


// Function for printing a phrase with a buffer
function bufferPrint(phrase) {
    for (const char of phrase) {
        process.stdout.write(char);
        // To flush the output immediately
        process.stdout.clearLine();
        process.stdout.cursorTo(0);
        // Sleep for 50 milliseconds
        setTimeout(() => {}, 50);
    }
}
