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


# Import Libraries & Modules


# Declare Global Variables & Flags
MACHINE_STATUS = True   #True = On / False = Off
QUARTERS = 0.25
NICKLES = 0.1
PENNIES = 0.01
money = 0


# TODO: 1. Prompt User by asking "What would you like? (espresso/latte/cappuccino):
def order_selection():
    order = int(input("""\nWhat would you like? (espresso/latte/cappuccino)
                    1 : espresso
                    2 : latte
                    3 : cappuccino
                    4 : report
                    5 : off
                    6 : top-up
                  """))
    if order == 1:
        return 'espresso'
    elif order == 2:
        return 'latte'
    elif order == 3:
        return 'cappuccino'
    elif order == 4:
        return 'report'
    elif order == 5:
        return 'off'
    elif order == 6:
        return 'top-up'


# TODO: 2. Turn off the Coffee Machine by entering "off" to prompt
def off_machine():
    MACHINE_STATUS = False


# TODO: 3. Print Report
def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money}")


# TODO: 4. Check resources sufficient?
def check_resources(order):
    resources_required = MENU[order]['ingredients']
    for ingredient in resources_required:
        if int(resources[ingredient]) < int(resources_required[ingredient]):
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


# TODO: 5. Process coins
def process_coins(order):
    price_of_coffee = MENU[order]['cost']
    print(f"Price of {order} is ${round(price_of_coffee,2)}.")
    quarters = int(input("How many quarters?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = QUARTERS * quarters + NICKLES * nickles + PENNIES * pennies
    print(f"You have provided ${round(total,2)}.")
    if total >= price_of_coffee:
        global money
        money += price_of_coffee
        return round(total - price_of_coffee, 2)
    else:
        print("Sorry that's not enough money. Money refunded. Cancelling order...")
        return None

# TODO: 6. Check transaction successful


# TODO: 7. Make Coffee
def make_coffee(order):
    global resources
    resources_required = MENU[order]['ingredients']
    for ingredient in resources_required:
        resources[ingredient] -= resources_required[ingredient]
    print(f"Here is your {order} ☕ Enjoy!")


def top_up():
    global resources
    for item in resources:
        resources[item] += int(input(f"How much {item} is topped up?: "))


while MACHINE_STATUS:
    order = order_selection()
    if order == 'off':
        off_machine()
        print("Turning off...")
        exit()
    elif order == 'report':
        report()
    elif order == 'top-up':
        top_up()
    else:
        one_cup = check_resources(order)
        if one_cup:
            change = process_coins(order)
            if change is not None:
                print(f"Here is ${change} in change.")
                make_coffee(order)

