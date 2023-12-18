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

from MostFrequent.lC import largestNameChecker

def largestNameCheckerTest():
    fileNames = ["Alberta","BC","NewBrunswick","NovaScotia","Quebec","USA"]
    gender = ["M_","F_"]
    n = 0
    for i in fileNames:
        n+=1
        print("\nTest",str(n)+":",i)
        for j in gender:
            name = "../CSVFiles/"+j+i+".csv"
            largestNameChecker(name,"../CSVFiles")

    print("\nTest",str(n+1)+": empty input")
    largestNameChecker("","")
    
largestNameCheckerTest()