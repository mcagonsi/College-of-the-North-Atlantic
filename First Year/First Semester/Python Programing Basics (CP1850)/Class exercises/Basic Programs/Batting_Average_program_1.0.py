# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:43:10 2023

@author: Michael.Agonsi
"""

#A program that calculates players batting average

print('='*65)
print('\t\t\t\t\tBaseball Team Manager')
print('\n\nThis program calculates the batting average for a player based' +
      '\non the player\'s official number of at bats and hits')
print('='*65)
print('')
print('')

p_name = input('Player\'s name:\t')
at_bats = int(input('Official number of at bats: \t'))
n_hits = int(input('Number of hits:\t'))

average = float(n_hits/at_bats)

#correct way to display floats, the round function will get rid of the zeros behind the decimal places specified
print(f"{p_name}\'s batting average is {average:.3f}")