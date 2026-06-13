from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: str
    name: str
    age: int
    risk_profile: str
    country: str