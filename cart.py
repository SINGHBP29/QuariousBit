# cart.py

from product_catalog import ProductCatalog

class ViewCart:
    def __init__(self, product_catalog):
        self.cart_items = {}
        self.discount = 0  # Initialize discount
        self.product_catalog = product_catalog  # Store the product Catalog

    def add_item(self, item, quantity):
        if hasattr(item, 'product_id'):
            if item.product_id in self.cart_items:
                self.cart_items[item.product_id]['quantity'] += quantity
            else:
                self.cart_items[item.product_id] = {'item': item, 'quantity': quantity}
        else:
            raise ValueError("Item must be an instance of Product with 'product_id' attribute.")

    def remove_item(self, item, quantity):
        if hasattr(item, 'product_id'):
            if item.product_id in self.cart_items:
                if self.cart_items[item.product_id]['quantity'] <= quantity:
                    del self.cart_items[item.product_id]
                else:
                    self.cart_items[item.product_id]['quantity'] -= quantity
        else:
            raise ValueError("Item must be an instance of Product with 'product_id' attribute.")

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")

    def view_cart(self):
        total_before_discount = sum(item.price * quantity for item_id, cart_info in self.cart_items.items() for item in [cart_info['item']] for quantity in [cart_info['quantity']])
        discount_amount = total_before_discount * (self.discount / 100)
        final_total = total_before_discount - discount_amount
        
        print("Cart contents:")
        for item_id, cart_info in self.cart_items.items():
            item = cart_info['item']
            quantity = cart_info['quantity']
            print(f"{item.name}: {quantity} x ${item.price:.2f} = ${item.price * quantity:.2f}")
        
        print(f"Total Before discount: ${total_before_discount:.2f}")
        print(f"Discount applied: ${discount_amount:.2f}")
        print(f"Total After discount: ${final_total:.2f}")

    def show_cart(self):
        self.view_cart()  # Call the existing method to display Cart contents

    def get_product(self, product_id):
        return self.product_catalog.get_product(product_id)
