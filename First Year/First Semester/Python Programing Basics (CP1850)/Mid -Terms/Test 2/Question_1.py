# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:07:28 2023

@author: Michael.Agonsi
"""
def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('------ Class Students Management ------')

def display_menu():
    '''
    

    Returns
    -------
    None.

    '''
    print('1. Add Student'+
          '\n2. Remove Student'+
          '\n3. Display Students'+
          '\n4. Calculate Average'+
          '\n5. Quit')
def add_student(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # takes inputs and adds them to the list 
    name = input('Enter student name:  ')
    age = int(input('Enter student age:  '))
    student = [name,age]
    STUDENTS.append(student)
    print('Student added Successfully')
    
  
def remove_student(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    name = input('Enter student name to be removed:  ')
    names=[] #list of names created
    for student in STUDENTS:
            names.append(student[0]) #appends name of each student to the list of names
          
    if name in names:       #checks if student name is on the list and removes it
        i=names.index(name) #Student name index corresponds to the index number of student on list to remove it from list
        STUDENTS.pop(i)
        print('Student Removed Successfully!')
    else: #returns the error if student name is not on the list
        print('Student not in list')
         
            

def display_student(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    if len(STUDENTS) == 0:
        print('No Student on the list')
    else:
        for student in STUDENTS:
            print('Name: {}, Age: {}'.format(student[0],student[1]))
def calculate_avg(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    #calculates the average age of all students on the list
    ages =[]
    if len(ages)==0:
        print("No student on the list! Cannot calculate average")
    else:
        for student in STUDENTS:
            ages.append(student[1])
        avg = sum(ages)/len(ages)
        print('Average age of students: {}'.format(round(avg,1)))
def main():
    '''
    

    Returns
    -------
    None.

    '''
    # list of lists for students
    STUDENTS =[]
    while True:
        display_title()
        display_menu() 
        menu_option = int(input('Enter your choice (1-5) :  '))
        if menu_option ==1: 
            add_student(STUDENTS)
        elif menu_option == 2:  
            remove_student(STUDENTS) 
        elif menu_option ==3:
            display_student(STUDENTS)
        elif menu_option == 4:
            calculate_avg(STUDENTS)
        elif menu_option == 5: #Exits the program
            print('Program terminated')
            break
        else:
            print("Error! Please enter a valid choice")
            
if __name__ == '__main__':
    main()