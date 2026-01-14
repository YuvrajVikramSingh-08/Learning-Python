from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

serve = True
while serve:
    choice = input("Which coffee would you like?(espresso/latte/cappuccino): ")
    if choice == "off":
        serve = False
        print("Bye!")
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        order = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(order):
            if moneymachine.make_payment(order.cost):
                coffeemaker.make_coffee(order)