# currency.py

class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
            'INR': 75.0
        }

    def convert(self, amount, currency):
        if currency in self.rates:
            return amount * self.rates[currency]
        else:
            print(f"Currency {currency} not supported.")
            return amount
