# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:52:23 2023

@author: Michael.Agonsi
"""
import random as r 

def intro():
    '''
    Introduces the program

    Returns
    -------
    None.

    '''
    print("Guess the Number!"+
          "\n\nI'm thinking of a number from 1 to 10")
def yourGuess() ->int:
    '''
    Gets input of your integer and returns it

    Returns
    -------
    int
        DESCRIPTION.

    '''
    yourNumber = int(input('\nYour guess:\t'))
    return yourNumber

def guessing() -> int:
    '''
    Generates random int and returns it

    Returns
    -------
    int
        DESCRIPTION.

    '''
    guessed = r.randint(1,11)
    return guessed

def main():
    '''
    Plays the guessing game

    Returns
    -------
    None.

    '''
    intro()
    looped = 'y'
    randNumber = guessing()
    index = 0
    while looped.lower() == 'y':
        index += 1
        yourInput = yourGuess()
        if yourInput > randNumber:
            print('Too High')
            continue
        elif yourInput < randNumber:
            print('Too Low')
            continue
        else:
            print(f"You guessed it in {index} tries.")
          
        looped = input('Would you like to play again? (y/n): ')
        index = 0
    print('\nBye!')
    
if __name__ == '__main__':
    main()