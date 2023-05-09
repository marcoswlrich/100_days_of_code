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
    },
}
profit = 0
resources = {"water": 300, "milk": 200, "coffe": 100}


def is_resource_sufficient(order_ingredients):
    """Retorna True quando o pedido pode ser feito, False se os ingredientes são insuficientes."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Desculpe, não é o suficiente {item}.")
            return False
    return True


def process_coins():
    """Retorna o total calculado a partir das moedas inseridas."""
    print("Por favor, insira moedas.")
    total = int(input("Quantos quarters?: ")) * 0.25
    total += int(input("Quantos dimes?: ")) * 0.1
    total += int(input("Quantos nickles?: ")) * 0.05
    total += int(input("Qauntos pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Retorne True quando o pagamento for aceito, ou False se o dinheiro for insuficiente."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui está ${change} o troco.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Desculpe, isso não é dinheiro suficiente. Dinheiro devolvido.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduz os ingredientes necessários dos recursos."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está seu {drink_name} ☕️. Aproveite!")


is_on = True

while is_on:
    choice = input("O que você gostaria? (expresso/café com leite/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Água: {resources['water']}ml")
        print(f"Leite: {resources['milk']}ml")
        print(f"Café: {resources['coffee']}g")
        print(f"Lucro: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
