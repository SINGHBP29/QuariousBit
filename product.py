# product.py

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id  # This should be present
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price:.2f} [{self.category}]"
