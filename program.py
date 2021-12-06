from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
import sqlite3

def main():
    customer_data_access = CustomerDataAccess('C:\\Users\\Liza\\customer.db')
    customer_data_access.print_all_customers()
    customer = Customer(1, 'Liza', 'Chelishev', 'Tel Aviv', 66657478)
    customer2 = Customer(2, 'May', 'Chelishev', 'Tel Aviv', 88785735)
    customer3 = Customer(3, 'Tref', 'Oren', 'Raanana', 77678597)
    customer_data_access.delete_customer(1)
    customer_data_access.insert_customer(customer)
    customer_data_access.delete_customer(2)
    customer_data_access.insert_customer(customer2)
    customer_data_access.delete_customer(3)
    customer_data_access.insert_customer(customer3)
    list_customers = customer_data_access.get_all_customers()
    print(list_customers)
    custest = customer_data_access.get_customers_by_id (2)
    print(f'The customer with id 2 is {custest}')
    updated_customer = Customer(8, 'Ghyej', 'Pokjh', 'Jersalem', 555214563)
    customer_data_access.update_customer(2, updated_customer)
    customer_data_access.print_all_customers()
    customer_data_access.close_connection()

main()
