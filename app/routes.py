from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Transaction
from schemas import TransactionCreate, TransactionResponse
from cache import get_transaction_cache, set_transaction_cache

router = APIRouter()


@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(txn: TransactionCreate, db: Session = Depends(get_db)):
    new_txn = Transaction(**txn.dict())
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    set_transaction_cache(new_txn)
    return new_txn


@router.get("/transactions/{txn_id}", response_model=TransactionResponse)
def get_transaction(txn_id: int, db: Session = Depends(get_db)):
    txn = get_transaction_cache(txn_id)
    if txn:
        return txn

    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()
    if txn:
        set_transaction_cache(txn)
    return txn
