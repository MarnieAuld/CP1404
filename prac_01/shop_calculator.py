"""
number_items = input(number of items)
    for i in range(1, number_items, 1)
    print(i, end=' ')
    item_price = input(price of item)
total price = calculate(item_price + item_price)
print("Total price for",number_items, " is ", total_price)
"""

total_price = 0
number_items = int(input("Number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))

for i in range(1, (number_items + 1), 1):
    print("Price of item", i, ":")
    item_price = float(input(""))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print("Total price for ", number_items, "items is: $", total_price)
