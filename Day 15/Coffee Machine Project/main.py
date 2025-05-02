MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,         # { }
            "milk": 100,
            "coffee": 24,
        },
        "cost": 5.0,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 500,
}
profit=0

def add():
    global profit
    if profit >= 4.0:
        resources["water"] += 300
        resources["milk"] += 200
        resources["coffee"] += 100
        profit -= 4.0
        print("\nThe Resources has refilled in Machine.")
    else:
        print(f"\nSorry You need $4 and you only have ${profit}")


def report():
    print(f"\nWater : {resources["water"]} ml.")
    print(f"Milk : {resources["milk"]} ml.")
    print(f"Coffee : {resources["coffee"]} gm.")
    print(f"Profit : ${profit}")


def payment():
    global profit
    print(f"\nYou Ordered {coffee_} coffe☕.")
    print(f"Bill: ${MENU[coffee_]["cost"]}")
    print("\nPlease Insert coins.")
    quarter = int(input("\n  Quarter How much?($0.50) : "))
    dimes = int(input("\n  Dimes How much?($0.40) : "))
    nickels = int(input("\n  Nickels How much?($0.20) : "))
    pennies = int(input("\n  Pennies How much?($0.10) : "))
    bill = round((0.50 * quarter) + (0.40 * dimes) + (0.20 * nickels) + (0.10 * pennies),2)
    print(f"\nAmount Paid: ${bill}")
    if bill >= MENU[coffee_]["cost"]:
        change = round(bill - MENU[coffee_]["cost"], 2)
        profit += round((bill - change),2)
        if change > 0:
            print(f"\nHere is your Change ${change}")
        print(f"\nEnjoy Your {coffee_} coffee☕")
        if coffee_ == "espresso":
            resources["water"] -= MENU[coffee_]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_]["ingredients"]["coffee"]
        else:
            resources["water"] -= MENU[coffee_]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee_]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee_]["ingredients"]["coffee"]
    else:
        print(f"\nSorry! You  have {bill} amount to pay is {MENU[coffee_]["cost"]}")


def selected_coffee(coffee):
    order_in = MENU[coffee]["ingredients"]
    for item in order_in:
        if order_in[item] > resources[item]:
            print(f"The {item} is not available.")
            exit()
    payment()


machine_on = True

while machine_on:
    coffee_ = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_ == "espresso":
        selected_coffee(coffee_)
    elif coffee_ == "latte":
        selected_coffee(coffee_)
    elif coffee_ == "cappuccino":
        selected_coffee(coffee_)
    elif coffee_ == "report":
        report()
    elif coffee_ == "add":
        add()
    else:
        machine_on = False
