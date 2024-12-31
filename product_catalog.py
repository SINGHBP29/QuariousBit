# product_catalog.py

from product import Product

class ProductCatalog:
    def __init__(self):
        # Pre-populate catalog with products
        self.products = {
            'P001': Product('P001', 'Gaming Laptop', 1500.00, 'electronics'),
            'P002': Product('P002', 'Smartphone', 800.00, 'electronics'),
            'P003': Product('P003', 'Jacket', 60.00, 'fashion')
        }

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def show_all_products(self):
        print("Available Products:")
        for product in self.products.values():
            print(product)
