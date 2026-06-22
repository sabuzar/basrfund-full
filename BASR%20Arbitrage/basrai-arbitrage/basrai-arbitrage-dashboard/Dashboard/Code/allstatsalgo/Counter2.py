from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


def get_tables_length(table_names):
    connection_string = 'postgresql://postgres:syed4433$$##@localhost/cryptodb'
    # Create an engine
    engine = create_engine(connection_string)
    metadata = MetaData()
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    table_lengths = {}

    for table_name in table_names:
        # Reflect the table
        table = Table(table_name, metadata, autoload_with=engine)
        # Use the count function to get the number of rows
        row_count = session.query(func.count()).select_from(table).scalar()
        # Store the table name and its length in the dictionary
        table_lengths[table_name] = row_count

    # Close the session
    session.close()

    return table_lengths


# Example usage:
table_names = ['Bucket0to2SOLtradeable', 'Bucket2to5SOLtradeable', 'Bucket5to10SOLtradeable', 'Bucket10to20SOLtradeable', 'Bucket30plusSOLtradeable']
lengths = get_tables_length(table_names)
B1 = lengths['Bucket0to2SOLtradeable']
B2 = lengths['Bucket2to5SOLtradeable']
B3 = lengths['Bucket5to10SOLtradeable']
B4 = lengths['Bucket10to20SOLtradeable']
B5 = lengths['Bucket30plusSOLtradeable']



print(B1,B2,B3,B4,B5)


