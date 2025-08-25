due = 50

coins = [25,10,5]

paid = 0

while due > 0:
    print(f"Amount Duo: {due}")
    coin = int(input("Insert Coin: "))

    if coin in coins:
        due = due - coin
        paid = paid + coin

if paid >= due:
    print(f"Change Owed: {paid-50}")