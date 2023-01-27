import configparser
from distutils.command.config import config
import psycopg2

class AccountRepository:
    def __init__(self):
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

    def get_accounts(self):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM account
                    """
                )
                accounts = cursor.fetchall()
        return accounts

    def insert_account(self, account):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO account 
                        (account_number, customer_id, current_balance) VALUES
                        (%(account_number)s, %(customer_id)s, %(current_balance)s)
                        RETURNING id
                    """, {
                    'account_number': account.account_number,
                    'customer_id': account.customer,
                    'current_balance': account.current_balance
                })
                account = cursor.fetchone()[0]
        return account

    def get_account(self, account_id): # TODO: no check if the account id is not there
        with self.open_connection() as db:
            with db.cursor as cursor:
                cursor.execute("""
                    SELECT * FROM account
                    WHERE id = %(account_id)s
                        
                """, {
                    'account_id': account_id
                })
                account = cursor.fetchone()[0] # putting return in here may solve todo issue above
        return account

class AddressRepository:
    def __init__(self):
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

    def insert_address(self, address):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address 
                        (address, city, state, zip_code) VALUES
                        (%(address)s, %(city)s, %(state)s, %(zip_code)s)
                        RETURNING id
                    """, {
                    'address': address.address,
                    'city': address.city,
                    'state': address.state,
                    'zip_code': address.zip_code
                })
                address = cursor.fetchone()[0]
        return address

    def get_addresses(self):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM address
                    """
                )
                addresses = cursor.fetchmany(1)
        return addresses

    def get_address(self, id):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM address
                    WHERE id  = %(address_id)s
                    """, {
                        'address_id': id 
                    }
                )
                address = cursor.fetchmany(1)
        return address

class CustomerRepository:
    def __init__(self):
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

    def insert_customer(self, customer):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO customer 
                        (first_name, last_name, address_id, email_address) VALUES
                        (%(first_name)s, %(last_name)s, %(address_id)s, %(email_address)s)
                        RETURNING id
                    """, {
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'address_id': customer.address,
                    'email_address': customer.email_address
                })
                print(customer)
                customer = cursor.fetchone()[0]
        return customer
    
    def get_customers(self):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM customer
                    """
                )
                customers = cursor.fetchmany(1)
        return customers

    def get_customer(self, id):
        with self.open_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM customer
                    WHERE id  = %(customer_id)s
                    """, {
                        'address_id': id 
                    }
                )
                address = cursor.fetchmany(1)
        return address   

# class Repository:
    
#     def __inti__(self):
#         config = configparser.ConfigParser()
#         config.read('config.ini')

#         self.HOST = config['postgres']['host']
#         self.USER = config['postgres']['user']
#         self.PASSWORD = config['postgres']['password']
#         self.DATABASE = config['postgres']['database']

#     def open_connection(self):
#         conn = psycopg2.connect(    
#             host=self.HOST,
#             user=self.USER,
#             password=self.PASSWORD,
#             dbname=self.DATABASE
#         )
#         return conn

#     def get_accounts(self):
#         with self.open_connection() as db:
#             with db.cursor() as cursor:
#                 cursor.execute("""
#                     SELECT * FROM account
#                     """
#                 )
#                 accounts = cursor.fetchmany(1)

#         return accounts

#     def insert_address(self, address):
#         with self.open_connection() as db:
#             with db.cursor() as cursor:
#                 cursor.execute("""
#                     INSERT INTO address 
#                         (address, city, state, zip_code) VALUES
#                         (%(address)s, %(city)s, %(state)s, %(zip_code)s)
#                         RETURNING id
#                     """, {
#                     'address': address.address,
#                     'city': address.city,
#                     'state': address.state,
#                     'zip_code': address.zip_code
#                 })
#                 address = cursor.fetchone()[0]

#         return address

#     def insert_customer(self, customer):
#         with self.open_connection() as db:
#             with db.cursor() as cursor:
#                 cursor.execute("""
#                     INSERT INTO customer 
#                         (first_name, last_name, address_id, email_address) VALUES
#                         (%(first_name)s, %(last_name)s, %(address_id)s, %(email_address)s)
#                         RETURNING id
#                     """, {
#                     'first_name': customer.first_name,
#                     'last_name': customer.last_name,
#                     'address_id': customer.address,
#                     'email_address': customer.email_address
#                 })
#                 print(customer)
#                 customer = cursor.fetchone()[0]

#         return customer

#     def insert_account(self, account):
#         with self.open_connection() as db:
#             with db.cursor() as cursor:
#                 cursor.execute("""
#                     INSERT INTO account 
#                         (account_number, customer_id, current_balance) VALUES
#                         (%(account_number)s, %(customer_id)s, %(current_balance)s)
#                         RETURNING id
#                     """, {
#                     'account_number': account.account_number,
#                     'customer_id': account.customer,
#                     'current_balance': account.current_balance
#                 })
#                 account = cursor.fetchone()[0]

#         return account