from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


def to_two_decimal_places(value):
    """
    Convert a float to a value with 2 decimal places.

    :param value: The float value to be converted.
    :return: The float value rounded to 2 decimal places.
    """
    return round(value, 2) if value is not None else None


def calculate_average_difference_last_24_hours(table_name):
    connection_string = 'postgresql://postgres:syed4433$$##@localhost/cryptodb'
    # Create an engine
    engine = create_engine(connection_string)
    metadata = MetaData()
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the current time and calculate the time 24 hours ago
    now = datetime.utcnow()
    last_24_hours = now - timedelta(hours=24)

    # Reflect the table
    table = Table(table_name, metadata, autoload_with=engine)

    # Check if 'dbtime' and 'Difference' columns exist
    if 'dbtime' in [col.name for col in table.columns] and 'RealDifference' in [col.name for col in table.columns]:

        # Check if there is more than 1 row in the last 24 hours
        row_count = session.query(func.count()).filter(table.c.dbtime >= last_24_hours).scalar()

        if row_count > 1:
            # Filter by the last 24 hours and calculate the average of the 'Difference' column
            average_difference = session.query(func.avg(table.c.RealDifference)).filter(
                table.c.dbtime >= last_24_hours
            ).scalar()

            # Close the session
            session.close()

            # Return the result
            return to_two_decimal_places(average_difference)
        else:
            session.close()
            return ""
    else:
        session.close()
        return "Required columns 'dbtime' or 'Difference' not found in the table."


# Example usage:
# table_name = 'Bucket500plusBTCtradeable'  # Replace with your table name
# average_difference = calculate_average_difference_last_24_hours(table_name)
#
# if average_difference is not None:
#     print(f"Average 'Difference' in the last 24 hours: {average_difference}")
# else:
#     print("No data found for the last 24 hours.")
