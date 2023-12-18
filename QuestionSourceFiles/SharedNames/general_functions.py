#!/usr/bin/env python3


import csv
import pandas as pd
import sys
import tty
import termios

#THis function takes a set of possible inputs and returns the key that was pressed when one of those proper inputs is pressed


#NEED TO TEST IF LOTS OF RUNNING WILL BREAK
def user_input_process( possibleInputs): 

    
    key = sys.stdin.read(1)

    if(key not in possibleInputs):
        return user_input_process(possibleInputs)
    else:
        return key


#setup for the recursive function above
def user_input(possibleInputs):
    fd = sys.stdin.fileno()

    # save the terminal attributes
    old_settings = termios.tcgetattr(fd)

    try:
       
        tty.setraw(fd)

        key = user_input_process(possibleInputs)
    finally:
        # restore the terminal attributes
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    print(key)
    return key
    
           

#This function takes the chosen data sets and the gender wanted and returns a data frame of all names, year and region in that set
def all_chosen_data_sets(chosenDataSets, gender):
    
    #Gender must by, M or F
    if(gender != 'F' and gender != 'M'):
        return ValueError
    
    path = __file__

    #path = os.getcwd()
    new_path = path[0 : len(path) - len('/QuestionSourceFiles/SharedNames/general_functions.py')]
    
    new_path = new_path + '/CSVFiles/'
    # path = 'CSVFiles/'
    beginning = new_path + gender + '_'
    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    ending = '.csv'
    chosenSetOfFiles= []
    for index in chosenDataSets:
        chosenSetOfFiles.append(setOfFiles[int(index) - 1])
        


    names = []
    years = []
    regionIdentifier = []
    totalSetsUsed = 0
    
    for set in chosenSetOfFiles:
        # try:
            totalSetsUsed = totalSetsUsed + 1
            with open(beginning + set + ending) as csvDataFile:
                csvReader = csv.reader(csvDataFile, delimiter=',')
                iterationsRan = 0
                for row in csvReader:
                    iterationsRan += 1
                    if(iterationsRan > 1):
                        if(int(row[0]) >= 1980 and int(row[0]) <= 2018):
                            names.append(row[1])
                            years.append(row[0])
                            regionIdentifier.append(set)
        # except:
        #     totalSetsUsed = totalSetsUsed - 1
        #     print("The " + gender + ' ' + set +" file was not found in the database")
            
            


    


    
    if totalSetsUsed > 0:
        people = {'Names':names, 'Years':years, 'Regions':regionIdentifier }
        people_df = pd.DataFrame(people)
            # else:
        # print("At least 2 Sets were not found")
        # return FileNotFoundError

    return people_df


def printNamesInDF(toPrint):


    toPrintNames = toPrint.Names.tolist()
    for i in toPrintNames:
            print(i) 


# Takes a data frame and returns all unique names in each region
#Also trims down the set to years >= 1980
def unique_names_per_region(chosenDataSets, totalDF):

    regions = ['BC', 'ALBERTA', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']


    chosenRegions = []
    for index in chosenDataSets:
        chosenRegions.append(regions[int(index) - 1])


    setOfUniqueNames = []
    regionsUniqueTotal = []
    namesTemp = []
    for area in chosenRegions:
        uniquePerRegion_df = totalDF[totalDF['Regions'] == area]

        namesTemp = uniquePerRegion_df['Names'].unique()
        setOfUniqueNames.extend(namesTemp)
    
        
        regionsTemp = [area] * len(namesTemp)
        regionsUniqueTotal.extend(regionsTemp)

    
        

    uniqueNames = {'Names': setOfUniqueNames, 'Regions':regionsUniqueTotal }
    uniqueNames_df = pd.DataFrame(uniqueNames)
    uniqueNames_df.sort_values(['Regions'], axis = 0, ascending=[True], inplace=True)
            

    return uniqueNames_df
    
