from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
