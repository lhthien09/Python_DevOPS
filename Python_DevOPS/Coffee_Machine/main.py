import data

MENU = data.MENU
resources = data.resources

machine_on = 1
money = 0


def raport():
    global resources, money
    for thing in resources:
        print(f"{thing}: {resources[thing]} ml/g")
    print(f"Money: ${money}")


def insert_coins():
    penny = int(input("How many pennies? "))
    nickel = int(input("How many nickels? "))
    dime = int(input("How many dimes? "))
    quarter = int(input("How many quarters? "))
    total = 0.01 * penny + 0.05 * nickel + 0.1 * dime + 0.25 * quarter
    return total


def check_resources(selection):
    wat = MENU[selection]["ingredients"]["water"]
    cof = MENU[selection]["ingredients"]["coffee"]
    milk = MENU[selection]["ingredients"]["milk"]
    arr = {"water": wat, "coffee": cof, "milk": milk}
    x = True
    for item in arr:
        if resources[item] < arr[item]:
            print(f"Sorry, there is not enough {item}.")
            x = False
    return x


def machine_on():
    global MENU, resources, money
    choices = input("What would you like? ☕(espresso/latte/cappuccino): ")

    if choices == "report":
        raport()
        machine_on()
    else:
        if check_resources(choices):
            total = insert_coins()
            if total >= MENU[choices]["cost"]:
                money += MENU[choices]["cost"]
                arr = ["water", "milk", "coffee"]
                for item in arr:
                    resources[item] -= MENU[choices]["ingredients"][item]

                print(f"Here is ${total - MENU[choices]['cost']} in change.")
                print(f"Here is your ☕ {choices}! Enjoy!")
                machine_on()
            else:
                print("Sorry that's not enough money. Money refunded.")
                machine_on()
        else:
            machine_on()

    if choices == 'off':
        return

machine_on()
