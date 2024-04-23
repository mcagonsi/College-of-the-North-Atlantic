from dataclasses import dataclass


@dataclass
class Person:  # creates the Person Class
    FName: str
    LName: str
    _email: str

    @property
    def fullName(self):  # returns the firstname and lastname as fullname str
        return self.FName + ' ' + self.LName

    @property
    def email(self):
        return self._email


@dataclass
class Customer(Person):  # creates the Customer Class
    Number: str

    def __str__(self):  # overrides the string representation of the class
        return f'''CUSTOMER \n{'Name:':10} {self.fullName} \n{'Email:':10} {self.email} \n{'Number:':10} {self.Number}'''


@dataclass
class Employee(Person):  # creates the Employee Class
    SSN: str

    def __str__(self):  # overrides the string representation of the class
        return f'''EMPLOYEE \n{'Name:':10} {self.fullName} \n{'Email:':10} {self.email} \n{'SSN:':10} {self.SSN}'''


def title():
    print('Customer/Employee Data Entry')
    print()


def fName():
    while True:
        try:
            f_name = input('First Name: ').title()
            return f_name
            break
        except ValueError:
            print('Invalid data type.')
            print()


def lName() -> str:
    # handles errors for input and returns the str value
    while True:
        try:
            l_name = input('Last Name: ').title()
            return l_name
            break
        except ValueError:
            print('Invalid data type.')
            print()


def email() -> str:
    # handles errors for input and returns the str value
    while True:
        try:
            email = input('Email: ')
            if '@' in email and len(email) > 5:
                if '.' in email:
                    return email
                    break
                else:
                    print('Invalid email address.')
                    print()
            else:
                print('Invalid email address')
                print()
        except ValueError:
            print('Invalid data type.')
            print()


def ssn() -> str:
    # handles errors for input and returns the str value
    while True:
        try:
            ssn = input('SSN: ')
            if '-' in ssn:
                return ssn
                break
            else:
                print('Please enter ssn in the specified format: xxx-xx-xxxx')
                print()
        except ValueError:
            print('Invalid data type.')
            print()


def number() -> str:
    # handles errors for input and returns the str value
    while True:
        try:
            number = input('Number: ')
            return number
            break
        except ValueError:
            print('Invalid data type')
            print()


def main():
    title()

    again = 'y'
    while again == 'y':
        while True:
            entry = input('Customer or employee ? (c/e): ').lower()
            print()
            print('DATA ENTRY')
            if entry == 'c':
                person = Customer(fName(), lName(), email(), number())
                print()
                if isinstance(person, Customer):  # checks if the object is an instance of the specified class
                    print(person)
                    break

            elif entry == 'e':
                person = Employee(fName(), lName(), email(), ssn())
                print()
                if isinstance(person, Employee):  # checks if the object is an instance of the specified class
                    print(person)
                    break

            else:
                print('Invalid Input!')

        print()
        again = input('Continue? (y/n): ').lower()
        print()

    print('Bye!')


if __name__ == '__main__':
    main()
