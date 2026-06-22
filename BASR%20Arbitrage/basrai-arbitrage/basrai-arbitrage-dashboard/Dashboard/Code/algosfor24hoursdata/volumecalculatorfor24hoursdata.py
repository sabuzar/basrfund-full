from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


# Set up the database engine and session
def setup_db_connection(connection_string):
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session


def to_two_decimal_places(value):
    """
    Convert a float to a value with 2 decimal places.

    :param value: The float value to be converted.
    :return: The float value rounded to 2 decimal places.
    """
    return round(value, 2) if value is not None else None


# Function to perform calculations (average, median, minimum, maximum) on a specific column for the last 24 hours
def perform_calculations_last_24_hours(table_name, column_name, time_column_name='dbtime'):
    connection_string = 'postgresql://postgres:syed4433$$##@localhost/cryptodb'  # Replace with your database credentials
    engine, session = setup_db_connection(connection_string)

    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)
    column = table.c[column_name]
    time_column = table.c[time_column_name]

    # Get the current time and calculate the time 24 hours ago
    now = datetime.utcnow()
    last_24_hours = now - timedelta(hours=24)

    # Check if the table has any data in the last 24 hours
    row_count = session.query(func.count()).select_from(table).filter(time_column >= last_24_hours).scalar()
    if row_count == 0:
        session.close()
        return {
            "average": "",
            "median": "",
            "minimum": "",
            "maximum": ""
        }

    # Calculate average
    average_value = session.query(func.avg(column)).filter(time_column >= last_24_hours).scalar()

    # Calculate maximum
    maximum_value = session.query(func.max(column)).filter(time_column >= last_24_hours).scalar()

    # Calculate minimum
    minimum_value = session.query(func.min(column)).filter(time_column >= last_24_hours).scalar()

    # Calculate median
    if row_count % 2 == 1:  # Odd number of rows
        median_value = session.query(column).filter(time_column >= last_24_hours).order_by(column).offset(row_count // 2).limit(1).scalar()
    else:  # Even number of rows
        row1 = session.query(column).filter(time_column >= last_24_hours).order_by(column).offset(row_count // 2 - 1).limit(1).scalar()
        row2 = session.query(column).filter(time_column >= last_24_hours).order_by(column).offset(row_count // 2).limit(1).scalar()
        median_value = (row1 + row2) / 2.0

    session.close()

    return {
        "average": to_two_decimal_places(average_value),
        "median": to_two_decimal_places(median_value),
        "minimum": to_two_decimal_places(minimum_value),
        "maximum": to_two_decimal_places(maximum_value)
    }


# # Example usage:
# print(perform_calculations_last_24_hours('Bucket500plusBTCtradeable', 'Exchange1BP1V'))
