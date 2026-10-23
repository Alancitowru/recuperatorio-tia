# Create a class called Product. Use the __init__ method to initialize two
# attributes: name and price.
# Add a method called apply_discount(percentage) that takes a number as an
# argument and reduces the product price by that percentage.
# Create two instances of the class with different items and prices.
# Apply a different discount to each product and print their final prices on the
# screen.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)


product1 = Product("T-shirt", 10000)
product2 = Product("Shoes", 50000)

product1.apply_discount(20)
product2.apply_discount(10)

print(product1.name, ":", product1.price)
print(product2.name, ":", product2.price)
