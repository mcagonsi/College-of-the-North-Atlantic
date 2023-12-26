# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:43:48 2023

@author: Michael.Agonsi
This module contains functions for calculating batting average for a user.
"""
def title():
    print('='*65)
    print('\t\t\t\t\tBaseball Team Manager')
    print('MENU OPTIONS'+
          '\n1 - Calculate batting average'+
          '\n2 - Exit program')
    print('='*65)
    
def at_bats() -> int:
    at_bats = int(input('Official number of at bats: \t'))
    return at_bats
def num_hits() -> int:
    n_hits = int(input('Number of hits:\t'))
    return n_hits
def avg (n_hits, at_bats) -> float:
    average = float(n_hits/at_bats)
    return average

def main():
    title()
    menu = True
    while (menu == True):
        option = input('Menu Option:\t')
        if (option == '1'):
            loop = 'y'
            while (loop == 'y'):
                print('Calculate batting average...')
                atBats = at_bats()
                nHits = num_hits()
                
                if (atBats <= 0 or nHits <= 0):
                    print('Input cannot be zero')
                    continue
                else:
                    aveRage = avg(nHits, atBats)
                    print(f"Batting average {aveRage:.3f}")
                loop = input('Continue? (y/n): ')
        elif (option == '2'):
            print('Bye!')
            break
            
        else:
            print('Not a valid option. Please try again')
   
if __name__ == "__main__":
    main()