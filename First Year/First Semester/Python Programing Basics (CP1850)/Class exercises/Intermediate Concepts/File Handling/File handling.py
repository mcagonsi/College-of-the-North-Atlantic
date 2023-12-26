# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:00:44 2023

@author: Michael.Agonsi
"""

file = open('Dera doc.zip', 'w')
file.write('Today is a good day')
file.close()


with open('BlackJack game.txt', 'w') as new_file:
    new_file.write('Today is mr aruns birthday and wedding anniversary')

with open('BlackJack game.txt', 'r') as new_doc:
    print(new_doc.readline())
with open('BlackJack game.txt', 'a') as hello:
    print(hello.write('\nhow are you doingsss?'))
   
