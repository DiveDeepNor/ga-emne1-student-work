import math

def calculate_hypotenuse(side_a, side_b):
    kat1 = side_a ** 2
    kat2 = side_b ** 2
    return math.sqrt(kat1 + kat2)

print(calculate_hypotenuse(3, 4))