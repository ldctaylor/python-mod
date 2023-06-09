groceries = [
    ["baby spinach", 2.78],
    ["hot chocolate",3.70],
    ["BBQ Shapes",9.00],
    ["Bread",2.10],
    ["Carrots",0.56],
    ["Oranges",3.08]
]
total = 0

for product in groceries:
    qty = int(input(f"Please enter the quantity for {product[0]}: "))
    total = round(total + (qty * float(product[1])),2)

print(f"Thankyou, your total is ${total}")