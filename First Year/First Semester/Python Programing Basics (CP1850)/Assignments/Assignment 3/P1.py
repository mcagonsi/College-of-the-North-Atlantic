# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:32:58 2023

@author: Chidera
"""

def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Tip Calculator')
    print()
    
def inputs()-> (float ,int):
    '''
    

    Returns
    -------
    (float ,int)
        DESCRIPTION.

    '''
    print('INPUT')
    while True: #loop for handling error for cost inputs
        try:
            cost = float(input('Cost of meal:  '))
            if cost > 0: #checks if cost input is greater than 0
                break
            else:
                print('Must be greater than 0. Please try again.')
                continue
        except ValueError: #handles the value error
            print('Must be a valid decimal number. Please try again.')
            continue
    while True: #loop for handling the error for tip inputs
        try:
            tip = int(input('Tip percent:  '))
            if tip >0: #checks if input is greater 0
                break
            else:
                print('Tip must be greater than 0. Please try again.')
                continue
        except ValueError:
            print('Must be a valid integer. Please try again.')
            continue
    print()
    return cost,tip
    
def calculation ()-> (float,int,float,float):
    '''
    

    Returns
    -------
    (float,int,float,float)
        DESCRIPTION.

    '''
    #calclulation for the tip ammount and total ammount
    cost,tip = inputs()
    if tip == 0:
        tip_ammount = tip
        total_ammount = tip_ammount + cost
    else:
        tip_ammount = cost * (tip/100)
        total_ammount = cost + tip_ammount
    return cost, tip, tip_ammount, total_ammount

def outputs():
    '''
    

    Returns
    -------
    None.

    '''
    cost, tip, tip_ammount, total_ammount = calculation()
    print('OUTPUT')
    print(f'Cost of meal: {cost:.2f}')
    print('Tip percent: {}%'.format(tip))
    print(f'Tip amount: {tip_ammount:.2f}')
    print(f'Total amount: {total_ammount:.2f}')
    
    #exits the program
    print()
    print('Thank You!')
    print()
    print('Bye!')
    
def main():
    #introduces the program by diesplaying the title
    display_title()
    #called only the outputs() funtion because it already call the other functions within it
    outputs()

if __name__ == '__main__':
    main()
    
