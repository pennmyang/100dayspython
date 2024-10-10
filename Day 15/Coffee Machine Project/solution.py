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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# NOTE I Was confused where order_ingredients came from. You don't need to declare/create a thing for it to be able to be used as an argument.
# order_ingredients is not declared globally, but it is dynamically passed to functions like is_resource_sufficient() and make_coffee() at runtime.
# These functions expect the ingredients dictionary to be passed in, and this happens when you call them with drink["ingredients"] based on the user's drink choice.

def is_resource_sufficient(order_ingredients): # you get Milk: ... Coffee: ... Water: ...
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients: # so when you iterate over the 3 keys of chosen drink
        if order_ingredients[item] > resources[item]: # you do the same for resources as they share same name
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# note: the solution code would still work even if the keys in the MENU and resources dictionaries were in a different order. The order of keys in Python dictionaries does not matter when accessing or manipulating data because dictionaries are unordered collections in Python.
# note: the word item in for loop is just a placeholder variable name, and you can absolutely use any other valid variable name

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2) # Note - I forgot to round
        print(f"Here is ${change} in change.")
        global profit # NOTE! I didn't declare a global profit variable.
        # indicate that the function needs to modify the global variable profit, rather than creating a new local variable with the same name.
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients: # same logic as is_resource_sufficient() function, you can loop through both dictionaries
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice] # this retrieves the details of the selected drink, listing Ingredients: Milk, Coffee, Water... Cost:
        if is_resource_sufficient(drink["ingredients"]): # thus when you retrieve "Ingredients" key here, you get "Milk, Coffee, Water"
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    # note they have 4 functions, I only had 2.
    # 1. is_resource_sufficient(drink["ingredients"])) -> takes in order_ingredients, returns T/F whether enough resources
    # 2. process_coins() -> no arguments, contains input prompts for quarters/dimes, returns the total calculated from coins inserted
    # 3. is_transaction_successful(payment, drink["cost"]): -> takes in 2 arguments (money_received, drink_cost) and returns T/F whether user give enough $
    # 4. make_coffee(choice, drink["ingredients"]) -> Deduct the required ingredients from the resources, no return







