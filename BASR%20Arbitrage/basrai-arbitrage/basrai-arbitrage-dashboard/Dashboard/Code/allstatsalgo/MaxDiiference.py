from sqlalchemy import create_engine, Column, Integer, Float, func, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine('postgresql://postgres:syed4433$$##@localhost/cryptodb')  # Replace with your database credentials
Session = sessionmaker(bind=engine)
session = Session()

# Function to calculate the maximum value of a specific column in a given table
def calculate_maximum(table_name, column_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Construct the query to calculate the maximum of the specified column
    column = table.c[column_name]
    maximum_value = session.query(func.max(column)).scalar()

    # Output the result

    return maximum_value
#
# Example usage: Replace 'my_table' and 'target_column' with your actual table and column names
print(calculate_maximum('Bucket500plusBTCtradeable', 'Exchange1BP1V'))
