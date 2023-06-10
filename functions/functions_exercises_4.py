unit_price=float(input("Unit price: "))
qty_units=int(input("Number of units: "))

def function(price, qty):
    return f"${price * qty}"

total_cost = function(unit_price, qty_units)

print(total_cost)