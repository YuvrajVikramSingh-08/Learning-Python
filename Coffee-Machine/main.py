from ascii import coffee_art
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

def resource_check(coffee_type):
    enough_resource = True
    insufficient_resources = []
    ingredients = MENU[coffee_type]["ingredients"]
    for i in ingredients:
        if resources[i] < ingredients[i]:
            insufficient_resources.append(i)
    if len(insufficient_resources) != 0:
        print(f"Sorry not enough resources. Add {insufficient_resources}")
        enough_resource = False
    return enough_resource

def process_coin(coffee_type):
    enough_balance = True
    coffee_cost = MENU[coffee_type]["cost"]
    quart = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    user_money = quart * 0.25 + dimes * 0.10 + nickel * 0.05 + penny * 0.01
    if user_money < coffee_cost:
        print("Insufficient money!")
        print(f"Here is your ${user_money}.")
        enough_balance = False
    else:
        print(f"Here is your ${user_money - coffee_cost} in change.")
        resources["money"] += coffee_cost
    return enough_balance

def make_coffee(coffee_choice):
    if resource_check(coffee_choice):
        if process_coin(coffee_choice):
            print(f"Here is your {coffee_choice.title()}. Enjoy! :)")
            ingredients = MENU[coffee_choice]["ingredients"]
            for i in ingredients:
                resources[i] -= ingredients[i]
    else:
        print("Sorry for the Inconvenience.")

print(coffee_art)

serve = True
while serve:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"Money : ${resources['money']}")
    elif choice == "off":
        serve = False
        print("Bye Bye")
    elif choice in MENU:
        make_coffee(coffee_choice=choice)
    else:
        print("Invalid Choices")