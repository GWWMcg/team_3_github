from Models.models import Address, Account, Customer
from Repository.repository import AccountRepository, CustomerRepository, AddressRepository

class AccountService:
    def __init__(self, account_repository = AccountRepository()): # why cant just set self.account_service to AccountRepository()?
        self.account_repository = account_repository

    def open_account(self, account: Account) -> Account:

        address = self.repository.insert_address(account.customer.address)

        account.customer.address = address

        customer = self.repository.insert_customer(account.customer)

        account.customer = customer

        return self.repository.insert_account(account)
    
    def get_accounts(self):
        return self.account_repository.get_accounts()

    def get_account(self, account_id):
        return self.account_repository.get_account(account_id)
    

class AddressService:
    def __init__(self, address_repository = AddressRepository()):
        self.address_repository = address_repository
    
    def insert_address(self, address: Address) -> Address:
        return self.address_repository.insert_address(address)

    def get_addresses(self):
        return self.address_repository.get_addresses()
    
    def get_address(self, address_id):
        return self.address_repository.get_address(id=address_id)

class CustomerService:
    def __init__(self, customer_repository = CustomerRepository()):
        self.customer_repository = customer_repository

    def insert_customer(self, customer: Customer) -> Customer:
        return self.customer_repository.insert_customer(customer=customer)

    def get_customers(self):
        return self.customer_repository.get_customers()

    def get_customer(self, customer_id):
        return self.customer_repository.get_customer(id=customer_id)

# class Services:

#     def __init__(self, repository = Repository()):
#         self.repository = repository

#     def open_account(self, account: Account) -> Account:

#         address = self.repository.insert_address(account.customer.address)

#         account.customer.address = address

#         customer = self.repository.insert_customer(account.customer)

#         account.customer = customer

#         return self.repository.insert_account(account)

#     def get_accounts(self):
#         return self.repository.get_accounts()