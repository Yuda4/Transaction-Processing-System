from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: str
    amount: float
    currency: str

class TransactionResponse(TransactionCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
