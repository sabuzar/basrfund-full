def to_two_decimal_places(value):
    """
    Convert a float to a value with 2 decimal places.

    :param value: The float value to be converted.
    :return: The float value rounded to 2 decimal places.
    """
    return round(value, 2) if isinstance(value, (int, float)) else None

def calculate_value(no_of_opp: int = 1, avg_price: float = 1.0, avg_volume: float = 1.0) -> float:
    """
    Calculate the product of the given parameters with safety checks.

    :param no_of_opp: Number of Price Opportunities Identified (Count#)
    :param avg_price: Average Price Difference Per Category (in USDT)
    :param avg_volume: Average Volume Per trade Per Category (Volume)
    :return: multiple of all parameters rounded to 2 decimal places
    """

    # Ensure all parameters are numeric (either int or float)
    try:
        no_of_opp = float(no_of_opp)
        avg_price = float(avg_price)
        avg_volume = float(avg_volume)
    except ValueError:
        return None  # Return None if any value cannot be converted to a float

    # Calculate only if no_of_opp is greater than 1
    if no_of_opp > 1:
        return to_two_decimal_places(no_of_opp * avg_price * avg_volume)
    else:
        return ''

