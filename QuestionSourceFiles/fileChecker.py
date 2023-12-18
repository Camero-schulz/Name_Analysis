import os

def fileCheck(fold):
    
    gender = ["M_", "F_"]
    places = ["USA", "Alberta", "BC", "NewBrunswick", "NovaScotia", "Quebec"]
    check = True
    for i in places:
        
        for j in gender:
            isExisting = os.path.exists(fold+"/"+j+i+".csv")
            if isExisting == False:
                print("The file "+j+i+".csv does not exist in the directory "+fold)
                check = isExisting
    

    #Checks for ethncicity CSV
    isExisting = os.path.exists("../EthnicityCSVFiles/first_nameRaceProbs.csv")
    if isExisting == False:
        print("The file first_nameRaceProbs.csv does not exist in the directory EthnicityCSVFiles")
        check = isExisting

    return check


#fold = "../CSVFiles"
#fileCheck(fold)
