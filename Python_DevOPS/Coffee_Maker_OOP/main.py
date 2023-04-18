from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = 1
while machine_on != 0:
    choice = input(f"What would you like? {menu.get_items()}  ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = 0
        break
    else:
        choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
            else:
                money_machine.make_payment(choice.cost)
        else:
            coffee_maker.is_resource_sufficient(choice)

