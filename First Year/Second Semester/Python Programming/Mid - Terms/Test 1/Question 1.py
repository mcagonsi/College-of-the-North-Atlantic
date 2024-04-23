# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:38:15 2024

@author: Michael.Agonsi
"""

from dataclasses import dataclass

@dataclass
class Rectangle: #this is the class object
    width: int
    length: int
    __is_square: bool = False

    def check_is_square(self): #checks if it is a square or not
        '''
        

        Returns
        -------
        None.

        '''
        if self.width == self.length:
            self.__is_square = True
        else:
            self.__is_square = False

    @property
    def area(self): # area property for the object
        '''
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if self.width < 0:
            return (self.width * -1) * self.length
        elif self.length < 0:
            return self.width * (self.length * -1)
        else:
            return self.width * self.length

    @property
    def perimeter(self): #perimeter property for the object
        '''
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if self.width < 0:
            return (2 * self.width * 0) + (2 * self.length)
        elif self.length < 0:
            return (2 * self.width) + (2 * self.length * 0)
        else:
            return (2 * self.width) + (2 * self.length)

    @property
    def is_square(self):
        '''
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        self.check_is_square() #calls the check if square fuction
        return self.__is_square


def title():
    print('The Rectangle Program')
    print()


def width()->int:
    '''
    

    Returns
    -------
    int
        DESCRIPTION.

    '''
    while True: #handles any errors
        try:
            Width = int(input('Enter width: '))
            return Width
            break
        except ValueError:
            print('Please enter an integer')
            continue


def length()->int: #handles any errors
    '''
    

    Returns
    -------
    int
        DESCRIPTION.

    '''
    while True:
        try:
            Length = int(input('Enter length: '))
            return Length
            break
        except ValueError:
            print('Please enter an integer')
            continue


def main(): #starts the program
    cont = 'y'
    while cont.lower() == 'y':
        title()
        w = width()
        l = length()
        print()
        rectangle = Rectangle(w, l)
        print('OUTPUT')

        print(f"{'AREA':15}: {rectangle.area:}")
        print(f"{'PERIMETER':15}: {rectangle.perimeter}")
        print(f"{'IS SQUARE':15} : {rectangle.is_square}")

        cont = input('Do you want to try again? (y/n): ').lower()
        print()
    print('Bye')


if __name__ == '__main__':
    main()

