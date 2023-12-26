# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:42:33 2023

@author: Michael.Agonsi
"""

import random as rand
# help(rand)

#random fumnction
#gives you a float between 0 and 1
number1 = rand.random()
print(number1)


#the randint() function
#gives you and integer in the rand you specify
#syntax: randint(min, max)
number2 = rand.randint(1, 100)
print(number2)

#thte randrange() function
#gives int in the range that you specify
#syntax: randrange(start, stop, step)
number3 = rand.randrange(1,100)

number4 = rand.randrange(100, 200, 2)



