# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:14:34 2023

@author: Michael.Agonsi
"""

print('BLACKJACK!')
print('Blackjack payout is 3:2')
print('\n\n')


s_money = int(input('Starting money:\t'))
b_amount = int(input('Bet amount:\t\t'))

print('\n\n')
print('ENDING MONEY FOR A...')

blackjack = float((b_amount*1.5)+s_money)
win = float(s_money + b_amount)
push = float(s_money)
lose = float (s_money - b_amount)

print(f"Blackjack:\t\t\t{blackjack:.2f}")
print(f"Win:\t\t\t\t{win:.2f}")
print(f"Push:\t\t\t\t{push:.2f}")
print(f"Lose:\t\t\t\t{lose:.2f}")
print("\n\nBye!")