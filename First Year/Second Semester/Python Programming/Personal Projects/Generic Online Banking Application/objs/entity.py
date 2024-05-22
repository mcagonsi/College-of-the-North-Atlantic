from dataclasses import dataclass
from datetime import datetime
import sys
sys.path.append("..")
from DBs import writeDB as wdb
from DBs import readDB as rdb
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
import mysql.connector as db
con = db.connect(host='localhost',user='root',passwd='root',port=3306,database='bankdb')
c = con.cursor()

@dataclass
class Bank:
    _BankName: str
    _Employees:dict
    _Customers:dict
    _Accounts:dict
    _Address: str
    _City: str
    _Country: str
    _PostalCode: str
    _Branch:str

    @property
    def bankName(self):
        return self._BankName

    @property
    def employees(self):
        return self._Employees

    @property
    def customers(self):
        return self._Customers
    @property
    def accounts(self):
        return self._Accounts

    # def __post_init__(self):
    #     self._Accounts = readaccts()
    #     self._Customers = readcustomer()
    #     self._Employees = readEmployees()

    def validateCustomersAccount(self,value):
        pass
        # if value in self._Accounts # this is to validate for creating an online account or logging in
        #     return True
    def validateAccountNumber(self,value):
        pass
       # if value in self._Accounts: # this is to validate customer account exists for the external client to return the name of the client during transactions


@dataclass
class AccountType:
    _ID:int
    _Name = ''

    @property
    def id(self):
        return self._ID
    @property
    def name(self):
        return self._Name


    def __post_init__(self):

        query = 'select * from accounttype;'
        c.execute(query)
        types = c.fetchall()
        for t in types:
            if self._ID == t[0]:
                self._Name = t[1]

@dataclass
class Accounts:
    _ID:int
    _Accounts = {}
    _customerID:int


    def __post_init__(self):
        CON = db.connect(host='localhost', user='root', passwd='root', port=3306, database='bankdb')
        C = CON.cursor()

        getaccounts = 'select * from account where Accounts_ID = %s '
        C.execute(getaccounts, (self._ID,))
        Accounts = C.fetchall()
        for a in Accounts:
            if a[2] ==1:
                self._Accounts[a[0]] = Account(a[0],a[1],a[2],AccountType(a[3]),a[4])
        CON.close()

        #should initialize the _Accounts to get all accounts with respective customerID and AccountsID from the database

    def getTotalBalance(self):
        pass
        # should calculate total balance of all relevant accounts
    def showAccounts(self):
        return self._Accounts

        #shows all the accounts owned by the customer
    def selectAccount(self, value):
        pass
        #selects the desired account to be used for debit transactioins




@dataclass
class Account:
    _AccountNumber:int # this is written in the database as union of the accountsID and any random generated 4 numbers
    _Balance: float
    _Active: bool
    _AccountType: AccountType
    _AccountsID: int




    @property
    def accountNumber(self):
        return self._AccountNumber
    @property
    def accountsID(self):
        return self._AccountsID

    @property
    def accountType(self):
        return self._AccountType
    @property
    def balance(self):
        return self._Balance
    @property
    def active(self):
        return self._Active

    def getBalance(self):
        return locale.currency(self._Balance,grouping=True)

    def creditAccount(self,value):
        cur_bal = float(self._Balance)
        self._Balance =cur_bal+ value
    def debitAccount(self,value):
        cur_bal = float(self._Balance)
        self._Balance = cur_bal - value

    def showTransactionHistory(self):
        rdb.getTransactionHistory(self)

        #Transactons = # instantiate from the Transaction history class based on the AccountNumber


@dataclass
class Transaction:
    _transactionID :int
    _AccountID : int
    _type :str
    _Amount :float
    _Date :datetime
    _FromBankName:str
    _From :str
    _FromAccountNumber:int
    _ToBankName: str
    _To:str
    _ToAccountNumber:int
    _status : str

    # based on the account number

    @property
    def transactionID(self):
        return self._transactionID
    @property
    def type(self):
        return self._type

    @property
    def amount(self):
        return self._Amount

    @property
    def date(self):
        return self._Date
    @property
    def status(self):
        return self._status
    @property
    def accountID(self):
        return self._AccountID

    @property
    def fromBankName(self):
        return self._FromBankName

    @property
    def From(self):
        return self._From

    @property
    def fromAccountNumber(self):
        return self._FromAccountNumber

    @property
    def toBankName(self):
        return self._ToBankName

    @property
    def to(self):
        return self._To

    @property
    def toAccountNumber(self):
        return self._ToAccountNumber

@dataclass
class TransactionHistory:
    _accountsID:int
    _history = {}

    def __post_init__(self):
        c.fetchall()
        trnsHistory = rdb.getTransactionHistory(self._accountsID)
        if trnsHistory is not None:
            for t in trnsHistory:
                self._history[t.transactionID] = t
        else:
            pass

    @property
    def accountsID(self):
        return self._accountsID

    @property
    def history(self):
        return self._history







@dataclass
class OnlineBankingAccount:
    _ID:int
    _email:str
    _password:str
    _CustomerID:int
    _AccountsID:int

    def createOnlineBankingAccount(self):
        return wdb.createOnlineBankingAcct(self)
    def changeLoginDetails(self):
        return wdb.changeLoginDetails(self)


    @property
    def ID(self):
        return self._ID
    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def customerID(self):
        return self._CustomerID
    @property
    def accountsID(self):
        return self._AccountsID



def main():
    # acct=TransactionHistory(25887740)
    # print(acct.history)
    pass







if __name__ == '__main__':
    main()