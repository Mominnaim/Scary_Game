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
        prize_item = random.choice(this.items_list)
        console.log(`You have survived and you have found ${prize_item}`)
        this.users_backpack.push(str(prize_item))
        this.users_backpack.sort()

        if (["Magazine", "Pistol"].includes(prize_item)) {
            // Remove prize_item from items_list
            const index = items_list.indexOf(prize_item);
            if (index !== -1) {
                items_list.splice(index, 1);
            }
        }
    }

}

class Father {

    useItem(backpack, demon, item, pick) {
        if (pick === "1") {
            if (backpack.includes("battery")) {
                console.log(`The demon is on path: ${demon}.`)
                const index = backpack.indexOf('battery');
                if (index !== -1) {
                    backpack.splice(index, 1);
                } else {
                    console.log("You do not have any batteries left to use")
                }
        } else if (pick === "2") {
            if (backpack.includes("matches")) {
                console.log(`The item is on ${item}`)
                const index = backpack.indexOf('matches');
                if (index !== -1) {
                    backpack.splice(index, 1);
                } else {
                    console.log("Sorry you do not have this item")
                }
            } 
        } else if (pick === "3") {
            if (backpack.includes("deagle") && (backpack.includes("bullets"))) {
                console.log("You need to pick the path where the demon is at")
                const index = backpack.indexOf('bullets');
                if (index !== -1) {
                    backpack.splice(index, 1);
                }
            } else if (backpack.includes("deagle") && (!backpack.includes("bullets"))) {
                console.log("You do not any bullets to shoot")
            } else if (!backpack.includes("deagle") && (backpack.includes("bullets"))) {
                console.log("You do not have a deagle to shoot with")
                }
            }
        }
    }

    create_gun(backpack) {
        const magazine = backpack.indexOf('magazine')
        if (magazine !== -1){
            backpack.splice(magazine,1);
        }
        const pistol = backpack.indexOf('pistol')
            if (pistol !== -1){
                backpack.splice(pistol,1)
            }
        }

}
