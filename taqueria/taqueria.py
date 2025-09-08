price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price_user = 0
while True:
    try:
        item = input("Item: ").title().strip()
        price_user = price_user + price[item]
        print(f"Total: ${price_user :.2f}")
    except (KeyboardInterrupt, EOFError):
        pass
    except KeyError:
        pass