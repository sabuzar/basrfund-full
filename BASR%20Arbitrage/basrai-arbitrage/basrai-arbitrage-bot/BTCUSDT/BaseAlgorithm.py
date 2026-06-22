import math

class Exchange:
    __slots__ = ('name', 'bid_price', 'ask_prices', 'differences')  # Optimize memory usage by limiting instance attributes

    def __init__(self, name, bid_price, ask_prices):
        self.name = name
        self.bid_price = bid_price
        self.ask_prices = ask_prices
        self.differences = {}

    def calculate_differences(self):
        self.differences = {
            f"{self.name}BP_{exchange}AP": self.bid_price - ask_price
            for exchange, ask_price in self.ask_prices.items()
        }

    def get_differences(self):
        return self.differences

"""
Module: BaseAlgorithm

This module defines the `Exchange` class, which is used for calculating and managing price differences between bid prices and ask prices of various exchanges.

Classes:
---------
- Exchange: Represents an exchange with a bid price and ask prices from other exchanges. It provides methods to calculate and retrieve the price differences.

Methods:
---------
- Exchange.__init__(name, bid_price, ask_prices):
    Initializes the Exchange object with the exchange's name, bid price, and ask prices from other exchanges.

- Exchange.calculate_differences():
    Calculates the differences between the exchange's bid price and ask prices from other exchanges, storing the results in a dictionary.

- Exchange.get_differences():
    Returns the dictionary of calculated price differences.

Usage:
---------
Use the `Exchange` class to compute and retrieve price differences for market analysis or trading strategy purposes.

"""




# Decimal conversion functions


def converting_4decimalPoints(number):
    try:
        # Ensure the input is a float
        number = float(number)
        # Truncate to 2 decimal places
        truncated_value = math.trunc(number * 100) / 10000
        return truncated_value
    except ValueError:
        return "Invalid input: The number provided is not a valid float."