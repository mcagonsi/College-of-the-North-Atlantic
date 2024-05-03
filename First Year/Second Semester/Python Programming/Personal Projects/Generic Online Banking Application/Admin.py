from objs import actors as a
from objs import entity as e
import mysql.connector as db
con = db.connect(host='localhost',user='root',passwd='root',port=3306,database='bankdb')
c = con.cursor()
def openCustomerAccount():
    print("Opening Customer Account")
    print()
    fname = input("First Name: ").upper()
    lname = input("Last Name: ").upper()
    sex = input('Gender (M/F): ').upper()
    dob = input("Date of Birth (YYYY-MM-DD): ")
    relationship = input("Relationship (Single/Married/Divorced): ").upper()
    phone = input("Phone Number: ")
    stateOfOrigin = input("State of Origin: ")
    countryofOrigin = input("Country of Origin: ")
    streetAddress = input("House/Street Address: ")
    town = input("City: ")
    country = input("Country: ")
    postalcode = input("Postal Code: ")

    # initializing the customer class to write to database

    C = a.Customer(fname,lname,sex,dob,relationship,phone,stateOfOrigin,countryofOrigin,streetAddress,town,country,postalcode,0,0)

    parameters = (C.FirstName,C.LastName, C.Gender, C.DateOfBirth,C.Relationship, C.PhoneNumber, C.StateOfOrigin, C.CountryOfOrigin,C.StreetAddress, C.City, C.Country,C.PostalCode)

    query = 'insert into customer values (default,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s);'

    c.execute(query,parameters)
    con.commit()


    # Note that by default upon creation of a customer account only a chequing account is opened
    acct_type = e.AccountType(1).name
    getaccountNumber = '''Select AccountNumber from Customer_Accounts_Account where LastName=%s and PhoneNumber=%s and AccountType_ID=1'''
    c.execute(getaccountNumber,(C.LastName,C.PhoneNumber))
    accountNumber = c.fetchone()[0]

    print('ACCOUNT CREATED SUCCESSFULLY')
    print('ACCOUNT DETAILS')
    print('FULL NAME: ', C.FirstName, C.LastName)
    print('ACCOUNT TYPE: ', acct_type)
    print('ACCOUNT NUMBER: ', accountNumber)

def checkCustomerAccount():
    print('TO CHECK CUSTOMER ACCOUNT PLEASE PROVIDE THE CUSTOMER LAST NAME AND PHONE NUMBER')

    lname = input("Last Name: ").upper()
    phone = input("Phone Number: ")
    print()

    getaccountsID = "select accounts_id from customer_accounts_account where LastName=%s and PhoneNumber=%s"
    c.execute(getaccountsID,(lname,phone))
    accountsID = c.fetchone()
    if accountsID == None:
        print('CUSTOMER ACCOUNT NOT FOUND')

    else:

        accounts = 'select * from account where Accounts_ID=%s'
        c.execute(accounts,(accountsID[0],))
        accountDetails = c.fetchall()
        for acct in accountDetails:
            acct = e.Account(acct[0],acct[1],acct[2],e.AccountType(acct[3]).name,acct[4])
            if acct.active == 1:
                print('ACCOUNT NUMBER: ', acct.accountNumber)
                print('ACCOUNT TYPE: ', acct.accountType)
                print('ACCOUNT BALANCE: ', acct.balance)
                print()

def closeCustomerAccount():
    print('TO CLOSE CUSTOMER ACCOUNT PLEASE PROVIDE CUSTOMER LAST NAME, PHONE NUMBER AND DATE OF BIRTH')
    print()
    lname = input("Last Name: ").upper()
    phone = input("Phone Number: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")

    get

# c.execute('update account set Balance = 500 where AccountNumber = 53494789')
# con.commit()

checkCustomerAccount()




