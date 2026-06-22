from sqlalchemy import create_engine, Column, Integer, Float, func, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine(
    'postgresql://postgres:syed4433$$##@localhost/cryptodb')  # Replace with your database credentials
Session = sessionmaker(bind=engine)
session = Session()

def to_two_decimal_places(value):
    """
    Convert a float to a value with 2 decimal places.

    :param value: The float value to be converted.
    :return: The float value rounded to 2 decimal places.
    """
    return round(value, 2)
# Function to calculate the average of a specific column in a given table
def calculate_average(table_name, column_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Check if the table contains any data
    count = session.query(func.count(table.c[column_name])).scalar()

    if count == 0:
        return 0  # Return 0 if the table is empty

    # Construct the query to calculate the average of the specified column
    column = table.c[column_name]
    average_value = session.query(func.avg(column)).scalar()

    return to_two_decimal_places(average_value)


# Example usage: Replace 'my_table' and 'target_column' with your actual table and column names
# x = calculate_average('Bucket500plusBTC', 'Difference')
# print(x)

