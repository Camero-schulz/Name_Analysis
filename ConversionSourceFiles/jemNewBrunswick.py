#!/usr/bin/env python3

#
#   Description: What does this code do?
#
#   Authors: 
#      Partner 1:
#      Partner 2:
#
#   Date of last update: 
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
    outputFileName = outputFileNameBase + ".csv"


#
#   What is being declared here and why?
#
    names    = []
    numbers  = []
    ranks    = []
    year = []
    total    = 0

    namesF    = []
    numbersF  = []
    ranksF    = []
    yearF = []
    totalF    = 0

#
#   What is the overall purpose of this section of code?
#
    with open ( inputFileName ) as csvDataFile:
        #
        # What does next do
        #
        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            #
            # What is happening here?
            #   - include information about strip() and the purpose
            #     of newranks as opposed to ranks
            #
            if row[1] == 'M' :
                tempName = row[2].strip()
                names.append(tempName)
                numbers.append(int(row[3]))
                year.append(int(row[0]))
                total = total + 1
                ranks.append(total)
            elif row[1] == 'F' :
                tempName = row[2].strip()
                namesF.append(tempName)
                numbersF.append(int(row[3]))
                yearF.append(int(row[0]))
                totalF = totalF + 1
                ranksF.append(totalF)                
        
        print ( "There are ",total," male names")
        print ( "There are ",totalF," female names")
    
    
    
    # Male
    prevNum = 0
    prevRank = 1
    counter = 1
    
    tempNum = 0
    prevYear = 0

    if total > 0 :
        people = {'Year': year,'Name':names,'Number':numbers}
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
        rankedPeople_df.to_csv("M_" + outputFileName, sep=',', index=False, encoding='utf-8')
    

    # Female 

    prevNum = 0
    prevRank = 1
    counter = 1
    
    tempNum = 0
    prevYear = 0
    
    if totalF > 0 :
            peopleF = {'Year': yearF,'Name':namesF,'Number':numbersF}
            people_dfF = pd.DataFrame(peopleF)
            print("Number of Entries:", totalF)

            people_dfF.sort_values(["Year","Number","Name"], axis = 0, ascending=[True, False, True], inplace=True) 
            
            # Ranker
            for i in range(totalF):    
                if people_dfF.iloc[i, 0] != prevYear:
                    prevRank = 1
                    counter = 1
                    ranksF[i] = prevRank
                    prevYear = people_dfF.iloc[i, 0]
                else:
                    if int(people_dfF.iloc[i, 2]) == int(prevNum):
                    
                        ranksF[i] = prevRank
                        counter = counter + 1
                    if int(people_dfF.iloc[i, 2]) != int(prevNum):
                        prevRank = prevRank + counter
                        ranksF[i] = prevRank
                        counter = 1
                    
                        prevNum = people_dfF.iloc[i, 2]
     
            # Attachment of Rank Column
            rankedPeople_dfF = people_dfF.assign(Rank=ranksF)
            
            # Display of results
            print ( rankedPeople_dfF )

            # CSV file creation
            rankedPeople_dfF.to_csv("F_"+outputFileName, sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
    main ( sys.argv[1:] )

#
#   End of names.py
#
