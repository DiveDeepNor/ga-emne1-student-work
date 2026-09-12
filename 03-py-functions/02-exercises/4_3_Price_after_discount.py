def calculate_discounted_price(price, discount_percent):
    return price*(1-discount_percent/100)

print(calculate_discounted_price(100, 10))