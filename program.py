from Customer import Customer
import sqlite3


def print_all_customers(cursor):
    cursor.execute('SELECT * FROM CUSTOMER')
    for customer in cursor:
        print(customer)


def insert_customer(cursor, customer):
    cursor.execute(f'INSERT INTO CUSTOMER VALUES ({customer.id}, "{customer.fname}", "{customer.lname}", ' +
                   f'"{customer.address}", {customer.mobile})')


def delete_customer (cursor, id):
    cursor.execute(f'DELETE FROM CUSTOMER WHERE ID = {customer.id}')


def get_all_customers (cursor):
    cursor.execute('SELECT * FROM CUSTOMER')
    list_customers =[]
    for customer in cursor:
        list_customers.append(customer)
    return list_customers



connection = sqlite3.connect('C:\\Users\\Liza\\customer.db')
cursor = connection.cursor()
print_all_customers(cursor)
customer = Customer(1, 'Liza', 'Chelishev', 'Tel Aviv', 66657478)
delete_customer(cursor, 1)
insert_customer(cursor, customer)
list_customers = get_all_customers(cursor)
print(list_customers)
connection.commit()
connection.close()