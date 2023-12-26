# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:00:34 2023

@author: Michael.Agonsi
"""

print("Hi, I am your computer and i can count from 0-9\n\n")

contr= input("Should i count? Y/N:\t")
while contr == "Y" or contr == "y":
    num=0
    while num < 10:
        print(num, end=' ')
        num+=1
    print ("\nGreat\n")
    contr= input('Should I count again? Y/N:\t')
    continue
add = input("Do you wan the sum of all the numbers? Y/N:\t")
total = 0
while add=="y" or add=="Y":
    for num in range(0,10):
        total+=num
        print(total)
else:
    print("Goodbye!")
        


