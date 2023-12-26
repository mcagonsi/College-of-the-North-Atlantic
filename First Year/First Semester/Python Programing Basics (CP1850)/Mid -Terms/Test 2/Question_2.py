# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 08:47:53 2023

@author: Michael.Agonsi
"""

def readFile():
    '''
    

    Returns
    -------
    None.

    '''
    file_name = input('Enter the name of the file:  ') #takes input for file name
    try:
        with open(file_name) as rules: #reads the file
            print()
            print('Rules ---')
            print()
            #prints the  contents of the file or displays contents
            for i, rule in enumerate(rules,start =1):
                print('{}. {}'.format(i,rule))
    #handles the case where the file does not exist         
    except FileNotFoundError:
        print('File Not Found! Please try again!')
    except Exception:
        print('An Unexpected Error Occured!')
        
def main():
    '''
    

    Returns
    -------
    None.

    '''
    #calls the function to read the file
    readFile()
    
if __name__ == '__main__':
    main()


        