#!/usr/bin/env python3

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib
    from NamesOverTime.ethinicityOverTime import *
    #NEEDS TO DOWNLOAD tk using sudo apt-get install python3-tk
except:
    print("Modules not found")


#THis function creates and prints the ethnicity graph
def visualizeEthnicityData(ethnicityPercentage, areaChosen, genderChosen):

    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    region = setOfFiles[int(areaChosen) - 1]
    setOfGenders = ['Male', 'Female']
    if(genderChosen == 'F'):
        gender = setOfGenders[1]
    if(genderChosen == 'M'):
        gender = setOfGenders[0]

    

    x = np.array(ethnicityPercentage['Years'])


    yWhite = np.array(ethnicityPercentage['White'])
    yBlack = np.array(ethnicityPercentage['Black'])
    yHispanic = np.array(ethnicityPercentage['Hispanic'])
    yAsian = np.array(ethnicityPercentage['Asian'])
    yOther = np.array(ethnicityPercentage['Other'])
    legend_drawn_flag = True
    


    plt.plot(x, yWhite)
    plt.plot(x, yBlack)
    plt.plot(x, yHispanic)
    plt.plot(x, yAsian)
    plt.plot(x, yOther)
    plt.xlabel("Years") # add X-axis label
    plt.ylabel("Percentage Of Ethnicity") # add Y-axis label
    plt.title("Percentage of Ethnicities in " + gender + "'s from "+ region +" from 1980-2018") # title

    plt.legend(["White", "Black", "Hispanic", "Asian", "Other"], loc=0, frameon=legend_drawn_flag)
    plt.show()
    
def ethnicityDataExists(areaChosen,gender):
    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    region = setOfFiles[int(areaChosen) - 1]


    path = __file__

    #path = os.getcwd()
    path = path[0 : len(path) - len('/QuestionSourceFiles/NamesOverTime/visualizeEthnicity.py')]
    path = path + "/EthnicityCSVFiles/ethnicityVisualization"+ gender + "_" + region + ".csv"
    isExisting = os.path.exists(path)
    return isExisting



def makeCSVEthnicityData(areaChosen, gender):

    nameFreqOverYears = all_names_over_years(areaChosen, gender)
    ethnicProb = open_ethnicty_probability()

    ethnicityPercentage = each_ethnicty_over_years_percentage(ethnicProb, nameFreqOverYears)
    ethnicityPercentage_df = pd.DataFrame(ethnicityPercentage)

    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']

    region = setOfFiles[int(areaChosen) - 1]
    path = __file__
    path = path[0 : len(path) - len('/QuestionSourceFiles/NamesOverTime/visualizeEthnicity.py')]
    path = path + "/EthnicityCSVFiles/ethnicityVisualization"+ gender + "_" + region + ".csv"
    
    ethnicityPercentage_df.to_csv(path, sep=',', index=False, encoding='utf-8')

def getCSVEthnicityData(areaChosen, gender):

    setOfFiles = ['BC', 'Alberta', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    region = setOfFiles[int(areaChosen) - 1]

    #Gender must by, M or F
    if(gender != 'F' and gender != 'M'):
        return ValueError
    
    path = __file__

    #path = os.getcwd()
    path = path[0 : len(path) - len('/QuestionSourceFiles/NamesOverTime/visualizeEthnicity.py')]
    
    path = path + "/EthnicityCSVFiles/ethnicityVisualization"+ gender + "_" + region + ".csv"
    # path = 'CSVFiles/'

    white = []
    black = []
    hispanic = []
    asian = []
    other = []
    yearsList =[]
    
    
           
    with open(path) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        iterationsRan = 0
        for row in csvReader:
            iterationsRan += 1
            if(iterationsRan > 1):
                
                yearsList.append(int(row[0]))
                white.append(float(row[1])) 
                black.append(float(row[2])) 
                hispanic.append(float(row[3])) 
                asian.append(float(row[4])) 
                other.append(float(row[5])) 
               
                
    ethincityPrecentage = {'Years': yearsList, 'White': white, 'Black': black, 'Hispanic': hispanic, 'Asian': asian, 'Other': other }
    
    return ethincityPrecentage


