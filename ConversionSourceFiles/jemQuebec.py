#!/usr/bin/env python3

#
#   Description: Extract data from the Quebec files and turns that data into a csv file
#
#
#   Date of last update: 13/3/2023
#

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

    if len(argv) < 2:
        print ( "Usage:  ./names.py -i <input file name> -o <output file0 name base>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:o:",["input=","output="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name> -o <output file name1 base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -o <output file name2 base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
    outputFileName = outputFileNameBase+".csv"

    names    = []
    numbers  = []
    ranks    = []
    years    = [0]
    theYear  = []
    
    total    = 0
    prevNum = 0
    prevRank = 1
    counter = 1
    
    tempNum = 0
    prevYear = 0

  
    with open ( inputFileName ) as csvDataFile:
        next ( csvDataFile )
        csvReader = csv.reader(csvDataFile, delimiter=',')
        # Array of all the years
        for i in range(43):
            years.append(1980 + i)

        # Data extraction
        for row in csvReader:
            tempName = row[0].strip()
            for j in range(1, 43):
                if int(row[j]) != 0:
                    if tempName != "Somme:":
                        names.append(tempName)
                        theYear.append(int(years[j]))
                        numbers.append(int(row[j]))
                        ranks.append(total)        
                        total = total + 1
        # Sorter 
        if total > 0 :
            people = {'Year': theYear,'Name':names,'Number':numbers}
            people_df = pd.DataFrame(people)
            print("Number of Entries:", total)

            people_df.sort_values(["Year","Number","Name"], axis = 0, ascending=[True, False, True], inplace=True) 
            
            # Ranker
            for i in range(total):    
                if people_df.iloc[i, 0] != prevYear:
                    prevRank = 1
                    counter = 1
                    ranks[i] = prevRank
                    prevYear = people_df.iloc[i, 0]
                else:
                    if int(people_df.iloc[i, 2]) == int(prevNum):
                    
                        ranks[i] = prevRank
                        counter = counter + 1
                    if int(people_df.iloc[i, 2]) != int(prevNum):
                        prevRank = prevRank + counter
                        ranks[i] = prevRank
                        counter = 1
                    
                        prevNum = people_df.iloc[i, 2]
     
            # Attachment of Rank Column
            rankedPeople_df = people_df.assign(Rank=ranks)
            
            # Display of results
            print ( rankedPeople_df )

            # CSV file creation
            rankedPeople_df.to_csv(outputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
# 
