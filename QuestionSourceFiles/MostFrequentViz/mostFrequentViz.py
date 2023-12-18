import os
import sys
import getopt
import csv
import pandas as pd
import matplotlib
# matplotlib.use('TkAgg', force=True)
import matplotlib.pyplot as plt

def regionListMaker(location,gender):
    if gender == "1":
        gender = "M"
    if gender == "2":
        gender = "F"
    inputFileName = []
    
    places = ["USA", "Alberta", "BC", "NewBrunswick", "NovaScotia", "Quebec"]
    
    if gender == "3":
        for j in places:
            inputFileName.append(location + '/' + 'M_' + j + ".csv")
            inputFileName.append(location + '/' + 'F_' + j + ".csv")
    else:
        for j in places:
            inputFileName.append(location + '/' + gender + '_' + j + ".csv")

    return inputFileName




def mostFrequentDFMaker(inputFileName, theYear):
    
    storedNames = []
    storedTotals = []
    for i in range(len(inputFileName)):
        with open ( inputFileName[i] ) as csvDataFile:
            next ( csvDataFile )  
            csvReader = csv.reader(csvDataFile, delimiter=',')

            for row in csvReader: 
                if int(row[0]) == int(theYear):
                        if row[1] in storedNames:
                            
                            i = storedNames.index(row[1])
                            storedTotals[i] = int(row[2]) + storedTotals[i]
                        else:
                            storedTotals.append(int(row[2]))
                            storedNames.append(row[1])



    people = {'Names':storedNames,'Totals':storedTotals}
    people_df = pd.DataFrame(people)
    people_df.sort_values(["Totals","Names"], axis = 0, ascending=[False, True], inplace=True) 
    line = "{:<15} {:>20}".format("Names", "Total Appearances")
    print(f"\n{line}")
    for n in range(0,10):
        line = "{:<15} {:>20}".format(people_df.iloc[n,0], people_df.iloc[n,1])
        print(line)
    return people_df


def mostFrequentVisualizer(people_df, gender, theYear):
    

    if gender == "3":
        genderWord = " "
    elif gender == "1":
        genderWord = " Male "
    elif gender == "2":
        genderWord = " Female "
    namesList = people_df['Names'].values.tolist()
    totalsList = people_df['Totals'].values.tolist()
    # print(namesList[0:10])
    # print(totalsList[0:10])
    plt.bar(namesList[0:10], totalsList[0:10])

    plt.title(f'The Most Popular{genderWord}Names of {theYear}')
    plt.xlabel('Names')
    plt.ylabel('Frequency')
    plt.show()

    

# def yearRangerForAll(inputFileName):
#     years = []
#     good = 0
#     prevYear = 0


#     for n in range(1923, 2023):
        
#         years.append(n)

#     for i in range(len(inputFileName)):
#         with open ( inputFileName[i] ) as csvDataFile:
#             next ( csvDataFile )  
#             csvReader = csv.reader(csvDataFile, delimiter=',')
#             currentYears = []
#             for row in csvReader:
#                 if int(row[0]) != prevYear:
#                     # print(int (row[0]))
#                     currentYears.append(int(row[0])) 
#                     prevYear = int(row[0])

#             for i in years:
#                 if i in currentYears:
#                     print(f"   {i}")
#                 else:
#                     print(i)
#                     years.remove(i)

    # for h in years:
    #     print(h)
    # print(good)

        # print(years)