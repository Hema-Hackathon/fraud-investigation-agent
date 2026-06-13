from pydantic import BaseModel

class Behavior(BaseModel):
    customer_id: str
    new_device: bool
    midnight_transaction: bool
    vpn_used: bool