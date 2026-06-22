from sqlalchemy import create_engine, Column, Integer, Float, func, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine('postgresql://postgres:syed4433$$##@localhost/cryptodb')  # Replace with your database credentials
Session = sessionmaker(bind=engine)
session = Session()

# Function to calculate the minimum value of a specific column in a given table
def calculate_minimum(table_name, column_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Construct the query to calculate the minimum of the specified column
    column = table.c[column_name]
    minimum_value = session.query(func.min(column)).scalar()

    # Output the result

    return minimum_value

# Example usage: Replace 'my_table' and 'target_column' with your actual table and column names
# calculate_minimum('Bucket500plusBTC', 'Difference')
