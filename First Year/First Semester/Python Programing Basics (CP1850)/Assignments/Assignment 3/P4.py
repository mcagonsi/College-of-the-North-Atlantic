# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:50:49 2023

@author: Chidera
"""
def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Fifa World Cup Winners')
    print()
def read_file()-> dict:
    '''
    

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    champions_list = {}
    ChamPions = []
    countries = []
    with open('world_cup_champions.txt') as champions: #reads the text file
        Champions = champions.readlines()
        for champion in Champions:
            champion = champion.split(',') #converts the string into a list with seperate elements
            ChamPions.append(champion) #appends each list to list to form a 2D list
            
            countries.append(champion[1]) # creates a list of countries
        #removes unwanted information
        ChamPions.pop(0)
        countries.pop(0)
        
        
        countries = list(set(countries)) #removes duplicates from the countries list
        
        #start looping each country through the 2D list
        for country in countries:
            #initializes the variables that would be added to the champions list dictionary
            wins = 0
            years = []
            for champ in ChamPions: #loops through each list in the 2D list
            
                if country in champ: #checks if the country country can be found in each list in the 2D list on iteration
                    wins+=1 #if present, it increments the wins value by 1
                    years.append(champ[0]) #this adds the year of win to the list of years 
                    champions_list[country] = {'wins':wins,'years':years} #sets the country as the key and add the values
        return champions_list
                    
def output():
    '''
    

    Returns
    -------
    None.

    '''
    CHAMPIONS_LIST = read_file()
    
    print('Country\t\t\t Wins\tYears')
    print('='*7,'\t\t','='*5,'\t','='*4)
    #loops through the unpacked dictionary sorted based on the country in alphabetical order
    for country,details in sorted(CHAMPIONS_LIST.items(),key = lambda x:x[0]):
        years= ", ".join(details['years']) #joins the items in the years list into one string and assigns it
        s= 17
        print(country,' '*(s-len(country)), details['wins'],'\t',years) #formats and prints the output accordingly
          
       
         
def main():
    '''
    

    Returns
    -------
    None.

    '''
    display_title()
    read_file() #reads the file
    output() #gives the output of the read file

if __name__ == '__main__':
    main()
