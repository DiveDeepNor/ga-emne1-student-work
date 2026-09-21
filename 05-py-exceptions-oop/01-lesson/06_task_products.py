class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}: {self.price:.2f}")

apple = Product("Apple", 12.0)
bread = Product("Bread", 5.0)
milk = Product("Milk", 24.0)

apple.show_info()
bread.show_info()
milk.show_info()

milk.price = 20.0
milk.show_info()

apple.show_info()
bread.show_info()