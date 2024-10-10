import sys

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
}

# Barista function checks if we have enough resources to make chosen drink
def barista(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Cashier function evaluates if enough money was given for chosen drink
def cashier(user_input):
    chosen_drink = user_input
    quarter = int(input("How many quarters?:"))
    dime = int(input("How many dime?:"))
    nickle = int(input("How many nickle?:"))
    penny = int(input("How many pennies?:"))

    total_given = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    if total_given > MENU[user_input]["cost"]:
        change = total_given - MENU[user_input]["cost"]
        print(f"Here is ${change} in change. Here is your {user_input}. Enjoy!")
        return

    else:
        print("That's not enough money, sorry! Money refunded.")
        return

while True:
    user_input = input("What would you like? espresso/latte/cappuccino:").lower()
    if user_input == "off":
        print("Shutting down the program...")
        sys.exit()

    # I had them all as separate IF branches, but should change to elif
    if user_input == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    elif resources["water"] or resources["milk"] or resources["coffee"] == 0:
        print("We're sold out, sorry! Come back another time.")

    else: