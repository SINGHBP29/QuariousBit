# checkout.py

from cart import ViewCart

class Checkout:
    def __init__(self):
        # Define exchange rates (example values)
        self.exchange_rates = {
            'USD': 1.0,      # Base currency
            'EUR': 0.93,     # Example: 1 USD = 0.93 EUR
            'GBP': 0.82,     # Example: 1 USD = 0.82 GBP
            'INR': 82.67     # Example: 1 USD = 82.67 INR
        }

    def final_checkout(self, cart, chosen_currency):
        # Check if cart is an instance of ViewCart
        if not isinstance(cart, ViewCart):
            raise ValueError("Cart must be an instance of ViewCart.")

        # Calculate total before discount
        total_before_discount = sum(
            cart.get_product(item_id).price * cart_info['quantity']
            for item_id, cart_info in cart.cart_items.items()
        )
        
        # Apply discount if any
        discount_amount = total_before_discount * (cart.discount / 100)
        final_total = total_before_discount - discount_amount

        # Convert amount to select currency
        if chosen_currency in self.exchange_rates:
            conversion_rate = self.exchange_rates[chosen_currency]
            final_total_converted = final_total * conversion_rate
        else:
            raise ValueError("Currency is not valid.")

        print(f"Total Before discount: ${total_before_discount:.2f}")
        print(f"Discount applied: ${discount_amount:.2f}")
        print(f"Total after discount: ${final_total:.2f}")
        print(f"Amount in {chosen_currency}: {final_total_converted:.2f}")
