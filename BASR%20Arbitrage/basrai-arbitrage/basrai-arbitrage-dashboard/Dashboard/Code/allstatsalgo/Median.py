from sqlalchemy import create_engine, Column, Integer, Float, func, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine('postgresql://postgres:syed4433$$##@localhost/cryptodb')  # Replace with your database credentials
Session = sessionmaker(bind=engine)
session = Session()

# Function to calculate the median of a specific column in a given table
def calculate_median(table_name, column_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    # Construct the query to calculate the median of the specified column
    column = table.c[column_name]
    count = session.query(func.count(column)).scalar()

    if count % 2 == 1:  # Odd number of rows
        median_value = session.query(column).order_by(column).offset(count // 2).limit(1).scalar()
    else:  # Even number of rows
        row1 = session.query(column).order_by(column).offset(count // 2 - 1).limit(1).scalar()
        row2 = session.query(column).order_by(column).offset(count // 2).limit(1).scalar()
        median_value = (row1 + row2) / 2.0

    # Output the result

    return median_value

# Example usage: Replace 'my_table' and 'target_column' with your actual table and column names
# calculate_median('Bucket500plusBTC', 'Difference')
