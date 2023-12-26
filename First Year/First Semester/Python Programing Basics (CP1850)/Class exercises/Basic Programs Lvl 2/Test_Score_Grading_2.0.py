# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:07:01 2023

@author: Michael.Agonsi
"""


#The console for the Test Scores Program

print('The Test Scores Program')
print('')
print('Enter 3 test scores')
print('='*22)

#Requesting inputs and assigning variables
counter = 0
t1 = float(input('Enter test score:\t'))
t2 = float(input('Enter test score:\t'))
t3 = float(input('Enter test score:\t'))
counter+=3

#formula for the calculation
t_total = t1+t2+t3
avg_score= t_total/counter

#giving output or result
print(22*'=')
print('Total Score:\t',int(t_total))
print('Average Score:\t', int(avg_score))
print('')



a = avg_score >= 90
b = avg_score<=89
B = avg_score>=80
c = avg_score<=79
C = avg_score>=60
d = avg_score <=59
D = avg_score >=40
e = avg_score<40
#for assigning grades to student
if (a):
    print('Your Grade:  \t\tA')
elif (b and B):
    print('Your Grade:  \t\tB')
elif (c and C):
    print('Your Grade:  \t\tC')
elif (d and D):
    print('Your Grade:\t\tD')
else :
    print('Your Grade:  \t\tF')

#closing the program
print('')
print("Bye")
