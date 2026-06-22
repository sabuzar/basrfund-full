import os
from sqlalchemy import Column, INTEGER, FLOAT, String, Sequence, create_engine
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


from config import DATABASE_URL

# Ensure DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set for the application. Please set the DATABASE_URL in config.py.")

"""
DBSchemaValueDifference.py

This module defines the database schema for storing cryptocurrency trading data using SQLAlchemy. It establishes a connection to a specified database via a URL and defines several database models for different trading buckets.

Key Components:
- **Database Connection**: Utilizes SQLAlchemy's `create_engine` function to connect to the database specified by `DATABASE_URL`. A null connection pool is used to avoid connection reuse.
- **Base Class**: The `BucketBase` class serves as an abstract base for all bucket models, ensuring common fields are included in each table.
- **Bucket Models**: Five specific bucket classes (`Bucket1`, `Bucket2`, `Bucket3`, `Bucket4`, `Bucket5`) are defined, each corresponding to different ranges of Bitcoin tradeable amounts.

Database Schema:
- **Common Fields**:
  - `id`: Primary key for each record.
  - `dbtime`: Timestamp of the record creation, with timezone support.
  - `TimeDtamp`: A floating-point representation of time.
  - Various fields for exchange data (e.g., `Exchange1`, `Exchange2`, their last traded prices, and bid/ask prices).
  - `RealDifference` and `Difference`: Fields to store calculated differences between exchanges.
  - `Processing_Time`: A float indicating the time taken for processing.

Usage:
1. Ensure that the `DATABASE_URL` is set in the configuration file (`config.py`).
2. This module will automatically create the necessary tables in the database upon execution.

Exceptions:
- Raises a ValueError if `DATABASE_URL` is not set.

Dependencies:
- Requires SQLAlchemy and its MySQL dialect for database interaction.

"""


# Create engine with connection pooling
engine = create_engine(DATABASE_URL, poolclass=NullPool)

# Base class for model definitions
Base = declarative_base()

# Base class for buckets to avoid repetition
class BucketBase(Base):
    __abstract__ = True
    id = Column(INTEGER, Sequence('example_table_id_seq'), primary_key=True)
    dbtime = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    TimeDtamp = Column(FLOAT, nullable=False)
    Exchange1 = Column(String, nullable=False)
    Exchange1_LTP = Column(FLOAT, nullable=False)
    Exchange1BP1 = Column(FLOAT, nullable=False)
    Exchange1BP1V = Column(FLOAT, nullable=False)
    Exchange2 = Column(String, nullable=False)
    Exchange2_LTP = Column(FLOAT, nullable=False)
    Exchange2AP1 = Column(FLOAT, nullable=False)
    Exchange2AP1V = Column(FLOAT, nullable=False)
    Exchange1BPAC=Column(FLOAT, nullable=False)
    Exchange1APAC = Column(FLOAT, nullable=False)
    RealDifference=Column(FLOAT, nullable=False)
    Difference = Column(FLOAT, nullable=False)
    Processing_Time = Column(FLOAT, nullable=False)

class Bucket1(BucketBase):
    __tablename__ = 'Bucket99BTCtradeable'

class Bucket2(BucketBase):
    __tablename__ = 'Bucket100to200BTCtradeable'

class Bucket3(BucketBase):
    __tablename__ = 'Bucket200to300BTCtradeable'

class Bucket4(BucketBase):
    __tablename__ = 'Bucket300to400BTCtradeable'

class Bucket5(BucketBase):
    __tablename__ = 'Bucket500plusBTCtradeable'

# Create all tables
Base.metadata.create_all(engine)