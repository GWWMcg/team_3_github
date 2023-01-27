import unittest
from Models.models import Account, Address, Customer
from Repository.repository import CustomerRepository, AddressRepository, AccountRepository
import configparser
from distutils.command.config import config
import psycopg2

class RepositoryTest(unittest.TestCase):
    def __init__(self):
        self.accountRepo = AccountRepository()
        self.addressRepo = AddressRepository()
        self.customerRepo = CustomerRepository()
        self.HOST = 'team-3-database.ckokfd9swhyk.us-west-2.rds.amazonaws.com'
        self.USER = 'team_3_user'
        self.PASSWORD = 'team3password'
        self.DATABASE = 'postgres'

    def open_connection(self):
        conn = psycopg2.connect(    
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            dbname=self.DATABASE
        )
        return conn 
        
    def insertAccount(self):
        self.accountRepo.insert_account(Account(account_number='1234', customer=Customer(id=1234), current_balance=12.34))
        
    def getAccounts(self):
        self.accountRepo.get_accounts()

    def getAccount(self):
        self.accountRepo.get_account(account_id=1)

    def insertAddress(self):
        self.addressRepo.insert_address(Address(address='test street', city='test city', state='CA', zip_code='92203'))
    
    def getAddresses(self):
        self.addressRepo.get_addresses()
    
    def getAddress(self):
        self.addressRepo.get_address(id=1)
    
    def insertCustomer(self):
        self.customerRepo.insert_customer(Customer(first_name='Tester', last_name='Testington', address=Address(address='test street', city='test city', state='CA', zip_code='92203'), email_address='test.testington@gmail.com'))

    def getCustomers(self):
        self.customerRepo.get_customers()
    
    def getCustomer(self):
        self.customerRepo.get_customer(id=1)