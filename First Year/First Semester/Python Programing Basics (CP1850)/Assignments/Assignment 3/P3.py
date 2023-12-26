# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:06:32 2023

@author: Chidera
"""

def birds_list()-> dict:
    '''
    

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    birds = {} #dictionary that contains the list of birds
    return birds

def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Bird Counter program')
    print()
    print("Enter 'x' to exit")
    print()

def inputs(BIRDS:dict):
    '''
    

    Parameters
    ----------
    BIRDS : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    while True:
        name = input('Enter name of bird: ')
        if name == 'x' and len(BIRDS) == 0 : #checks the input to end the program
            print()                          # also checks if the list is emptiy
            print('No bird has was spotted.') #returns the message if empty
            break
        else:
            if name == 'x': #if list is not empty it prints the output and ends the program
                print()
                display_bird_list(BIRDS)
                print()
                break
            else:
                if name in BIRDS: #checks if name is on the list
                    BIRDS[name] +=1 #increments whatever value is there by 1
                else:
                    BIRDS[name]= 1 #if name is not on the list, it adds the name and assigns value of 1
def display_bird_list(BIRDS:dict):
    '''
    

    Parameters
    ----------
    BIRDS : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    print('Name\t\t\t\t\t\t\t\tCount')
    print('='*35,'='*5)
    for name,count in sorted(BIRDS.items(),key= lambda x:x[0]): #loops through a list of items sorted alphabetically on the name.
        s=35-len(name) #this formats the output to the console by reducing the spaces based on the lenght of the name.
        print(name.title(),' '*s,count)
    print()

def main():
    '''
    

    Returns
    -------
    None.

    '''
    display_title()
    BIRDS = birds_list()       
    inputs(BIRDS)

if __name__=='__main__':
    main()
    



