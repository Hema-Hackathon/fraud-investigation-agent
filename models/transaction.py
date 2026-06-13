from pydantic import BaseModel

class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    amount: float
    transaction_type: str
    timestamp: str