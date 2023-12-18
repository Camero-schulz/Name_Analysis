import os
import sys
import getopt
import csv
import pandas as pd

try:
    from MostFrequent.input_functions import key_input
except:
    print("Error: could not import processing functions")

def getListOfFiles(fileLocation):
    listOfFiles = []
    count = 0
    for i in os.listdir(fileLocation):
        if ".csv" in i:
            listOfFiles.append(i[2:-4])
    
    if len(listOfFiles) == 0:
        print("No files found")
    else:
        return listOfFiles

def printListOfFiles(listForDisplay):
    if len(listForDisplay) == 0:
        print("No Available regions")
    else:
        count = 1
        numList = []
        print("The available regions are: ")
        listForDisplay = list(dict.fromkeys(listForDisplay))
        for i in listForDisplay:
            print(f"{count}) {i}")
            numList.append(str(count))
            count = count + 1
        return numList

def getGender():
    print("\nWhat is the preferred gender?\n1) Male \n2) Female\n\nEnter ( 1 or 2 ): ")
    gender = key_input(["1", "2"])
    if gender == "1":
        return "M_"
    elif gender == "2":
        return "F_"

def largestNameChecker(inputFileName, fileLocation):
    num = len(fileLocation) + 1
    greatestNum = 0
    greatestYear = 0
    if inputFileName[num] == 'M':
        gender = " male "
        location = inputFileName[num+2:-4]
    elif inputFileName[num] == 'F':
        gender = " female "
        location = inputFileName[num+2:-4]
    else:
        gender = " "
        location = inputFileName[:-4]
    
    try:
        with open ( inputFileName ) as csvDataFile:
            next ( csvDataFile )  
            csvReader = csv.reader(csvDataFile, delimiter=',')

            for row in csvReader: 
                
                if int(row[2]) >= int(greatestNum):
                    greatestName = row[1]
                    greatestYear = row[0]
                    greatestNum = row[2]
            
            print(f"The most frequently used{gender}name ever in {location} was {greatestName} in the year {greatestYear} with a frequency of {greatestNum}")
    except:
        print("Error: could not open file properly")

def yearRange(inputFileName, fileLocation):
    year = [0]
    try:
        with open ( inputFileName ) as csvDataFile:
            next ( csvDataFile )  
            csvReader = csv.reader(csvDataFile, delimiter=',')

            for row in csvReader: 
                if int(row[0]) != int(year[-1]):
                    year.append(row[0])
        year.remove(0)
        return year

    except:
        print("Error: could not open file properly")

def yearRangeChecker(listOfYears):
    inRange = False
    while inRange == False:
            print(f"Enter a year (between {listOfYears[0]} - {listOfYears[-1]}): ")
            theYear = str(input())
            inRange = theYear in listOfYears
            if inRange == False:
                print("Input is not within the given range. \nTry again")

    return theYear

def largestNameOfTheYearChecker(inputFileName, fileLocation, theYear):
    num = len(fileLocation) + 1
    greatestNum = 0
    
    if inputFileName[num] == 'M':
        gender = " male "
        location = inputFileName[num+2:-4]
    elif inputFileName[num] == 'F':
        gender = " female "
        location = inputFileName[num+2:-4]
    else:
        gender = " "
        location = inputFileName[:-4]
    
    try:
        with open ( inputFileName ) as csvDataFile:
            next ( csvDataFile )  
            csvReader = csv.reader(csvDataFile, delimiter=',')

            for row in csvReader: 
                if int(row[0]) == int(theYear):
                    if int(row[2]) >= int(greatestNum):
                        greatestName = row[1]
                        greatestNum = row[2]
                
            print(f"In the year {theYear}, the most frequently used{gender}name in {location} was {greatestName} with a frequency of {greatestNum}")
    except:
        print("Error: could not open file properly")