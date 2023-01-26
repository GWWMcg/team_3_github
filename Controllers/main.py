from fastapi import FastAPI
from Services.services import Services
from Models.models import Account
app = FastAPI()

service = Services()

@app.get("/account")
async def get_accounts():
    return service.get_accounts()

@app.post("/account")
async def open_account(account: Account):
    return service.open_account(account)