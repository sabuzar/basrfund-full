from sqlalchemy.orm import sessionmaker
from DBSchemaValueDifference import Bucket1, Bucket2, Bucket3, Bucket4, Bucket5, Base, engine
from BaseAlgorithm import converting_4decimalPoints
import time

"""
modelsValueDifference.py

This module is designed for managing and inserting cryptocurrency price difference data into a database using SQLAlchemy. It provides functions to generate timestamps, insert records into designated database buckets based on price differences, and validate exchange data.

Key Functions:
- **generate_unix_timestamp()**: Generates the current timestamp in milliseconds since the epoch, facilitating accurate time tracking for records.

- **insert_to_bucket(bucket_class, ...)**: Inserts a new record into the specified bucket class. It manages database sessions, handles exceptions, and ensures data integrity through transaction management.

- **db_buckets(Difference, ...)**: Determines the appropriate bucket for inserting data based on the price difference. It categorizes differences into five defined ranges corresponding to different buckets.

- **calc_smallerV(E1V1, E2V1)**: Returns the smaller of two values, used for calculations involving exchange rates.

- **real_value(E1B1, E2A1, E1V1, E2V1)**: Computes real values based on exchange rates and quantities, returning adjusted values for further processing.

- **checker(TS, ...)**: Validates the statuses of two exchanges and checks conditions before invoking `db_buckets` to insert data.

Database Setup:
- Initializes a SQLAlchemy session and creates necessary tables defined in `DBSchemaValueDifference.py`.

Usage:
1. Ensure that the database schema is established in `DBSchemaValueDifference.py`.
2. Call the relevant functions with appropriate parameters to manage price difference data effectively.

Dependencies:
- Requires SQLAlchemy for ORM functionality.
- Imports utility functions from `BaseAlgorithm`.

Exception Handling:
- Implements error handling during database operations to ensure that transactions are rolled back in case of failure.

"""

def generate_unix_timestamp():
    # Get the current time in seconds and multiply by 1000 to convert to milliseconds
    timestamp = time.time() * 1000
    return float(timestamp)

# Example usage
current_timestamp = generate_unix_timestamp()


# Database setup
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def insert_to_bucket(bucket_class, TimeDtamp, Exchange1, Exchange1_LTP, ExchangeBP1, Exchange1BPV, Exchange2,
                     Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC
                     ,RealDifference ,Difference,Processing_Time):
    session = Session()
    try:
        record = bucket_class(
            TimeDtamp=TimeDtamp,
            Exchange1=Exchange1,
            Exchange1_LTP=Exchange1_LTP,
            Exchange1BP1=ExchangeBP1,
            Exchange1BP1V=Exchange1BPV,
            Exchange2=Exchange2,
            Exchange2_LTP=Exchange2_LTP,
            Exchange2AP1=Exchange2AP1,
            Exchange2AP1V=Exchange2AP1V,
            Exchange1BPAC=Exchange1BPAC,
            Exchange1APAC =  Exchange1APAC,
            RealDifference = RealDifference,
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


def db_buckets(Difference, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Processing_Time):
    if 50 <= RealDifference < 100:
        insert_to_bucket(Bucket1, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 100 <= RealDifference < 200:
        insert_to_bucket(Bucket2, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 200 <= RealDifference < 300:
        insert_to_bucket(Bucket3, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 300 <= RealDifference < 400:
        insert_to_bucket(Bucket4, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif RealDifference > 500:
        insert_to_bucket(Bucket5, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)


def calc_smallerV(E1V1, E2V1):
    return min(float(E1V1), float(E2V1))

def real_value(E1B1, E2A1, E1V1, E2V1):
    E1B1, E2A1 = float(E1B1), float(E2A1)
    val = calc_smallerV(E1V1, E2V1)
    x = E1B1 * val
    y = E2A1 * val
    return y, x, x - y
# Checker function
def checker(TS, Exchange1, Exchange1_LTP,Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BPV, Exchange2,
            Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange2BP1, Exchange2BP1V,  Processing_Time,
            Exchange1subExchange2, Exchange1Status, Exchange2Status):


    if Exchange1Status == 200 and Exchange2Status == 200:
        V1= converting_4decimalPoints(Exchange1BPV)
        V2= converting_4decimalPoints(Exchange2AP1V)
        if V1 > 0 and V2 > 0:
            if TS == None:
                TS = generate_unix_timestamp()
            if Exchange1BP - Exchange2AP1 == Exchange1subExchange2:
                Exchange1BPAC, Exchange1APAC, RealDifference=real_value(Exchange1BP,Exchange2AP1,Exchange1BPV,Exchange2AP1V)
                db_buckets(
                    Exchange1subExchange2, TS, Exchange1, Exchange1_LTP, Exchange1BP, Exchange1BPV, Exchange2,
                    Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC, Exchange1APAC, RealDifference, Processing_Time
                )
