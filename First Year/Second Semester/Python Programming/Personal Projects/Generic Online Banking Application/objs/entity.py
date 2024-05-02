from dataclasses import dataclass
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
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

    def __post_init__(self):
        self._Accounts = readaccts()
        self._Customers = readcustomer()
        self._Employees = readEmployees()

    def validateCustomersAccount(self,value):
        if value in self._Accounts # this is to validate for creating an online account or logging in
            return True
    def validateAccountNumber(self,value):
        if value in self._Accounts: # this is to validate customer account exists for the external client to return the name of the client during transactions


@dataclass
class AccountType:
    _ID:int
    _Name:str

    @property
    def id(self):
        return self._ID
    @property
    def name(self):
        return self._Name

    def getTypeName(self):
        return self._Name # this should get the Account name based on the ID

@dataclass
class Accounts:
    _ID:int
    _Accounts = {}
    _customerID:int
    _OnlineAccountID= 0 #default if doesnt have an onlinebankingaccount on the database

    def __post_init__(self):
        #should initialize the _Accounts to get all accounts with respective customerID and AccountsID from the database

    def getTotalBalance(self):
        # should calculate total balance of all relevant accounts
    def showAccounts(self):
        #shows all the accounts owned by the customer
    def selectAccount(self, value):
        #selects the desired account to be used for debit transactioins
    def transactionAccount(self,value):
        #selects the desired account for internal transfer transactions



@dataclass
class Account:
    _AccountNumber:int # this is written in the database as union of the accountsID and any random generated 4 numbers
    _AccountsID: int
    _AccountType:AccountType
    _Balance:float
    _Active:bool

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
        self._Balance += value
    def debitAccount(self,value):
        self._Balance -= value
    def updateBalance(self):
        #should write balance to the database
    def showTransactionHistory(self):
        Transactons = # instantiate from the Transaction history class based on the AccountNumber


@dataclass
class Transaction:
    _transactionID:int
    _type:str
    _Amount:float
    _Date:datetime
    _status:str
    _AccountID:int # based on the account number

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



@dataclass
class Debit_Credit(Transaction):
    _SenderBankName:str
    _SenderName:str # customers account name
    _SenderAccountNumber:int
    _RecipientBankName:str
    _RecipientName = None # set based on the clients name verified from the bank
    _RecipientAccountNumber:int

    @property
    def senderBankName(self):
        return self._SenderBankName
    @property
    def senderName(self):
        return self._SenderName
    @property
    def senderAccountNumber(self):
        return self._SenderAccountNumber
    @property
    def recipientBankName(self):
        return self._RecipientBankName
    @property
    def recipientName(self):
        return self._RecipientName
    @property
    def recipientAccountNumber(self):
        return self._RecipientAccountNumber


@dataclass
class Transfer(Transaction):
    _FromAccountType:AccountType
    _FromBankName:str
    _FromAccountNumber:int
    _ToAccountType:AccountType
    _ToBankName:str
    _ToAccountNumber:int

    @property
    def fromAccountType(self):
        return self._FromAccountType

    @property
    def fromBankName(self):
        return self._FromBankName

    @property
    def fromAccountNumber(self):
        return self._FromAccountNumber

    @property
    def toAccountType(self):
        return self._ToAccountType
    @property
    def toBankName(self):
        return self._ToBankName
    @property
    def toAccountNumber(self):
        return self._ToAccountNumber













