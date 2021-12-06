import sqlite3


class CustomerDataAccess:

    def __init__(self, db_file_path):
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def print_all_customers(self):
        self.cursor.execute('SELECT * FROM CUSTOMER')
        for customer in self.cursor:
            print(customer)

    def insert_customer(self, customer):
        self.cursor.execute(f'INSERT INTO CUSTOMER VALUES ({customer.id}, "{customer.fname}", "{customer.lname}", ' +
                       f'"{customer.address}", {customer.mobile})')

    def delete_customer(self, id):
        print('Delete customer with id:' + str(id))
        self.cursor.execute(f'DELETE FROM CUSTOMER WHERE id = {id}')

    def get_all_customers(self):
        self.cursor.execute('SELECT * FROM CUSTOMER')
        list_customers = []
        for customer in self.cursor:
            list_customers.append(customer)
        return list_customers

    def get_customers_by_id(self, id):
        self.cursor.execute(f'SELECT * FROM CUSTOMER WHERE id = {id}')
        customer = None
        for customer in self.cursor:
            break
        return customer

    def update_customer(self, id, customer):
        self.cursor.execute(
            f'UPDATE CUSTOMER SET ID = {customer.id},fname = "{customer.fname}" , lname = "{customer.lname}", ' +
            f'ADDRESS = "{customer.address}", MOBILE = {customer.mobile} WHERE id = {id}')

    def close_connection(self):
        self.connection.commit()
        self.connection.close()