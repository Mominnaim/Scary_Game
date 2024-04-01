function onDocumentLoaded() {
    var buttons = document.querySelectorAll('.game-container button');
    var buttonIds = [];

    buttons.forEach(function(button) {
        buttonIds.push(button.id);
    });

    demonPath = buttonIds[Math.floor(Math.random() * buttonIds.length)];
    itemPaths = buttonIds.filter(path => path !== demonPath)[Math.floor(Math.random() * 2)];
    safePath = buttonIds.filter(path => path !== demonPath && path !== itemPaths)[0];

    const path_to_class = new StoredVariable(demonPath, itemPaths, safePath, buttonIds);
    path_to_class.printPath();

}

document.addEventListener('DOMContentLoaded', onDocumentLoaded);


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

    console.log('I am here')

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