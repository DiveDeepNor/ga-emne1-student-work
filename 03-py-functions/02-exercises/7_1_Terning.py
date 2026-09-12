import random
def roll_die (sides = 6):
    for i in range (1, 11, +1):
        number = random.randint(1, sides)
        print(number)

# kast tering med 6 sider
roll_die()

# kast tering med 20 sider
# roll_die(20)