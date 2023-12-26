# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:13:57 2023

@author: Michael.Agonsi
"""
import csv


with open("movies.csv", newline='') as file:
    reader= csv.reader(file)
    for row in reader:
        print(f'{row[0]} {row[1]}')



    
