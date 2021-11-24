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


def makeCoffee(name):
    if name == 'espresso':
        resources['water'] -= MENU[name]['ingredients']['water']
        resources['coffee'] -= MENU[name]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[name]['ingredients']['water']
        resources['milk'] -= MENU[name]['ingredients']['milk']
        resources['coffee'] -= MENU[name]['ingredients']['coffee']


def getCost(name):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    totalPaid = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    if totalPaid < MENU[name]['cost']:
        print("Sorry that's not enough money. Money refunded.")

    elif name == 'espresso':
        makeCoffee(name)
        print(f"Here is { round( totalPaid - MENU[name]['cost'], 2) } in change\n"
              f"Here is your {name}☕. Enjoy!")
        resources['money'] += MENU[name]['cost']

    elif name == 'latte':
        makeCoffee(name)
        print(f"Here is { round( totalPaid - MENU[name]['cost'], 2) } in change\n"
              f"Here is your {name}☕. Enjoy!")
        resources['money'] += MENU[name]['cost']

    elif name == 'cappuccino':
        makeCoffee(name)
        print(f"Here is { round( totalPaid - MENU[name]['cost'], 2) } in change\n"
              f"Here is your {name}☕. Enjoy!")
        resources['money'] += MENU[name]['cost']


def getOrder(ch):
    if ch == 'espresso':
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and \
                resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            getCost('espresso')
        else:
            if resources['water'] < MENU['espresso']['ingredients']['water']:
                print("Sorry there is not enough water")
            elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                print("Sorry there is not enough coffee")

    elif ch == 'latte':
        if resources['water'] >= MENU['latte']['ingredients']['water'] and \
                resources['milk'] >= MENU['latte']['ingredients']['milk'] and \
                resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            getCost('latte')
        else:
            if resources['water'] < MENU['latte']['ingredients']['water']:
                print("Sorry there is not enough water")
            elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                print("Sorry there is not enough coffee")
            elif resources['milk'] < MENU['latte']['ingredients']['milk']:
                print("Sorry there is not enough milk")

    elif ch == 'cappuccino':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and \
                resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and \
                resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            getCost('cappuccino')
        else:
            if resources['water'] < MENU['cappuccino']['ingredients']['water']:
                print("Sorry there is not enough water")
            elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                print("Sorry there is not enough coffee")
            elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
                print("Sorry there is not enough milk")

    else:
        print("Invalid Choice")

machineOn = True

while machineOn:
    choice = input(f"What would you like? ({[k for k, v in MENU.items()][0]}/{[k for k, v in MENU.items()][1]}/"
                   f"{[k for k, v in MENU.items()][2]}): ").lower()
    if choice == 'off':
        machineOn = False

    elif choice == 'report':
        print(f"Water: {resources['water']}\n"
              f"Milk: {resources['milk']}\n"
              f"Coffee: {resources['coffee']}\n"
              f"Money: ${resources['money']}")
    else:
        getOrder(choice)