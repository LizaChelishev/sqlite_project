from Customer import Customer
from CustomerDataAccess import CustomerDataAccess

def print_menu():
    print('\
    1. Get all customers \n\
    2. Get customer by id \n\
    3. Insert customer \n\
    4. Delete customer \n\
    5. Update customer  \n\
    6. Exit')

def get_user_selection():
    while True:
        selection_string = input('Please choose a number from the menu: ')
        if selection_string.isnumeric():
            selection = int(selection_string)
            if selection in range(1, 7):
                break
    return selection

def process_user_selection(selection, customer_data_access):
    if selection == 1:
        customer_data_access.print_all_customers()
    elif selection == 2:
        id = int(input('Please enter the customer id: '))
        current_customer = customer_data_access.get_customers_by_id(id)
        if current_customer is not None:
            print(f'The customer with id {id} is {current_customer}')
        else:
            print(f'customer with id: {id} does not exist')
    elif selection == 3:
        id = int(input('Please enter the customer id: '))
        current_customer = customer_data_access.get_customers_by_id(id)
        if current_customer is not None:
            print(f'Error, customer id {id} already exist')
        else:
            fname = input('Please enter the customer first name: ')
            lname = input('Please enter the customer last name: ')
            list_customers = customer_data_access.get_customers_by_first_name_and_last_name(fname, lname)
            answer = 'yes'
            if len(list_customers) != 0:
                answer = input('Are you sure? ')
            if answer == 'yes':
                address = input('Please enter the customer address: ')
                mobile = int(input('Please enter the customer mobile: '))
                customer = Customer(id, fname, lname, address, mobile)
                customer_data_access.insert_customer(customer)

    elif selection == 4:
        id = int(input('Please enter the customer id: '))
        customer_data_access.delete_customer(id)

    elif selection == 5:
        current_id = int(input('Please enter the current customer id: '))
        current_customer = customer_data_access.get_customers_by_id(current_id)
        if current_customer is None:
            print(f'Error, customer id {id} does not exist')
        else:
            id = int(input('Please enter the new id: '))
            fname = input('Please enter the new first name: ')
            lname = input('Please enter the new last name: ')
            address = input('Please enter the new address: ')
            mobile = int(input('Please enter the new mobile: '))
            customer = Customer(id, fname, lname, address, mobile)
            customer_data_access.update_customer(current_id, customer)

    elif selection == 6:
        customer_data_access.close_connection()


def main():
    customer_data_access = CustomerDataAccess('C:\\Users\\Liza\\customer.db')
    while True:
        print_menu()
        selection = get_user_selection()
        process_user_selection(selection, customer_data_access)
        if selection == 6:
            break

main()
