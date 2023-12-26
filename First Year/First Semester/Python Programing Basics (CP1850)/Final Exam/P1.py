# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:04:04 2023

@author: K205User
"""
   
def display_menu():
    '''
    

    Returns
    -------
    None.

    '''
    print('------Class Students Management------')
    print('1. Add Student'+
          '\n2. Display Students'+
          '\n3. Get Top Student'+
          '\n4. Quit')

def add(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    name = input("Enter student name: ").title()

    #takes inputs and handles errors
    while True:
        try:
            roll_number = int(input('Enter student roll number: '))
            break
        except ValueError:
            print('Please input an integer!')
    while True:
        try:
            marks = list(map(int,input('Enter student marks, separated by space: ').split()))
            break
        except Exception:
            print('Enter only numbers!')
    student =[name,roll_number,marks]
    STUDENTS.append(student) #adds student data to the STUDENT list
    print('Student added successfully!')
    print()


def display_students(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    if len(STUDENTS)== 0: #executes if the list is empt
        print('Class list is empty!')
    else:
        print('List of Students:\n')
        for student in STUDENTS:
            print('Name: {}, Roll Number: {}'.format(student[0],student[1]))
        print()


def get_top(STUDENTS:list):
    '''
    

    Parameters
    ----------
    STUDENTS : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    average_marks = [] #creates the list of average mark for each student
    for student in STUDENTS:
        #calculates the average for each student and appends it to the list
        avg = sum(student[2])/len(student[2])
        average_marks.append(avg)
    top_avg = max(average_marks) #gets the highest average mark
    top_student = average_marks.index(top_avg) #gets the index number for the highest average mark on the list relative to student index on STUDENTS list
    topStudent = STUDENTS[top_student] #gets the top students information 
    
    print('Name: {}, Roll Number: {}, Average Marks = {}'.format(topStudent[0],topStudent[1], round(top_avg,1)))
    print()
    
def main():
    '''
    

    Returns
    -------
    None.

    '''
    
    STUDENTS = []
    while True:
        display_menu()
        print()
        choice = int(input('Enter your choice (1-4): '))
        print()
        if choice == 1:
            add(STUDENTS)
        elif choice == 2:
            display_students(STUDENTS)
        elif choice == 3:
            get_top(STUDENTS)
        elif choice == 4:
            print('\nBye!')
            break
        else: 
            print('Invalid choice! Please try again!')
            
if __name__ == '__main__':
    main()
        