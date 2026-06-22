from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from datetime import datetime, timedelta

def get_tables_length_last_24_hours(table_names):
    connection_string = 'postgresql://postgres:syed4433$$##@localhost/cryptodb'
    # Create an engine
    engine = create_engine(connection_string)
    metadata = MetaData()
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    table_lengths = {}

    # Get the current time and calculate the time 24 hours ago
    now = datetime.utcnow()
    last_24_hours = now - timedelta(hours=24)

    for table_name in table_names:
        # Reflect the table
        table = Table(table_name, metadata, autoload_with=engine)
        # Ensure the table has a 'dbtime' column and filter by the last 24 hours
        if 'dbtime' in [col.name for col in table.columns]:
            row_count = session.query(func.count()).select_from(table).filter(
                table.c.dbtime >= last_24_hours
            ).scalar()
            # Store the table name and its row count in the dictionary
            table_lengths[table_name] = row_count
        else:
            table_lengths[table_name] = "No 'dbtime' column found"

    # Close the session
    session.close()

    return table_lengths

#
# table_names = ['Bucket0to2BCHtradeable', 'Bucket100to200BTCtradeable', 'Bucket200to300BTCtradeable', 'Bucket300to400BTCtradeable', 'Bucket500plusBTCtradeable']
# lengths = get_tables_length_last_24_hours(table_names)
#
# # Extract individual table counts
# B1 = lengths['Bucket0to2BCHtradeable']
# B2 = lengths['Bucket100to200BTCtradeable']
# B3 = lengths['Bucket200to300BTCtradeable']
# B4 = lengths['Bucket300to400BTCtradeable']
# B5 = lengths['Bucket500plusBTCtradeable']
#
# print(B1, B2, B3, B4, B5)
