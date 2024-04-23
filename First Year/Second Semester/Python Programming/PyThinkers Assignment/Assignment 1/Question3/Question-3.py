from dataclasses import dataclass
import csv

@dataclass
class Customer:
    """
    Class named 'Customer' that stores varying customer information attributes
    """
    id: int = 0
    firstName: str = ''
    lastName: str = ''
    company: str = ''
    address: str = ''
    city: str = ''
    state: str = ''
    zip: str = ''

    @property
    def fullName(self):
        """
        Property that returns a formatted full-name string from the Customer
        attributes 'firstName' & 'lastName'.
        """
        return f"{self.firstName} {self.lastName}"

    @property
    def fullAddress(self):
        """
        Property that returns a formatted string of attributes 'address',
        'city', 'state', and 'zip'. Adds an extra line for 'company' attribute
        if the info is available.
        """
        if self.company == '':
            return f"{self.address} \n{self.city}, {self.state} {self.zip}"
        else:
            return f"{self.company} \n{self.address} \n{self.city}, {self.state} {self.zip}"


def getCustomers(object_list):
    """
    Function that reads individual customer information from the csv file
    'customers.csv' into a 'Customer' object and appends each customer to an
    object_list.

    :param object_list: empty object list
    """
    with open('customers.csv', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            object_list.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def title():
    """
    Function that prints the program title
    """
    print("Customer Viewer")

def looper_check():
    """
    Asks the user if they would like to continue, then checks the loop
    variable to make sure proper input was received, finally returns loop.
    :return loop:
    """
    loop = input('\nContinue? (y/n): ')
    while loop.lower() != 'y' and loop.lower() != 'n':
        print("Please enter 'y' or 'n'.")
        loop = input('\nContinue? (y/n): ')
    return loop


def main():
    """
    Main function of the program. Creates an empty object list, then calls the
    getCustomers() function to load 'Customer' objects to the list. Prints program
    title. Checks for Customer id matching the prompted customer input, if no
    customer is found, prompts the user as such. Loops until the user would
    like to stop, and checks for proper loop input.
    """
    object_list = []
    getCustomers(object_list)
    title()
    loop = 'y'
    while loop.lower() == 'y':
        cust_id = input('\nEnter customer ID: ')
        access = False
        for obj in object_list:
            if cust_id == obj.id:
                print()
                print(obj.fullName)
                print(obj.fullAddress)
                loop = looper_check()
                access = True
                #Sets access to True if customer is found
        if access == False:
            #If access is still False, no customer found.
            print("\nNo customer with that ID")
            loop = looper_check()
    print()
    print("Bye!")


if __name__ == '__main__':
    main()