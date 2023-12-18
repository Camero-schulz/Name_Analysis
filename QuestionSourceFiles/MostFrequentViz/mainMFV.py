import os
import sys
import getopt
import csv
import pandas as pd
import matplotlib
# matplotlib.use('TkAgg', force=True)
import matplotlib.pyplot as plt
from MostFrequentViz.mostFrequentViz import *
from input_functions import key_input

def mainMFV():
    usefulYears = []
    theYear = 0
    for i in range(1980, 2019):
        usefulYears.append(i)

    location = "../CSVFiles"
    print("\nWhat is the preferred gender?\n1) Male \n2) Female\n3) Both\n\nEnter: ")
    gender = key_input(["1", "2", "3"])
    inputFileName = regionListMaker(location, gender)
    while theYear not in usefulYears:
        theYear = input("\nEnter a year ( between 1980 -- 2018 ): ")
        try:
            theYear = int(theYear)
        except:
            pass
        if theYear not in usefulYears:
            print("The year entered is not in range not in range")

    people_df = mostFrequentDFMaker (inputFileName,theYear)
    mostFrequentVisualizer(people_df, gender, theYear)
