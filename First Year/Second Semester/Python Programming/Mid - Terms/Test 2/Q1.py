from dataclasses import dataclass
import random


@dataclass
class Bank:
    def __init__(self,accounts: dict = {}, account_numbers:list =[],transaction_history:list =[]):
        self.accounts = accounts
        self.account_numbers = account_numbers
        self.transaction_history = transaction_history

    def create_account(self, customer_name: str ='', initial_balance: float =0):
        list_accounts = self.accounts
        list_accounts[customer_name.title()] = initial_balance
        account_number = random.randint(1000000, 9999999)
        self.account_numbers.append([account_number, customer_name])

    def deposit(self, customer_name:str='', amount:float=0):
        transaction_history = self.transaction_history
        if customer_name in self.accounts.keys():
            self.accounts[customer_name] += amount
            transaction_history.append([customer_name, f'Deposit: {amount}'])

        else:
            print('Account not found. Try again.')


    def withdraw(self, customer_name:str ='', amount:float =0):
        if customer_name in self.accounts.keys():
            if amount <= self.accounts[customer_name] and self.accounts[customer_name] > 0:
                self.accounts[customer_name] -= amount
                self.transaction_history.append([customer_name, f'Withdrawal: {amount}'])

            else:
                print('Insufficient funds. Try again.')

        else:
            print('Account not found. Try again.')

    def get_balance(self, customer_name: str):
        list_accounts = self.accounts

        if customer_name in list_accounts:
            return list_accounts[customer_name]
        else:
            return 'Customer not found. Try again.'

    def get_transaction_history(self, customer_name:str=''):
        transaction_history = self.transaction_history
        for transaction in transaction_history:
            if customer_name == transaction[0]:
                return transaction[1]
            else:
                return 'Customer not found. Try again.'

    def transfer(self, sender_name: str, receiver_name: str, amount: float):
        list_accounts = self.accounts
        transaction_history = self.transaction_history
        # if sender_name in list_accounts:
        #     if list_accounts[sender_name] > 0 and amount <= list_accounts[sender_name]:
        list_accounts[sender_name] -= amount
        transaction_history.append([sender_name, f'Transfer: -{amount} to {receiver_name}'])
        #     else:
        #         print('Insufficient funds. Try again.')
        # else:
        #     print('Customer not found. Try again.')

#
# @dataclass
# class SavingsAccount(Bank):
#     interest_rate: float = 0
#
#     def get_balance(self, customer_name: str):
#         accounts = Bank.accounts={}
#         if customer_name in accounts:
#             return round(accounts[customer_name])
#         else:
#             return 'Customer not found. Try again.'
#
#     def calculate_interest(self, customer_name: str):
#         accounts = Bank.accounts
#         if customer_name in accounts:
#             interest = accounts[customer_name] * self.interest_rate
#             accounts[customer_name] = accounts[customer_name] + interest


def main():
    bank = Bank()
    bank.create_account('Alice', 1000)

    # savings_account = SavingsAccount()
    # savings_account.interest_rate = 0.05
    # savings_account.create_account('Bob', 2000)
    # savings_account.deposit('Bob', 1000)
    # savings_account.calculate_interest('Bob')
    # print(savings_account.get_balance('Bob'))
    #
    # print()

    bank.deposit('Alice', 500)
    bank.withdraw('Alice', 200)
    bank.transfer('Alice', 'Bob', 300)
    print(bank.get_balance('Alice'))

    print()

    print(bank.get_transaction_history('Alice'))

    print()

    # savings_account.deposit('Bob', 300)
    # print(savings_account.get_balance('Bob'))


if __name__ == '__main__':
    main()
