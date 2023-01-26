from Accounts.Models.models import Account
from Accounts.Repository.repository import Repository

class Services:

    def __init__(self, repository = Repository()):
        self.repository = repository

    def open_account(self, account: Account) -> Account:

        address = self.repository.insert_address(account.customer.address)

        account.customer.address = address

        customer = self.repository.insert_customer(account.customer)

        account.customer = customer

        return self.repository.insert_account(account)

    def get_accounts(self):
        return self.repository.get_accounts()