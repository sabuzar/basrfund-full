from sqlalchemy.orm import sessionmaker
from DBSchemaPriceDifference import Bucket1, Bucket2, Bucket3, Bucket4, Bucket5, Base, engine
from BaseAlgorithm import converting_4decimalPoints
import time


"""
modelsPriceDifference.py

This module is responsible for managing the insertion of cryptocurrency price difference data into a database using SQLAlchemy. It defines functions to generate timestamps, insert records into specific database buckets based on price differences, and perform checks on exchange data.

Key Functions:
- **generate_unix_timestamp()**: Returns the current time in milliseconds since the epoch, useful for timestamping records.
- **insert_to_bucket(bucket_class, ...)**: Inserts a new record into the specified bucket class. It handles session management and commits the transaction to the database.
- **db_buckets(Difference, ...)**: Determines which bucket to insert data into based on the price difference. It categorizes differences into five predefined ranges corresponding to different buckets.
- **checker(TS, ...)**: Validates exchange statuses and conditions before invoking `db_buckets` to insert data.

Database Setup:
- The module initializes a SQLAlchemy session and creates all necessary tables upon execution. The bucket classes (Bucket1 to Bucket5) correspond to different ranges of Bitcoin tradeable amounts.

Usage:
1. Ensure that the required database schema is defined in `DBSchemaPriceDifference.py`.
2. Call the appropriate functions with the necessary parameters to manage price difference data.

Dependencies:
- Requires SQLAlchemy for ORM functionality and interaction with the database.
- Imports utility functions from `BaseAlgorithm`.

Exception Handling:
- Includes error handling during database operations to ensure that transactions are rolled back in case of failure.

"""

def generate_unix_timestamp():
    # Get the current time in seconds and multiply by 1000 to convert to milliseconds
    timestamp = time.time() * 1000
    return float(timestamp)

# Example usage
current_timestamp = generate_unix_timestamp()

# Use this value for inserting data

# Database setup
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def insert_to_bucket(bucket_class, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, ExchangeBP1, Exchange1BPV, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time):
    session = Session()
    try:
        record = bucket_class(
            TimeDtamp=TimeDtamp,
            Exchange1=Exchange1,
            Exchange1_LTP=Exchange1_LTP,
            Exchange1AP1=Exchange1AP1,
            Exchange1AP1V=Exchange1AP1V,
            Exchange1BP1=ExchangeBP1,
            Exchange1BP1V=Exchange1BPV,
            Exchange2=Exchange2,
            Exchange2_LTP=Exchange2_LTP,
            Exchange2AP1=Exchange2AP1,
            Exchange2AP1V=Exchange2AP1V,
            Exchange2BP1=Exchange2BP1,
            Exchange2BP1V=Exchange2BP1V,
            Difference=Difference,
            Processing_Time=Processing_Time
        )
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Failed: {e}")
    finally:
        session.close()

def db_buckets(Difference, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Processing_Time):
    if 50 <= Difference < 100:
        insert_to_bucket(Bucket1, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 100 <= Difference < 200:
        insert_to_bucket(Bucket2, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 200 <= Difference < 300:
        insert_to_bucket(Bucket3, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 300 <= Difference < 400:
        insert_to_bucket(Bucket4, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif Difference > 500:
        insert_to_bucket(Bucket5, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)

# Checker function
def checker(TS, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BPV, Exchange2,
            Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Processing_Time,
            Exchange1subExchange2, Exchange1Status, Exchange2Status):



    if Exchange1Status == 200 and Exchange2Status == 200:
        V1= converting_4decimalPoints(Exchange1BPV)
        V2= converting_4decimalPoints(Exchange2AP1V)
        if V1 > 0 and V2 > 0:
            if TS == None:
                TS = generate_unix_timestamp()
            if Exchange1BP - Exchange2AP1 == Exchange1subExchange2:
                db_buckets(
                    Exchange1subExchange2, TS, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BPV, Exchange2,
                    Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Processing_Time
                )