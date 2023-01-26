from pydantic import BaseModel

# A Pydantic model
class Address(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zip_code: str

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email_address: str

class Account(BaseModel):
    id: int
    account_number: str
    customer: Customer
    current_balance: float