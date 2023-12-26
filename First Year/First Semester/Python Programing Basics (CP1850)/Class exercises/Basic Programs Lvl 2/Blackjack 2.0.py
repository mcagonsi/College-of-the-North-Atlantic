# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:44:07 2023

@author: Michael.Agonsi
"""


print('BLACKJACK!')
print('Blackjack payout is 3:2')
print('Enter \'x\' for bet to exit')
print('\n\n')


loop = True
while loop == True:
    s_money = float(input('Starting money:\t'))
    b_amount = input('Bet amount:\t\t')
    if b_amount == 'x':
        print('Bye!')
        break
        
    else:
        if (s_money < 5 or s_money > 10000)
        elif((b_amount >= 5 and b_amount <= 1000) and (b_amount < s_money):
            b_amount = float(b_amount)
            option = input('Blackjack, win, push, or loss? (b/w/p/l): ')
            blackjack = float((b_amount*1.5)+s_money)
            win = float(s_money + b_amount) 
            push = float(s_money) 
            lose = float (s_money - b_amount) 
            if option == 'b':
                s_money = blackjack
                print(f"Money:  {blackjack:.2f}")
            elif option == 'w':
                s_money = win
                print(f"Money:  {win:.2f}")
            elif option == 'p':
                s_money = push
                print(f"Money:  {push:.2f}")
            elif option == 'l':
                s_money = lose
                print(f"Money:  {lose:.2f}")
    
        
        