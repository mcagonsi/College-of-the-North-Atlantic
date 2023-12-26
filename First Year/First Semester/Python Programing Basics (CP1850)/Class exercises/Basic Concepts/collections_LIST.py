# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:30:07 2023

@author: Michael.Agonsi
"""

'''
LIST SYNTHAX

list_name = [item1, item2, item3, etc]
'''

movie = ['The Dark Knight',2007, 7.8]
type(movie)

str_objects = ['michael', 'dera', 'agonsi']
flt_objects = [3.6,67.9,56.0]

'''
TO ACCESS THE ITEM OR OBJECTS WITHIN THE LIST
Positive indexing syntax:
    listName[0-number]
Negative indexing syntax:
    listName[-1 - -ve_number]
        or
    list_name[index_number]

'''

movie[2]
type(movie[0])

'''
UPDATING THE OBJECTS WITHIN THE LIST
    syntax:
        list_name[index] = new_value



'''

movie[0] = 'Super Man Vs Batman'

'''
    METHODS WITH LIST
    syntax:
        list_name.append(element) - adds element to the last position on the list
        list_name.insert(index, element) - inserts element in the specified position
        list_name.remove(element) - removes specified element
        list_name.pop(index) - returns and removes element on specified index
        list_name.index(element) - returns index of specified element in list
'''

'''
    NOTE: To pop an element using the index number we can retrieve the index number,
    assign it to a variable and remove.
    syntax:
        x = listname.index(element)
        listname.pop(x)
'''


'''
    PROPERTIES OF A LIST
    
LENGTH: checks the number of items in a list
syntax:
    len(listName)

CAN BE LOOPED OR CODED IN CONDITIONAL STATEMENTS using the IN keyword

Syntax:
    for item in listName:
        -- statements e.g print(item)
    
    if {element} in listName:
        -- statements e.g movies.append(name)
    while i < len(listName):
        -- statements
        
OTHER FUNCTIONS WITH LIST: enumerate and zip

ENUMERATE:
    this is a simple way to list or print or unpack a list. [with the index number]
    syntax:
        for item in enumerate(listName):
            -- statements
ZIP:
    this is to join contents of two lists together to one list and print them
    syntax:
        for item1, item2 in zip(list1, list2):
            -- statements
            
OTHER LIST METHODS

count( ) :
    takes a specific element and gives the number of times the element appears in the list
    syntax:
        listName.count(item_to_check)
        
reverse() :
    this reverses the contents of the list. when you try to access the list again it will be the 
    reverse presented.
    syntax:
        listName,reverse()
sort():
    this sorts the items in a list into ascending order by default.
    syntax:
        listName.sort()
    you can use key arguments as well.
    syntax:
        listName,sort(key = str.lower)
sorted():
    it makes a copy of the lists ,sorts it and returns the value of the sorted copy list while the
    original list remains intact.
    syntax:
        listName.sorted([key=])

OTHER FUNCTIONS YOU CAN USE WITH A NUMERICAL LIST
    max(listName) -> gives the maximum number in a list
    min(listName) -> gives the minimum number in a list
    sum(listName) -> gives the sum of the numbers in a list.
        sum(listName, start = [n] ) -> takes the sum of the list and adds it to n
    
    
    
    
    
    
    
    
    '''

















        
