from sqlalchemy.orm import sessionmaker
from DBSchemaValueDifference import Bucket1, Bucket2, Bucket3, Bucket4, Bucket5, Base, engine
from BaseAlgorithm import converting_4decimalPoints
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
    if 5 <= RealDifference < 10:
        insert_to_bucket(Bucket1, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 10 <= RealDifference < 20:
        insert_to_bucket(Bucket2, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 20 <= RealDifference < 30:
        insert_to_bucket(Bucket3, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif 30 <= RealDifference < 40:
        insert_to_bucket(Bucket4, TimeDtamp, Exchange1, Exchange1_LTP,  Exchange1BP, Exchange1BP1, Exchange2, Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC,Exchange1APAC,RealDifference, Difference, Processing_Time)
    elif RealDifference > 50:
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
        if V1 > 10 and V2 > 10:
            if Exchange1BP - Exchange2AP1 == Exchange1subExchange2:
                Exchange1BPAC, Exchange1APAC, RealDifference=real_value(Exchange1BP,Exchange2AP1,Exchange1BPV,Exchange2AP1V)
                db_buckets(
                    Exchange1subExchange2, TS, Exchange1, Exchange1_LTP, Exchange1BP, Exchange1BPV, Exchange2,
                    Exchange2_LTP, Exchange2AP1, Exchange2AP1V,Exchange1BPAC, Exchange1APAC, RealDifference, Processing_Time
                )