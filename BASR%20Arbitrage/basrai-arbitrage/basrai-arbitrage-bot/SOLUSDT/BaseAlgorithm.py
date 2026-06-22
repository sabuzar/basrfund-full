import math
from datetime import datetime, timezone, timedelta

class Exchange:
    def __init__(self, name, bid_price, ask_prices):
        self.name = name
        self.bid_price = bid_price
        self.ask_prices = ask_prices
        self.differences = {}

    def calculate_differences(self):
        for exchange, ask_price in self.ask_prices.items():
            self.differences[f"{self.name}BP_{exchange}AP"] = self.bid_price - ask_price

    def get_differences(self):
        return self.differences



# Time conversion functions
async def convert_to_gmt_async(timestamp, offset_hours):
    if len(str(timestamp)) == 13:
        timestamp_sec = timestamp / 1000.0  # Convert milliseconds to seconds
    else:
        timestamp_sec = timestamp  # Timestamp is already in seconds

    utc_datetime = datetime.utcfromtimestamp(timestamp_sec).replace(tzinfo=timezone.utc)
    gmt_offset = timedelta(hours=offset_hours)
    gmt_datetime = utc_datetime + gmt_offset
    gmt_datetime = gmt_datetime.replace(tzinfo=None)
    time = gmt_datetime.microsecond
    gmt_datetime_str = gmt_datetime.strftime("%a, %d %b %Y %H:%M:%S")

    return gmt_datetime_str, time

async def convert_to_gmt5_async(timestamp):
    return await convert_to_gmt_async(timestamp, 5)

async def convert_to_gmt4_async(timestamp):
    return await convert_to_gmt_async(timestamp, 4)

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