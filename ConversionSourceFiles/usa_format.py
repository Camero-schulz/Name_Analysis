#!/usr/bin/env python3

import pandas as pd

#created by Joe Mather, 1231960

#1 year, all names: 0:3.30
#2 year, all names: 0:7.25
#5 year, all names: 0:33.00
#10 year, all names: 1:44.26

#formats usa name info into standard format

def USA_format():

    while(True):
        first = input("Enter the starting year (1880-2021): ")
        try:
            first = int(first)
            if (1880 <= first <= 2021):
                break
            else:
                print("ERROR: Number must be in range")
        except ValueError:
            print("ERROR: Input must be an integer")
        
    while(True):
        last = input("Enter the last year (1880-2021): ")
        try:
            last = int(last)
            if ((last >= first) and (1880 <= last <= 2021)):
                break
            else:
                print("ERROR: Number must be in range and less than the starting year")
        except ValueError:
            print("ERROR: Input must be an integer")
        
    while(True):
        num_names = input("Enter the number of names per year (-1 for all names): ")
        try:
            num_names = int(num_names)
            if (-1 <= num_names):
                break
            else:
                print("ERROR: Number must be greater than or equal to -1")
        except ValueError:
            print("ERROR: Input must be an integer")

    print("Running... ")

    year = []
    name = []
    occurence = []
    rank = []

    names = {"year":year,"name":name,"occurence":occurence,"rank":rank}

    female_df = pd.DataFrame(names)
    male_df = pd.DataFrame(names)
    

    m_total = 1
    f_total = 1
    
    for i in range(first,last+1): #each year
        m_year=1
        f_year=1
        f_temp_rank = 1
        f_temp_occurence = -1
        m_temp_rank = 1
        m_temp_occurence = -1

        file_name = "../DataFiles/USADATA/yob"+str(i)+".txt"
        current_year = open(file_name, "r")
        year_lines = current_year.readlines()

        for line in year_lines:
            if(num_names == -1 or m_year<=(num_names) or f_year<=(num_names)):
                #format into list for dataframe
                line = line.strip()
                current_line = line.split(',')
                current_line.insert(0,str(i)) #adds year
                current_line[1] = current_line[1].upper()

                #adding names to respective dataframes
                if(current_line[2]=='M' and (num_names == -1 or m_year<=(num_names))):
                    current_line.append(m_year) #m_year is the rank
                    current_line.pop(2) #removes gender mark

                    if (current_line[2] == m_temp_occurence): #does same rank if tied
                        current_line[3] = m_temp_rank
                    male_df.loc[m_total] = current_line
                    m_total+=1
                    m_year+=1
                    m_temp_occurence = current_line[2]
                    m_temp_rank = current_line[3]

                elif(current_line[2]=='F' and (num_names == -1 or f_year<=(num_names))):
                    current_line.append(f_year)
                    current_line.pop(2)

                    if (current_line[2] == f_temp_occurence):
                        current_line[3] = f_temp_rank
                    female_df.loc[f_total] = current_line
                    f_total+=1
                    f_year+=1
                    f_temp_rank = current_line[2]
                    f_temp_occurence = current_line[3]

        current_year.close()
    
    male_df.to_csv("../CSVFiles/M_USA.csv", sep=',', index=False, encoding='utf-8')
    female_df.to_csv("../CSVFiles/F_USA.csv", sep=',', index=False, encoding='utf-8')
    print("Done!")
    

USA_format()