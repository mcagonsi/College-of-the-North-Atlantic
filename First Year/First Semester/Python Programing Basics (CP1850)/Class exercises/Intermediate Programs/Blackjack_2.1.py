# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:36:37 2023

@author: Michael.Agonsi
"""

import random

def title_and_option():
    '''
    prints title of program

    Returns
    -------
    None.

    '''
    print('BLACKJACK!')
    print('Blackjack payout is 3:2')
    print('Enter \'x\' for bet to exit')
    print('\n\n')

def start_money():
    '''
    Collects input for starting money and returns it

    Returns
    -------
    s_money : TYPE
        DESCRIPTION.

    '''
    while True:
        s_money = float(input('Starting money:\t'))
        if s_money < 5:
            print ('Minimum amount of starting money should be 5')
        elif s_money > 10000:
            print ('Maximum amount of starting money should be 10,000')
        else:
            return s_money

def betting_calculation(s_money):
    '''
    checks to continue or exit the program
    randomly assigns odds and calculates the bet

    Parameters
    ----------
    s_money : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    loop = True
    while loop == True:
        b_amount = input('Bet amount:\t\t')
        if b_amount == 'x':
            print('Bye!')
            break
        elif float(b_amount) < 5 :
            print('Minimum bet amount should be 5')
            continue
        elif float(b_amount) > s_money:
            print('The bet can\'t be greater than player\'s current amount of money')
            continue
                     
        elif float(b_amount) > 1000:
            print ('Maximum bet amount should be 1000')
            continue
       
            
        else:
           
            b_amount = float(b_amount)

            odds = random.randint(1,100)
            blackjack = float((b_amount*1.5)+s_money)
            win = float(s_money + b_amount) 
            push = float(s_money) 
            lose = float (s_money - b_amount)
           
            if odds >= 95 :
                s_money = blackjack
                print('You got a blackjack!')
                print(f"Money:  {blackjack:.2f}\n")
            elif odds >=58 and odds < 95:
                s_money = win
                print('You won.')
                print(f"Money:  {win:.2f}\n")
            elif odds >= 49 and odds < 58:
                s_money = push
                print('You pushed.')
                print(f"Money:  {push:.2f}\n")
            else :
                s_money = lose
                print('You lost.')
                print(f"Money:  {lose:.2f}\n")

if __name__ == '__main__':
    title_and_option()
    money_start = start_money()
    betting_calculation(money_start)
    
        