import sys
sys.path.append('../')
from dataclasses import dataclass
from objs import entity as E


BANK = E.Bank('Tesla Inc Bank','2 Skywalket Avenue', 'Oacis', 'Marsian City', 'Mars','184 3DE')
# print(BANK.accounts)
# print(BANK.customers)
# print(BANK.accountsids)
#
# BANK.validateAccountNumber()
@dataclass
class API:
    _name=BANK.bankName
    _status = None
    _headers = BANK.bankName
    _body = BANK

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status
    def get(self,accountNumber):
        bank_name = self._headers
        account, customer = BANK.validateAccountNumber(accountNumber)
        if account != None and customer != None:
            self._status = 200
            return bank_name,account,customer
        else:
           self._status = 404
    def post(self,Transaction):
        Recipient = self._body.accounts[Transaction.toAccountNumber]
        status = Recipient.creditAccount(Transaction)
        if status is True:
            self._status = 200
        else:
            self._status = 400

        # a credit alert should always deposit into the checkings account,external client will be gotten from the api.get() return


        pass


# api = API()
# api.get(35323480)

