# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:49:59 2023

@author: K205User
"""
def read(FILENAME:str)->str:
    '''
    

    Parameters
    ----------
    FILENAME : str
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.

    '''
    #this reads the file and returns it as a block of string object
    with open(FILENAME) as file:
        reader = file.read()
        return reader
   

def count_words(FILENAME:str)->dict:
    '''
    

    Parameters
    ----------
    FILENAME : str
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    try: #handles exception error
    
        read_file = read(FILENAME)
        words_list = read_file.replace('.',' ').replace(',',' ').replace(':',' ').split() #refines the string and converts to a list of items 
        
        words_dictionary = {} #this creates the dictionary
        
        #this loops through each item in the list and adds it to the dicitonary as well as the frequency value
        for word in words_list:
            words_dictionary[word]= words_list.count(word)
        
        return words_dictionary #returns the dictionary
    except FileNotFoundError:
        print()
        print('File does not exist!')
    except Exception:
        print()
        print('An unexpected error occured!')

def main():
    '''
    

    Returns
    -------
    None.

    '''
    FILENAME = input('Enter name of text file:  ')
    dictionaryOfWords = count_words(FILENAME)
    print(dictionaryOfWords)
    
if __name__ =='__main__':
    main()