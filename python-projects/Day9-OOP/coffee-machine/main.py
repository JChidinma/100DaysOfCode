from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


money_machine.report()
coffee_maker.report()

is_on = True
while is_on:
    options = menu.get_items()
    drink_choice = input(f"What would you like to drink? ({options}): \n")

    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_type = menu.find_drink(drink_choice)
        print(coffee_type)
        if coffee_maker.is_resource_sufficient(coffee_type) and money_machine.make_payment(coffee_type.cost):
            coffee_maker.make_coffee(coffee_type)
