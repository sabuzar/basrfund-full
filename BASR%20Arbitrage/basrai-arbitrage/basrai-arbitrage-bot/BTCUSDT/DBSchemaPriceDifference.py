import os
from sqlalchemy import Column, INTEGER, FLOAT, String, Sequence, create_engine
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


from config import DATABASE_URL

"""
Module: DBSchemaPriceDifference

This module defines the database schema for tracking price differences across cryptocurrency exchanges. It uses SQLAlchemy for ORM and database interactions.

Dependencies:
--------------
- SQLAlchemy: For database modeling and interaction.
- config.py: Must provide a `DATABASE_URL` for database connection.

Classes:
---------
- BucketBase: An abstract base class defining common columns for price difference data.
- Bucket1, Bucket2, Bucket3, Bucket4, Bucket5:
    Concrete table models representing data buckets for specific ranges of cryptocurrency trading volumes.

Attributes:
---------
- BucketBase.id: Primary key for the table.
- BucketBase.dbtime: Timestamp of entry creation.
- BucketBase.TimeDtamp: Float representation of time for sorting or calculation.
- BucketBase.Exchange1, Exchange2: Exchange names.
- BucketBase.Exchange1_LTP, Exchange2_LTP: Last traded prices for the exchanges.
- BucketBase.Exchange1AP1, Exchange2AP1: Ask price 1 for the exchanges.
- BucketBase.Exchange1BP1, Exchange2BP1: Bid price 1 for the exchanges.
- BucketBase.Difference: Calculated price difference.
- BucketBase.Processing_Time: Time taken for processing.

Setup:
---------
- Requires `DATABASE_URL` in the `config.py` file.
- Uses NullPool for connection pooling.

Usage:
---------
Run the script to initialize the database schema. It creates tables for specific trading volume buckets in the database.

"""



# Ensure DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set for the application. Please set the DATABASE_URL in config.py.")

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
    Exchange1AP1 = Column(FLOAT, nullable=False)
    Exchange1AP1V = Column(FLOAT, nullable=False)
    Exchange1BP1 = Column(FLOAT, nullable=False)
    Exchange1BP1V = Column(FLOAT, nullable=False)
    Exchange2 = Column(String, nullable=False)
    Exchange2_LTP = Column(FLOAT, nullable=False)
    Exchange2AP1 = Column(FLOAT, nullable=False)
    Exchange2AP1V = Column(FLOAT, nullable=False)
    Exchange2BP1 = Column(FLOAT, nullable=False)
    Exchange2BP1V = Column(FLOAT, nullable=False)
    Difference = Column(FLOAT, nullable=False)
    Processing_Time = Column(FLOAT, nullable=False)

class Bucket1(BucketBase):
    __tablename__ = 'Bucket99BTC'

class Bucket2(BucketBase):
    __tablename__ = 'Bucket100to200BTC'

class Bucket3(BucketBase):
    __tablename__ = 'Bucket200to300BTC'

class Bucket4(BucketBase):
    __tablename__ = 'Bucket300to400BTC'

class Bucket5(BucketBase):
    __tablename__ = 'Bucket500plusBTC'

# Create all tables
Base.metadata.create_all(engine)