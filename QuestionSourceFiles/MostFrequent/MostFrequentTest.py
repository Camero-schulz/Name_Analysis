#!/usr/bin/env python3
import os
direct = os.getcwd()

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'MostFrequent'):
    os.chdir('..')
else:
    print("Error: unsupported running directory")
    exit(0)

print(os.getcwd())

from lC import largestNameChecker

#Overall: the input is very restricted only allowing good input for user In which makes it difficult for a user to cause error
#could maybe add funciton to get the top name of a specific year rather than all time


#getListofFiles
#looks good, could be have an error message in case no files are there

#printListOfFiles
#Idk, maybe an error message incase the input list is empty

#largestNameChecker
#I would recomend checks to make sure that the files open properly and that they contain what they should
def largestNameCheckerTest():
    fileNames = ["Alberta", "BC","NewBrunswick","NovaScotia","Quebec","USA"]
    gender = ["M_","F_"]
    for i in fileNames:
        for j in gender:
            name = j+i+".csv"
            largestNameChecker(name,"../CSVFiles")

    print("Test 1: empty input")
    largestNameChecker("","")
    
largestNameChecker()