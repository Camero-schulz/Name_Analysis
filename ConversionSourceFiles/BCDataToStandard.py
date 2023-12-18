#!/usr/bin/env python3


#
# This code changes the BC DATA into one csv file of the format Year, sex, name, frequency, rank
#
#
#
#
#

# Libraries
import sys

import csv
import pandas as pd
 
def main ( argv ):

    
 

    fileName = ['../DataFiles/BCDATA/bc-popular-boys-names.csv', '../DataFiles/BCDATA/bc-popular-girls-names.csv']
    for sex in fileName:
        names    = []
        years = []
        numbers  = []
        yearIndex = []
        with open (sex) as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=',')
            for row in csvReader: 
                if(row[0] == "Name"):
                    yearIndex = row.copy()
                    del yearIndex[0]
                    yearIndex.remove('Total')
                else:
                    for i in range(1, len(row)-2): 
                        if(int(row[i]) != 0):
                            tempName = row[0].strip()
                            names.append(tempName)
                            numbers.append(int(row[i]))
                            years.append(yearIndex[i])
                            

           
            people = {'Year':years,'Name':names,'Number':numbers}
            people_df = pd.DataFrame(people)

            
            
                        

            people_df.sort_values(["Year",'Number',"Name"], axis = 0, ascending=[True, False,True], inplace=True)
            
            ranks = []
            currentRank = 1
            currentYear = 1923
            for index in range(0, len(people_df)):
                
                if(int(people_df.iloc[index, 0]) != currentYear):
                    currentRank = 1
                    currentYear = int(currentYear) + 1 
                
                ranks.append(currentRank)
                currentRank= currentRank + 1

            for index in range(1, len(people_df)):
                if(people_df.iloc[index,2] == people_df.iloc[index-1,2]):
                        ranks[index] = ranks[index -1]
                        
                
            
            people_df["Rank"] = ranks


            if(sex == fileName[0]):
                people_df.to_csv('../CSVFiles/M_BC.csv', sep=',', index=False, encoding='utf-8')               
            elif(sex == fileName[1]):
                people_df.to_csv('../CSVFiles/F_BC.csv', sep=',', index=False, encoding='utf-8')

            
            
                                

        

if __name__ == "__main__":
    main ( sys.argv[1:] )
