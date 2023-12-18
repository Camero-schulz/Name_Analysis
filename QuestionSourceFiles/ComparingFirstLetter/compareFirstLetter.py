#!/usr/bin/env python3

### Comparing first letter ###

import pandas as pd
import sys
import getopt
import csv
import os
import readline
import matplotlib.pyplot as plt
import numpy as np

from ComparingFirstLetter.input_functions import key_input
from ComparingFirstLetter.CFL_Functions import *
from ComparingFirstLetter.CFL_Graph import *


direct = os.getcwd()
dir_prefix = ''

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')


# Need this to sort data properly with names
def sort_key(data):
  return data[1]

def CFL_main():

  # Gathers all acceptable letters -- everything between (a, z) and (A, Z)
  allLetters = []   # list of all acceptable characters for key_input
  for i in range (ord('a'), ord('z')+1):
    allLetters.append(chr(i))

  for i in range (ord('A'), ord('Z')+1):
    allLetters.append(chr(i))

  print("\n---------------------MENU---------------------")
  print("FILE:")
  print("1) Alberta FILE")
  print("2) British Columbia FILE")
  print("3) Quebec FILE")
  print("4) USA FILE")
  print("5) New Brunswick FILE")
  print("6) Nova Scotia FILE")
  fileInput = key_input(['1', '2', '3', '4', '5', '6'])
  fileInput = (int(fileInput)) - 1
  fileOptions = ["Alberta", "BC", "Quebec", "USA", "NewBrunswick", "NovaScotia"]

  print("\nGENDER:")
  print("1) Male names only")
  print("2) Female names only")
  print("3) Male and Female names")
  genderInput = key_input(['1', '2', '3'])

  print("\nCOMPARE FIRST LETTER:")
  print("Please enter a single character: ")
  charInput = key_input(allLetters)
  charInput = charInput.upper()

  print("\nTIME FRAME:")
  print("1) Over a single year")
  print("2) Over many years")
  print("3) Every single year - WARNING: This input could take upwards of five minutes or more based on the letter entered")
  yearInput = key_input(['1', '2', '3'])


  # FOR FILE / GENDER INPUT
  # Male input
  if (genderInput == '1' or genderInput == '3'):
    namesM, gender, inputFileNameM = determineFile(genderInput, fileOptions, fileInput)
  # Female input
  if (genderInput == '2' or genderInput == '3'):
    genderInput = '2'
    namesF, gender, inputFileNameF = determineFile(genderInput, fileOptions, fileInput)


  # TO DETERMINE THE COMPLETE RANGE OF YEARS
  if gender == "male":
    begYear, endYear = rangeOfYears(inputFileNameM)
  elif gender == "female":
    begYear, endYear = rangeOfYears(inputFileNameF)
  else:
    print("Error: File not found")
    sys.exit()  


  # FOR YEAR INPUT
  years = timeFrame(yearInput, begYear, endYear)


  print("\nEFFICIENCY - Ignore names based on popularity:")
  print("1) Use all names in the file regardless of number of entries")
  print("2) Ignore names with ONE entry per year")
  print("3) Ignore names with TWO entries or less per year")
  print("4) Ignore names with FIVE entries or less per year")
  print("5) Ignore names with TEN entries or less per year")
  entryInput = key_input(['1', '2', '3', '4', '5'])

  # FOR EFFICIENCY INPUT
  ignore = efficiency(entryInput)


  # Determines all male names which starts with the userInput
  if 'namesM' in locals():
    totalNamesM = []
    for i in range (len(years)):
      namesM, totalNamesM = openCSVFileName(inputFileNameM, namesM, years[i], charInput, totalNamesM, ignore)

    print("\nThere are {0} different male names that start with '{1}'".format(len(totalNamesM), charInput))
    print("For efficiency, we are reading only {0} male names".format(len(namesM)))

    total = []
    # Finds the ranking of each name in the list
    for j in range (len(namesM)):
      total = openCSVFileTotal(inputFileNameM, total, years, namesM[j])

    data = (list(zip(namesM, total)))       # Creates a list from two sepeate lists
    data.sort(key=sort_key, reverse=True)   # Sorts names and numbers from highest to lowest
      
    # prints results
    print("\n")
    print("PRINTING THE TOP 50 MALE NAMES")
    print("{:>12}{:>16}".format("MALE NAMES:", "TOTAL:"))
    for i in range (50):
      try:
        print("{:>12}{:>16}".format(data[i][0], data[i][1]))
      except IndexError:
        break
    print("\n")

    if (len(totalNamesM) >= 1):
      print("Would you like to see the data visually? (Y/N): ")
      graphQ = key_input(['y', 'Y', 'n', 'N'])
      if (graphQ == 'y' or graphQ == 'Y'):
        create(data, charInput, "male")



  # Determines all female names which starts with the userInput
  if 'namesF' in locals():  
    totalNamesF = []
    for i in range (len(years)):
      namesF, totalNamesF = openCSVFileName(inputFileNameF, namesF, years[i], charInput, totalNamesF, ignore)

    print("\nThere are {0} different female names that start with '{1}'".format(len(totalNamesF), charInput))
    print("For efficiency, we are reading only {0} female names".format(len(namesF)))

    total = []
    # Finds the ranking of each name in the list
    for j in range (len(namesF)):
      total = openCSVFileTotal(inputFileNameF, total, years, namesF[j])

    data1 = (list(zip(namesF, total)))       # Creates a list from two sepeate lists
    data1.sort(key=sort_key, reverse=True)   # Sorts names and numbers from highest to lowest

    # print results
    print("\n")
    print("PRINTING THE TOP 50 FEMALE NAMES")
    print("{:>12}{:>16}".format("FEMALE NAMES:", "TOTAL:"))
    for i in range (50):
      try:
        print("{:>12}{:>16}".format(data1[i][0], data1[i][1]))
      except IndexError:
        break
    print("\n")

    if (len(totalNamesF) >= 1):
      print("Would you like to see the data visually? (Y/N): ")
      graphQ = key_input(['y', 'Y', 'n', 'N'])
      if (graphQ == 'y' or graphQ == 'Y'):
        create(data1, charInput, "female")

    

    


if __name__ == "__main__":
  CFL_main()
