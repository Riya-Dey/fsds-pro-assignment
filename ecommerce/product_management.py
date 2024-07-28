# ecommerce/product_management.py

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.price
            self.price -= discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")
