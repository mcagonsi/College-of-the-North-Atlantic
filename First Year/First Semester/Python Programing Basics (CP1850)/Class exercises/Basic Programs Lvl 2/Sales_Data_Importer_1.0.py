# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:16:28 2023

@author: Michael.Agonsi
"""



def title():
    print('SALES DATA IMPORTER')
    print('')
    print('Enter Sales Data')
    print('')
def get_amount() -> float:
    '''
    Gets a sales amount from the user, converts it to a float
    value and returns the float value.

    Parameters
    ----------
    float : TYPE
        DESCRIPTION.

    Returns
    -------
    amount : TYPE
        DESCRIPTION.

    '''
    while True:
        amount = float(input('Amount:\t\t\t'))
        if amount > 0:
            return amount
            break
            
        else:
            print('Amount must be greater than 0')

def get_month() -> int:
    '''
    Gets a month from the user, converts it to an int value, and
    returns the int value.

    Parameters
    ----------
    int : TYPE
        DESCRIPTION.

    Returns
    -------
    mm : TYPE
        DESCRIPTION.

    '''
    while True:
        mm = int(input('Month (1-12):\t'))
        if mm >= 1 and mm <=12:
            return mm
            break
            
        else :
            print('Month must be between 1 and 12')
            continue
def get_day(month) -> int:
    '''
    Gets a day from the user, converts it to an int value, and
    returns the int value.

    Parameters
    ----------
    int : TYPE
        DESCRIPTION.

    Returns
    -------
    dd : TYPE
        DESCRIPTION.

    '''
    
    while True:
        dd = int(input('Day (1-31):\t\t'))
        
        if month == 2 and dd > 29:
            print('Day must be between 1 and 28')
            continue
        elif month == 4 and dd > 30:
            print('Day must be between 1 and 30')
            continue
        elif month == 6 and dd > 30:
            print('Day must be between 1 and 30')
            continue
        elif month == 9 and dd > 30:
            print('Day must be between 1 and 30')
            continue
        elif month == 11 and dd >30:
            print('Day must be between 1 and 30')
            continue
        elif dd <= 0 or dd > 31 :
            print('Please enter a valid day!')
            continue
        else:
            return dd
        

         
        
def get_year() -> int :
    '''
    Gets a year from the user, converts it to an int value, and
    returns the int value.

    Parameters
    ----------
    int : TYPE
        DESCRIPTION.

    Returns
    -------
    yy : TYPE
        DESCRIPTION.

    '''
    while True:
            yy = int(input('Year:\t\t\t'))
            if yy >=2000 and yy <=9999:
                return yy
                break
           
            else:
                print('Sales Year must be between 2000 and 9999')
                continue
    
def main():
    title()
    total = 0
    counter = 0
    again = 'y'
    while again == 'y':
        initial_money = get_amount()
        year = get_year()
        month = get_month()
        day = get_day(month)
        total += initial_money
        counter +=1
        if month >= 1 and month <=3:
            print(f"{counter}.\t\t\t\t{year}-{month}-{day}\tQuarter 1\t ${initial_money:.1f}\n")
        elif month >= 4 and month <= 6:
            print(f"{counter}.\t\t\t\t{year}-{month}-{day}\tQuarter 2\t ${initial_money:.1f}\n")
        elif month >= 7 and month <=9:
            print(f"{counter}.\t\t\t\t{year}-{month}-{day}\tQuarter 3\t ${initial_money:.1f}\n")
        elif month >= 10 and month <= 12:
            print(f"{counter}.\t\t\t\t{year}-{month}-{day}\tQuarter 4\t ${initial_money:.1f}\n")
        print('')
        again = input('Enter more sales ? (y/n): ')
        print()
        again = again.lower()
        
          
    print('Total Sales\n'+
           '-'*10,'\n', total, '\nBye!')
if __name__ == '__main__':
    main()

