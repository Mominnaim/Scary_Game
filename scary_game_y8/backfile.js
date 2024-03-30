



var demonPath;
var itemPaths;
var safePath;

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
// The Evil_demon object
const monster = new Evil_demon()

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


var survivalCounter = 0; // Variable to keep track of survival counter

        function updateSurvived() {
            survivalCounter++; // Increment the survival count
            document.getElementById('survived').textContent = survivalCounter; // update the span content
        }

class StoredVariable {
    constructor(demonPath,itemPaths,safePath,buttonIds) {
        this.demonPath = demonPath
        this.itemPaths = itemPaths
        this.safePath = safePath
        this.buttonIds = buttonIds
    }

    printPath() {
        console.log(`${this.demonPath} this is the demon Path`)
        console.log(`${this.itemPaths} This is the item Path`)
        console.log(`${this.safePath} THis is the safe path`)
    }
}

function buttonClick(path) {
    if (demonPath === path) {
        document.getElementById('type-of-path').textContent = 'demon';
        monster.getDeath()
    } else if (itemPaths === path) {
        document.getElementById('type-of-path').textContent = 'item';
    } else if (safePath === path){
        document.getElementById('type-of-path').textContent = 'safe';
    }

}

document.addEventListener('DOMContentLoaded', onDocumentLoaded);

