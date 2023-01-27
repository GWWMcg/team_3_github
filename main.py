from fastapi import FastAPI
from Services.services import AddressService, AccountService, AddressRepository
from Models.models import Account, Address, Customer
app = FastAPI()

@app.get("/list_account")
async def get_accounts():
    return AccountService.get_accounts()

@app.get("/accounts")
async def get_accounts(id: str):
    return AccountService.get_account(id=id)

@app.post("/open_account")
async def open_account(account: Account):
    return AccountService.open_account(account)

app.get('/list_addresses')
async def get_addresses():
    return AddressService.get_addresses()

app.get('/address')
async def get_addresses(id):
    return AddressService.get_address(id=id)

app.post('/open_address')
async def open_address(address: Address):
    return AddressService.insert_address(address)

# app.get("/")