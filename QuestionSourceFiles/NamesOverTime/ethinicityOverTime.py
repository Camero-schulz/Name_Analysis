

import pandas as pd
import csv
from NamesOverTime.other_functions import *





#This function returns the percent of people of each of the 5 given ethnicities from 1980 to 2018

def each_ethnicty_over_years_percentage(ethnictyProv_df, names_time_df):


    white = []
    black = []
    hispanic = []
    asian = []
    other = []
    totalPeople = []
    yearsList =[]
    for year in range(1980, 2018):
        listOfEthnicityOverYears = (amount_of_each_ethnicty(ethnictyProv_df, names_time_df, year))
        yearsList.append(year)
        white.append(listOfEthnicityOverYears[0])
        black.append(listOfEthnicityOverYears[1])
        hispanic.append(listOfEthnicityOverYears[2])
        asian.append(listOfEthnicityOverYears[3])
        other.append(listOfEthnicityOverYears[4])
        totalPeople.append(listOfEthnicityOverYears[5])
    

    

    for i in range(0, 38):
        white[i] = white[i]/totalPeople[i] * 100
        black[i] = black[i]/totalPeople[i] * 100
        hispanic[i] = hispanic[i]/totalPeople[i] * 100
        asian[i] = asian[i]/totalPeople[i] * 100
        other[i] = other[i]/totalPeople[i] * 100




    


    ethincityPrecentage = {'Years': yearsList, 'White': white, 'Black': black, 'Hispanic': hispanic, 'Asian': asian, 'Other': other }
    
    return ethincityPrecentage



#This function makes a data frame with the predicted amount of each ethnicity in given year
#returns a list of length 5 with the last being the total people
#Note some names may not be in the ethnicty probability data frame which will lower percentages
def amount_of_each_ethnicty(ethnictyProb_df, names_time_df, year):

    index = int(year) - 1980
    whiteFreq = 0
    blackFreq = 0
    hispanicFreq = 0
    asianFreq = 0
    otherFreq = 0
    totalPeople = 0

    
 
    ethnictyProb_names_df = ethnictyProb_df[ethnictyProb_df['Names'].isin(names_time_df['Names'])]
    
    names_time_checked_df =  names_time_df[names_time_df['Names'].isin(ethnictyProb_names_df['Names'])]
   


    for name in names_time_checked_df.iterrows():
        
        whiteFreq = whiteFreq + float(name[1][1][index]) * ethnictyProb_names_df[ethnictyProb_names_df['Names'] == name[1][0]].iloc[0,1]
        blackFreq = blackFreq + float(name[1][1][index]) * ethnictyProb_names_df[ethnictyProb_names_df['Names'] == name[1][0]].iloc[0,2]
        hispanicFreq = hispanicFreq + float(name[1][1][index]) * ethnictyProb_names_df[ethnictyProb_names_df['Names'] == name[1][0]].iloc[0,3]
        asianFreq = asianFreq + float(name[1][1][index]) * ethnictyProb_names_df[ethnictyProb_names_df['Names'] == name[1][0]].iloc[0,4]
        otherFreq = otherFreq + float(name[1][1][index]) * ethnictyProb_names_df[ethnictyProb_names_df['Names'] == name[1][0]].iloc[0,5]
        totalPeople = totalPeople + int(name[1][1][index])


    return[whiteFreq, blackFreq, hispanicFreq, asianFreq, otherFreq, totalPeople]


#This function makes a dataframe with names and a corsponding probability for each of the 5 defined ethnicities
def open_ethnicty_probability():

    path = __file__
    path = path[0 : len(path) - len('/QuestionSourceFiles/NamesOverTime/ethnicityOverTime.py')]
    path = path + "/EthnicityCSVFiles/first_nameRaceProbs.csv"

    names = []
    white = []
    black = []
    hispanic = []
    asian = []
    other = []


    with open(path) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        iterationsRan = 0
        for row in csvReader:
            iterationsRan += 1
            if(iterationsRan > 1):
                
                names.append(row[0])
                white.append(float(row[1]))
                black.append(float(row[2]))
                hispanic.append(float(row[3]))
                asian.append(float(row[4]))
                other.append(float(row[5]))
    

    ethnicityProb = {'Names': names, 'White': white, 'Black': black, 'Hispanic': hispanic, 'Asian': asian, 'Other': other}

    ethnicityProb_df = pd.DataFrame(ethnicityProb)
                

    return ethnicityProb_df







###################################

#The follwing functions create a data frame with all names from a data set and a corrosponding list of frequencies
#of that name from year 1980-2018
######################################




def all_names_over_years(chosenDataSet,gender):


    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']


    namesInRegion = all_chosen_data_sets(chosenDataSet, gender)
    
    
    listOfNameFrequencyOverYears = []
    for name in namesInRegion:
        listOfNameFrequencyOverYears.append(names_over_years(name, setOfFiles[int(chosenDataSet)-1], gender))

    people = {'Names': namesInRegion, 'FrequencyList': listOfNameFrequencyOverYears}

    people_df = pd.DataFrame(people)

    
    return people_df 
    
        

        


def names_over_years(name, region, gender):
    
    #finds the occurences of a name from 1980 - 2018
    overYears = []

    for year in range(1980,2018):
        
        overYears.append(name_in_year([name, region, year], gender))

    return overYears





def name_in_year(region_data, gender): # the rank of the name in a given year
    #region_data = [str(name),str(region name),int(year)]
    if (len(region_data) != 3 or len(region_data[0]) == 0 or len(region_data[1]) == 0 or len(str(region_data[2])) != 4):
        print("Error: invalid input for highest_rank_year")

    else:
        files = open_csv(region_data[1])
        if files != -1:
            csv_m = files[0]
            csv_f = files[1]

            m_placement = [] #hows the request info when found
            f_placement = [] 

            for row in csv_m:
                if ((int(row[0]) != region_data[2])): #checks year
                    pass
                else:
                    if (row[1].upper() == region_data[0].upper()): #checks name
                        m_placement = row

            for row in csv_f:
                if (int(row[0]) != region_data[2]):
                    pass
                else:
                    if (row[1].upper() == region_data[0].upper()):
                        f_placement = row
            files[2].close()
            files[3].close()

            
            

            if(gender == 'M'):
                try:
                    return(m_placement[2])
                except:
                    return 0
            elif(gender == 'F'):
                try:
                    return(f_placement[2])
                except:
                    return 0
            else:
                print('')



