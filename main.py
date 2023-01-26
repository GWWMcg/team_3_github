from fastapi import FastAPI
from Accounts.Services.services import Services
from Accounts.Models.models import Account
app = FastAPI()

service = Services()

@app.get("/account")
async def get_accounts():
    return service.get_accounts()

@app.post("/account")
async def open_account(account: Account):
    return service.open_account(account)