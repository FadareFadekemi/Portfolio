from sqlalchemy import Column, Integer, String, Float
from database import Base


class input(Base):
    __tablename__ = "Fraud_detection"
    transdatetrans_time = Column(String,primary_key = True, index = True)
    amt = Column(Float)
    dob = Column(String)
    long = Column(String)
    lat = Column(String)
    merch_long = Column(Float)
    merch_lat = Column(Float)
    merchant = Column(String)
    category = Column(String)

