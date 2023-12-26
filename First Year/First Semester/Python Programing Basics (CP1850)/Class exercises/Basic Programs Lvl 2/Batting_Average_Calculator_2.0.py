# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:01:41 2023

@author: Michael.Agonsi
"""

def separator ():
    '''
    Creates separator

    Returns
    -------
    None.

    '''
    print('='*65)
def title ():
    '''
    prints title

    Returns
    -------
    None.

    '''
    print('\t\t\t\t\tBaseball Team Manager')
def menu ():
    '''
    prints menu options

    Returns
    -------
    None.

    '''
    print('MENU OPTIONS'+
          '\n1. - Calculate batting average'+
          '\n2. - Exit program')
def option():
    '''
    collects input and returns

    Returns
    -------
    option : TYPE
        DESCRIPTION.

    '''
    option = int(input('Menu option: '))
    return option
def calculation ():
    '''
    calculates the batting average

    Returns
    -------
    None.

    '''
    print('Calculate batting average...')
    at_bats = int(input('Official number of at bats: \t'))
    n_hits = int(input('Number of hits:\t'))

    average = float(n_hits/at_bats)

    print(f"Batting average is {average:.3f}")
    
    
if __name__ == '__main__':
    separator()
    title()
    menu()
    separator()
    while True:
        choice = option()
        if choice == 1:
            calculation()
        elif choice == 2:
            break
        elif choice == 3:
            print('Not a valid option. Please try again')
            continue
    print('\nBye!')
            