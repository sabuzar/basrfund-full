from sqlalchemy.orm import sessionmaker
from DBSchemaPricedifference import Bucket1, Bucket2, Bucket3, Bucket4, Bucket5, Base, engine
from BaseAlgorithm import converting_4decimalPoints
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
    if 5 <= Difference < 10:
        insert_to_bucket(Bucket1, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 10 <= Difference < 20:
        insert_to_bucket(Bucket2, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 20 <= Difference < 30:
        insert_to_bucket(Bucket3, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif 30 <= Difference < 40:
        insert_to_bucket(Bucket4, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)
    elif Difference > 50:
        insert_to_bucket(Bucket5, TimeDtamp, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Difference, Processing_Time)

# Checker function
def checker(TS, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BPV, Exchange2,
            Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Processing_Time,
            Exchange1subExchange2, Exchange1Status, Exchange2Status):

    if Exchange1Status == 200 and Exchange2Status == 200:
        V1= converting_4decimalPoints(Exchange1BPV)
        V2= converting_4decimalPoints(Exchange2AP1V)
        if V1 > 10 and V2 > 10:
            if Exchange1BP - Exchange2AP1 == Exchange1subExchange2:
                db_buckets(
                    Exchange1subExchange2, TS, Exchange1, Exchange1_LTP, Exchange1AP1, Exchange1AP1V, Exchange1BP, Exchange1BPV, Exchange2,
                    Exchange2_LTP, Exchange2AP1, Exchange2AP1V, Exchange2BP1, Exchange2BP1V, Processing_Time
                )