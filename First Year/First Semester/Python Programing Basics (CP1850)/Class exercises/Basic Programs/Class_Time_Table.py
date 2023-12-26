# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:55:35 2023

@author: Michael.Agonsi
"""

#Code that reminds you of your class schedule

#data to be recalled
mon='CP1850, CR1130, CP1420, CP1555'
tue= 'CP1555, MA1900, CP1461, CP1420'
wed='CP1850, CM1400, MA1900'
thur='CP1850, CP1461, MA1900'
fri = 'CP1850, CM1400'

#prompting for input
print('I will remind you of your classes for the week.'+
      '\nEnter only number for command'+
      '\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday')
command= (input('Remind me of: '))

#giving the result of the command inputed
if command == '1': 
    print(mon)
elif command == '2': 
    print(tue)
elif command == '3': 
    print(wed)
elif command == '4': 
    print(thur)
elif command == '5': 
    print(fri)
else:
    print('You must enter a command')