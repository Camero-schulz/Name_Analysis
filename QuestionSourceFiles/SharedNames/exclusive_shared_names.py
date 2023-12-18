#!/usr/bin/env python3

#Written By Ian Fuller-Thomson


AMOUNTOFDATASETS = 6
COMPLETEDCHAR = '0'
TOTALDATASETS = 6


try:
    import pandas as pd
    from SharedNames.general_functions import *
except ModuleNotFoundError:
    print("Did not import all required libraries")


                
def exclsuive_main():
    print("Would you like to compare Female or Male Names?")
    print("1) Male")
    print("2) Female")
    genderChosen = user_input(['1', '2'])
    if(genderChosen == '1'):
        genderChosen = 'M'
    elif(genderChosen == '2'):
        genderChosen = 'F'
    else:
        print("User_Input had a critical error")
        return

    print( "Input which set of names you would like to compare: ")
    print("1) British Columbia")
    print("2) Alberta")
    print("3) Quebec")
    print("3) United States of America")
    print("5) New Brunswick")
    print("6) Nova Scotia")
    print( COMPLETEDCHAR +") Confirm Choices")
    shared_names_input(genderChosen)


def shared_names_input(genderChosen):
    amountOfInputs = []
    

    menuDone = False
    posssibleInputList = ['1', '2', '3', '4','5', '6', COMPLETEDCHAR]
    dataSets = ['British Columbia', 'Alberta', 'Quebec', 'United States Of America', 'New Brunswick', 'Nova Scotia']
    chosenDataSets = []
    


    while((len(amountOfInputs) <= AMOUNTOFDATASETS + 1 or input == COMPLETEDCHAR) and menuDone == False):
        
        if(len(chosenDataSets) < 2):
            print("Please choose a data set")
            
        elif(len(chosenDataSets) < AMOUNTOFDATASETS):
            print("Please choose a data set or Confirm")
            
        else:
            print("Please Confirm")
            

        
        
        input = user_input(posssibleInputList)
        
        
        
        if(len(chosenDataSets) < 2 and COMPLETEDCHAR == input):
            print("Please input at least two Data Sets")
            

        elif(input == COMPLETEDCHAR):

            print("Datasets Chosen")
            

            exclusive_names(chosenDataSets, genderChosen)
            menuDone = True

        elif(len(chosenDataSets) == AMOUNTOFDATASETS and input != COMPLETEDCHAR):
            print("Please input " + COMPLETEDCHAR + " to confirm")
            

        elif(input in chosenDataSets and len(chosenDataSets) == AMOUNTOFDATASETS):
            print("Data Sets already chosen please confirm your choices")
            

        elif(input in chosenDataSets):
            print("Data Set already chosen please pick a diffrent data set or confirm your choices")
            

        elif(input != COMPLETEDCHAR):
            
            print(dataSets[int(input) -1] + ' was inputed.')
            chosenDataSets.append(input)



        
        
        
            
def exclusive_names_one_gender(chosenDataSets, gender):


    #Gender must by, M or F
    if(gender != 'F' and gender != 'M'):
        return ValueError
    try:
        total_df = all_chosen_data_sets(chosenDataSets, gender)
    except FileNotFoundError:
        empty = []        
        return pd.DataFrame({'Names': empty, 'Regions': empty})
    
    
    uniqueNamesPerRegion_df = unique_names_per_region(chosenDataSets, total_df)
    
    


    return uniqueNamesPerRegion_df

def exclusive_names(chosenDataSets, genderChosen):
    regions = ['BC', 'ALBERTA', 'Quebec', 'USA', 'NewBrunswick', 'NovaScotia']
    regionsUsed = []
    for set in chosenDataSets:
        regionsUsed.append(regions[int(set) -1])
    
    uniqueNamesMaleRegion_df = exclusive_names_one_gender(chosenDataSets, genderChosen)
        
    setOfDupilcatesIndexWithBoolean = uniqueNamesMaleRegion_df.duplicated(subset = ['Names'],keep=False)        
    # setOfDupilcatesIndex = []

    
    uniqueNamesMaleRegion_df = uniqueNamesMaleRegion_df.assign(Duplicates=setOfDupilcatesIndexWithBoolean)

    namesInOnlyOneRegion = uniqueNamesMaleRegion_df[uniqueNamesMaleRegion_df['Duplicates'] == False]

        
    
    # for i in range(len(setOfDupilcatesIndex)):
    #     if setOfDupilcatesIndexWithBoolean[i] == False:
    #         setOfDupilcatesIndex.append(i+1)


    #namesInOnlyOneRegion = uniqueNamesMaleRegion_df.filter(items=setOfDupilcatesIndex, axis = 0)

   
    for currentRegion in regionsUsed:
        print("Number of Names only in " + currentRegion + ": ", end='')
                
        toPrint = namesInOnlyOneRegion[namesInOnlyOneRegion['Regions'] == currentRegion]
        print(len(toPrint))

        print("Would you like to see the Exclusive Names for :" + currentRegion)
        print("0 for No, 1 for Yes")
        answer = user_input(['0','1'])
        if(answer == '1'):
            printNamesInDF(toPrint)

                
