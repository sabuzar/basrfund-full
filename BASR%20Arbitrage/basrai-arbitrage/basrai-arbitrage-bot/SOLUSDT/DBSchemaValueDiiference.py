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
    __tablename__ = 'Bucket0to2SOLtradeable'

class Bucket2(BucketBase):
    __tablename__ = 'Bucket2to5SOLtradeable'

class Bucket3(BucketBase):
    __tablename__ = 'Bucket5to10SOLtradeable'

class Bucket4(BucketBase):
    __tablename__ = 'Bucket10to20SOLtradeable'

class Bucket5(BucketBase):
    __tablename__ = 'Bucket30plusSOLtradeable'

# Create all tables
Base.metadata.create_all(engine)