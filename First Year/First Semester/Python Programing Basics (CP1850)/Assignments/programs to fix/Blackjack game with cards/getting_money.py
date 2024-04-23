# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:48:11 2023

@author: Michael.Agonsi
"""

def read_s_money():
    
    with open('Money.txt', 'r') as money:
        ammount = money.read()
       
        return float(ammount)
def update_s_money(s_money):
    with open('Money.txt', 'w') as money:
        money.write(str(int(s_money)))

def buy_chips(s_money):
    print('Buy more chips ?' +
          '\n1. 10' +
          '\n2. 20' +
          '\n3. 50' +
          '\n4. 100' )
    chips_amount = [10,20,50,100]
    chip = int(input('Chip ammount: '))
    num_chips = int(input('Number of selected chip: '))
    i = chip - 1
    total = chips_amount[i] * num_chips
    while True:
        if total > 5 and total <= 5000:
            while True:
                ans = input(f'You want to buy {total} chips (y/n)?:').lower()
                if ans == 'y':
                    s_money += total
                    break
                else:
                    break
            break
        else:
            print('You can only by a minimum of 5000 chips value')
            break
    print()
    print(f'You bought a total of {total}')
    
    if s_money > 5 and s_money <= 10000:
        update_s_money(s_money)
    else:
        print('Start money exceed maximum allowed amount of 10000')
    