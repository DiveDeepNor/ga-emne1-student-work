def greet(name):
    print(f"Hello, {name}")

greet("Erna")
greet("Njaal")



def show_total(price, quantity):
    total = price * quantity
    print(f"Total: {total:.2f}")

# Parameters are number, no "or"
show_total(49.90,3)