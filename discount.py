# discount.py
class DiscountHandler:
    def __init__(self):
        self.discounts = [
            {"category": "fashion", "type": "BOGO", "description": "Buy 1 Get 1 Free"},
            {"category": "electronics", "type": "percentage", "value": 0.10, "description": "10% off"}
        ]

    def query_discounts(self):
        print("Available Discounts:")
        for discount in self.discounts:
            print(f"- {discount['description']} on {discount['category']}")

    def apply_discounts(self, cart):
        total_before_discount = sum(item.price * quantity for item_id, quantity in cart.cart_items.items() for item in [cart.get_product(item_id)])
        total_discount = 0

        # Apply Buy 1 Get 1 Free on fashion items
        for cart_info in cart.cart_items.values():
            if isinstance(cart_info, dict) and 'item' in cart_info and 'quantity' in cart_info:
                item = cart_info['item']
                quantity = cart_info['quantity']
                for discount in self.discounts:
                    if discount['category'] == item.category and discount['type'] == "BOGO" and quantity >= 2:
                        free_items = quantity // 2
                        discount_value = free_items * item.price
                        total_discount += discount_value
                        print(f"Discount applied: {discount['description']} on {item.name}, saving ${discount_value:.2f}.")

        # Apply 10% off on electronics Devices
        for cart_info in cart.cart_items.values():
            if isinstance(cart_info, dict) and 'item' in cart_info and 'quantity' in cart_info:
                item = cart_info['item']
                quantity = cart_info['quantity']
                for discount in self.discounts:
                    if discount['category'] == item.category and discount['type'] == "percentage":
                        discount_value = discount['value'] * (item.price * quantity)
                        total_discount += discount_value
                        print(f"Discount applied: {discount['description']} on {item.name}, saving ${discount_value:.2f}.")

        total_after_discount = total_before_discount - total_discount
        print(f"Total before discount: ${total_before_discount:.2f}")
        print(f"Total discount applied: ${total_discount:.2f}")
        print(f"Total after discount: ${total_after_discount:.2f}")

        return total_discount
