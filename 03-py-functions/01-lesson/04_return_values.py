def calculate_total(price, quantity):
    total = price * quantity
    return total

order_total = calculate_total(149.50, 3)
print(f"The total is: {order_total:.2f}")
