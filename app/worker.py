import os

from celery import Celery
import time

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
celery_app = Celery("worker", broker=CELERY_BROKER_URL)


@celery_app.task
def process_transaction(txn_id):
    time.sleep(5)
    return f"Transaction {txn_id} processed."
