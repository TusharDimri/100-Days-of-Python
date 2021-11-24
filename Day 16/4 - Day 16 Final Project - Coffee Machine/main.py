from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
# print(MENU.menu)
isWorking = True

while isWorking:
    ch = input(f"What would you like? ({MENU.get_items()}\b): ").lower()

    if ch == 'off':
        isWorking = False

    elif ch == 'report':
        coffee_machine.report()
        money.report()

    else:
        drink = MENU.find_drink(ch)
        if drink and coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
