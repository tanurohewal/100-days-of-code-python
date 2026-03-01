MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {resources['money']}")

    elif choice in MENU:
        ingredients = MENU[choice]["ingredients"]
        for item in ingredients:
            if ingredients[item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                break

        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_money = quarters + dimes + nickles + pennies

            cost = MENU[choice]["cost"]

            if total_money < cost:
                print("Sorry that's not enough money. Money refunded.")

            else:
                change = round(total_money - cost, 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                resources["money"] += cost

                for item in ingredients:
                    resources[item] -= ingredients[item]
                print(f"Here is your {choice}. Enjoy!")