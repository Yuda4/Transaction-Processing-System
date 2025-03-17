import redis
import json
from schemas import TransactionResponse

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

def set_transaction_cache(txn):
    txn_dict = {
        "id": txn.id,
        "user_id": txn.user_id,
        "amount": txn.amount,
        "currency": txn.currency,
        "status": txn.status,
        "created_at": txn.created_at.isoformat(),  # Convert datetime to string
    }
    redis_client.set(f"txn:{txn.id}", json.dumps(txn_dict), ex=3600)

def get_transaction_cache(txn_id):
    txn_data = redis_client.get(f"txn:{txn_id}")
    if txn_data:
        return TransactionResponse(**json.loads(txn_data))
    return None
