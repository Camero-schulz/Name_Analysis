#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

try:
    from MostFrequent.lC import *
    from MostFrequent.input_functions import key_input
except:
    print("Error: could not import processing functions")
 
# def main ( argv ):
def mostFrequent_main ():
    print()
    # Initializations
    listForDisplay = []
    numList = []
    num = 0
    fileLocation = "../CSVFiles"

    # Gets list of files from this location
    listForDisplay = getListOfFiles(fileLocation)
    
    # Prints the available regions 
    numList = printListOfFiles(listForDisplay)

    # Takes in user's choice of region
    print("\nEnter the numbers beside them to select: ")
    num = key_input(numList)

    # Gets the gender of the wanted file
    genderPrefix = getGender()

    # Creates file address
    inputFileName = fileLocation + "/" + genderPrefix + listForDisplay[int(num) -1] + ".csv"
    print("\nWould you prefer?\n1) The most popular name all time?\n2) The most popular name of a specific year\n\nEnter ( 1 or 2 ): ")
    yearSpecifics = key_input(["1", "2"])
    # inRange = False
    
    if yearSpecifics == "1":
        largestNameChecker(inputFileName, fileLocation)
    
    elif yearSpecifics == "2":
        listOfYears = yearRange(inputFileName, fileLocation)
        theYear = yearRangeChecker(listOfYears)
        largestNameOfTheYearChecker(inputFileName, fileLocation, int(theYear))


#
#   End of names.py
#
