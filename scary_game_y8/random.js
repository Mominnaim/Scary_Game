function whatPath(userChoice, demonPath, itemPaths, safePath, gunNumber) {
    if (gunNumber === 0) {
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
        }
    } else if (gunNumber === 1){
        console.log("You have a loaded Deagle, aim wisely!\n");
    
        //const userChoice = readlineSync.questionInt(`Tunnel #${loopCount} Walk your path => `);
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

        }
    }
  }


  // Iterate over the collection of elements
  for (let i = 0; i < buttons.length; i++) {
    const buttonClickPromise = new Promise((resolve, reject ) => {
        const button = buttons[i].querySelector('button'); // Get the button element inside each game_button div
        // Add an event listener to each button
        button.addEventListener('click', () => {
            // Call your function with the desired arguments
            whatPath(button.id, demonPath, itemPaths, safePath,guns);
            resolve('yes')

        });

    })

    const result = await buttonClickPromise
    console.log(result)
    
}