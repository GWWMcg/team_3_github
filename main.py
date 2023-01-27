from fastapi import FastAPI
from Services.services import AddressService, AccountService, AddressRepository
from Models.models import Account, Address, Customer
app = FastAPI()

acc_ser = AccountService()
add_ser = AddressService()

@app.get("/list_account")
async def get_accounts():
    return acc_ser.get_accounts()

@app.get("/accounts")
async def get_accounts(id: str):
    return acc_ser.get_account(id=id)

@app.post("/open_account")
async def open_account(account: Account):
    return acc_ser.open_account(account)

@app.get('/list_addresses')
async def get_addresses():
    return add_ser.get_addresses()

@app.get('/address')
async def get_addresses(id):
    return add_ser.get_address(id=id)

@app.post('/open_address')
async def open_address(address: Address):
    return add_ser.insert_address(address)

# app.get("/")