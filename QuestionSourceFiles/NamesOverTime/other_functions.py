#!/usr/bin/env python3


import csv
import pandas as pd
import sys
import tty
import termios
import os

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
    
           


def open_csv(region_data):
    #region_data = regionName
    #ensures that the current directory is valid and gets to correct location
    direct = os.getcwd()
    dir_prefix = ''

    if (direct[-18:] == 'teamprojectcis2250'):
        dir_prefix = ''
    elif (direct[-19:] == 'QuestionSourceFiles'):
        dir_prefix = '../'
    elif (direct[-12:] == 'NamesOverTime'):
        dir_prefix = '../../'
    else:
        print("Error: invalid running directory")

    try:
        #opens files and makes sure they are valid
        f_file_name = dir_prefix+"CSVFiles/F_"+region_data+".csv"
        m_file_name = dir_prefix+"CSVFiles/M_"+region_data+".csv"
        F_file = open(f_file_name, "r")
        M_file = open(m_file_name, "r")

        if F_file == None or M_file == None:
            raise Exception
        else:
            csv_m = csv.reader(M_file, delimiter = ',')
            next(csv_m)

            #checks to make sure correct formatting
            for row in csv_m:
                if len(row) != 4:
                    raise Exception
                row[0] = int(row[0])
                row[2] = int(row[2])
                row[3] = int(row[3])
                break
            csv_f = csv.reader(F_file, delimiter = ',')
            M_file.seek(0)
            next(M_file)

            next(csv_f)
            for row in csv_f:
                if len(row) != 4:
                    raise Exception
                row[0] = int(row[0])
                row[2] = int(row[2])
                row[3] = int(row[3])
                break
            F_file.seek(0)
            next(F_file)

            return [csv_m, csv_f,F_file,M_file]

    except:
        print("Error: could not open valid csv data files")
        return -1
    



#This function takes the chosen data sets and the gender wanted and returns a data frame of all names, year and region in that set
def all_chosen_data_sets(chosenDataSet, gender):
    
    #Gender must by, M or F
    if(gender != 'F' and gender != 'M'):
        return ValueError
    
    path = __file__

    #path = os.getcwd()
    new_path = path[0 : len(path) - len('/QuestionSourceFiles/NamesOverTime/other_functions.py')]
    
    new_path = new_path + '/CSVFiles/'
    # path = 'CSVFiles/'
    beginning = new_path + gender + '_'
    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    ending = '.csv'
    chosenSetOfFiles= []
    
    chosenSetOfFiles.append(setOfFiles[int(chosenDataSet) - 1])
        


    names = []
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
                        
    return names

            