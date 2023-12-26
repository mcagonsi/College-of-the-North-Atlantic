# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:28:59 2023

@author: Chidera
"""

def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Prime Number Checker')
    print()

def logic(num:int,result:list):
    '''
    

    Parameters
    ----------
    num : int
        DESCRIPTION.
    result : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    for i in range (1,5000):
        check = num%i 
        if check == 0:
            result.append(i)

def check_prime(num:int,result:list):
    '''
    

    Parameters
    ----------
    num : int
        DESCRIPTION.
    result : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    length = len(result)
    if length == 1:
        print('1 is a prime number')
    else:
        first_num = result[0]
        prime_num = result[1]
       
        
        if first_num == 1 and prime_num == num:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
            factors = len(result)
            print(f"It has {factors} factors:" , *result) 
        
def main():
    '''
    

    Returns
    -------
    None.

    '''
    # displays title
    display_title()
    
    # starts the loop
    loop = "y".lower()
    while loop == "y":
        # loop that checks for error
        while True:
            # list that stores the factors
            result = []
            
            # takes user input
            num = int(input('Please enter a number between 1 and 5000: '))
            if num > 0 and num <= 5000:
                # Checks for prime number and returns result or output
                logic(num, result)
                check_prime(num,result)
                break
            else:
                print()
                print('Error! Invalid Entry!')
                print()
            continue
        print()
        loop = input('Try again ? (y/n): ')
        print()
        
    # exits the loop and program
    print()
    print('Bye!')
if __name__ == '__main__':    
    main()
    
    