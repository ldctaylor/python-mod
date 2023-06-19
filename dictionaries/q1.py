#The dictionary below represents the cost of individual items in a supermarket. Write a program that asks the user how many of each item they would like in turn, and outputs the total cost of their groceries.

groceries = {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Coffee": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

total = 0
for _ in groceries.keys():
    qty = float(input(f"Please enter the quantity of {_}: "))
    total = total + (qty * groceries[_])

print(f"Your total cost is ${total}")
