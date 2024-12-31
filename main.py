# main.py
from product_catalog import ProductCatalog
from cart import ViewCart
from checkout import Checkout
from discount import DiscountHandler

if __name__ == "__main__":
    # Initialize product catalog, shopping cart, discount handler, and checkout
    product_catalog = ProductCatalog()
    cart = ViewCart(product_catalog)
    checkout = Checkout()
    discount_handler = DiscountHandler()
    product_catalog.show_all_products()

    while True:
        print("\nOptions: add, remove, view, apply discount, checkout, exit")
        action = input("What would you like to do? ").lower()

        if action == "add":
            product_id = input("Enter the Product ID to add: ").upper()
            product = product_catalog.get_product(product_id)
            if product and hasattr(product, 'product_id'):
                while True:
                    quantity_input = input(f"How many {product.name}s would you like to add? (Type 'cancel' to go back) ").strip()
                    if quantity_input.lower() == 'cancel':
                        break
                    try:
                        quantity = int(quantity_input)
                        if quantity < 0:
                            print("Please enter a positive number.")
                        else:
                            cart.add_item(product, quantity)
                            print(f"Added {quantity} {product.name}(s) to the cart.")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            else:
                print("Product not found or invalid product object.")
        elif action == "remove":
            product_id = input("Enter the Product ID to remove: ").upper()
            product = product_catalog.get_product(product_id)
            if product and hasattr(product, 'product_id'):
                while True:
                    quantity_input = input(f"How many {product.name}s would you like to remove? (Type 'cancel' to go back) ").strip()
                    if quantity_input.lower() == 'cancel':
                        break
                    try:
                        quantity = int(quantity_input)
                        if quantity < 0:
                            print("Please enter a positive number.")
                        else:
                            cart.remove_item(product, quantity)
                            print(f"Removed {quantity} {product.name}(s) from the cart.")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            else:
                print("Product not found or invalid product object.")
        elif action == "apply discount":
            discount_handler.query_discounts()
            while True:
                discount_input = input("Enter discount percentage (0-100) or 'none' to skip: ").strip()
                if discount_input.lower() == 'none':
                    break
                try:
                    discount_percentage = float(discount_input)
                    if 0 <= discount_percentage <= 100:
                        cart.apply_discount(discount_percentage)
                        print(f"Discount of {discount_percentage}% applied.")
                        break
                    else:
                        print("Please enter a valid percentage between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif action == "view":
            cart.view_cart()
            
        elif action == "checkout":
            chosen_currency = input("Convert to (USD, EUR, GBP, INR): ").upper()
            checkout.final_checkout(cart, chosen_currency)
            break
        elif action == "exit":
            print("Exiting the shopping system.")
            break
        else:
            print("Invalid action. Please try again.")