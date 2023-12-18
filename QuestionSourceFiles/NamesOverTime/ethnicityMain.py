try: 
    from NamesOverTime.visualizeEthnicity import *
    
    from NamesOverTime.other_functions import user_input
except:
    print("Modules not found")


COMPLETEDCHAR = 0


def ethnicityMain():
    print("Would you like to analyze Female or Male Names:")
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
    #Commemted sets have been removed because the code is unable to run in a reasonable time
    #print("British Columbia: '1'")
    #print("Alberta: '2'")
    #QUebec removed because of to many unique names that are not in the harvard data set
    #print("United States of America: '4'")
    print("5) New Brunswick:")
    print("6) Nova Scotia")
    
    continueRun = 'y'
    areaChosen = user_input(['5','6'])

    isFileMade = ethnicityDataExists(areaChosen, genderChosen)

    if(isFileMade == False):
        print("This Ethnicity Data has not been processed.")
        print("This could take a significant amount of time to run.")
        print("Are you sure you would like to run this now?")
        print('y) Yes')
        print("n) No")
        continueRun = user_input(['y', 'n'])
        if(continueRun == 'y'):
            print("Processing now...")
            makeCSVEthnicityData(areaChosen, genderChosen)
            print("CSV File Created, Done Processing")
    

    if(continueRun == 'y'):
        visualizeEthnicityData(getCSVEthnicityData(areaChosen, genderChosen), areaChosen, genderChosen)
    else:
        print("Exiting...")
    

    



    
