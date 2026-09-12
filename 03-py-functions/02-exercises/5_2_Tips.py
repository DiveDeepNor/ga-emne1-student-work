def calculate_tip(amount, tip_percent = 0):
    return amount/100*tip_percent

print(calculate_tip(200, 10))
print(calculate_tip(123))