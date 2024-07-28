# ecommerce/order_processing.py

from .product_management import Product

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.items.append((product, quantity))

    def total_amount(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def __str__(self):
        items_str = ', '.join([f"{item.name} (x{quantity})" for item, quantity in self.items])
        return f"Order(order_id={self.order_id}, items=[{items_str}])"
