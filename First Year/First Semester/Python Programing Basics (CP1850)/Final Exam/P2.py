# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:00:39 2023

@author: K205User
"""
import csv

FILENAME = 'students.csv'


def read_csv(FILENAME:str)->list:
    '''
    

    Parameters
    ----------
    FILENAME : str
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    '''
    records_list = [] #creates an empty list of records
    
    try:
        
        with open(FILENAME) as file:
            readfile = csv.reader(file)
            students = list(readfile) #reads the file into a list
            students.pop(0) #removes the first row to leave only student details
            for student in students:
                #creates the dictionary object for each record(student)
                records ={'name': student[0],
                         'roll': student[1]}
                #removes the ones already added to the dictionary
                student.pop(0)
                student.pop(0)
                #cleans the left over list of any empty item
                if '' in student:
                    student.remove('')
                #adds the left over list as the marks into the dictionary
                records['marks']=student
                #adds the records dictionary to the records list
                records_list.append(records)
        return records_list #returns the list of records
    except FileNotFoundError: 
        print('students.csv file not found please create file')

def write_csv(OUTPUTFILENAME:str,student_records:list):
    '''
    

    Parameters
    ----------
    OUTPUTFILENAME : str
        DESCRIPTION.
    student_records : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    student_list = [['Name','Roll Number','Marks']] #creates the first row of the list of lists before writing in to the file
    for student in student_records:
        record = [student['name'], student['roll']] #adds the first two items from the dictionary to the record list
        for i in student['marks']: #loops throught the 'marks' which is a list and adds to the record list
            record.append(i)
        student_list.append(record) #adds each student record to the 2D list for writing into csv file
    
    #writes the  list into the csv file with the same structure from reading the previous file.
    with open(OUTPUTFILENAME,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(student_list)
    print('File has been created') #notifies that the file has been created

def main():
    '''
    

    Returns
    -------
    None.

    '''

    student_records = read_csv(FILENAME)
    print(student_records)
    print()
    OUTPUTFILENAME =input('Enter output file name: ')
    write_csv(OUTPUTFILENAME, student_records)

if __name__ == '__main__':
    main()
    
    "footnote: i was not quite sure exactly what you want. if you wanted an input file name for the writing or something to run on the console"