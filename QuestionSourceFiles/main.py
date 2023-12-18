#!/usr/bin/env python3
import os

direct = os.getcwd()

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')


try:
    from fileChecker import fileCheck
    from SpecificName.SNInputFunctions import key_input

except:
    print("Error, could not import required functions")
    exit(0)

allExists = fileCheck("../CSVFiles")

if allExists == True:
    key = -1

    print("\nWelcome to team Beaver's name analysis")

    while (key != '0' and key != 'n'):
        for i in range(1,39):
            print("*",end="")
        print("\nWhat function would you like to use?")
        print("1) Find how a specific name campares over time")
        print("2) See what names are only in one out of 2 or more regions")
        print("3) See what the most popular was in a region in a given year")
        print("4) Sorts names that start with the letter entered by the user")
        print("5) See the percentage of diffrent ethnic groups from 1980-2018")
        print("6) See the top 10 most used names in our databases from 1980-2018")
        print("0) exit")
        for i in range(1,39):
            print("*",end="")
        print("\nPress the key of the function you want")

        try:
            key = key_input(['0','1','2','3','4', '5','6'])
        except:
            print("Error, could not get key input")

        if (key == '1'):
            try:
                from SpecificName.SNMain import specific_main
                specific_main()
            except:
                pass
            
        elif (key == '2'):
            try:
                from SharedNames.exclusive_shared_names import exclsuive_main
                exclsuive_main()
            except:
                pass
        
        elif (key == '3'):
            try:
                from MostFrequent.mostFrequent import mostFrequent_main
                mostFrequent_main()
                
            except Exception as e: 
                print(e)
                pass
            
        elif (key == '4'):
            from ComparingFirstLetter.compareFirstLetter import CFL_main
            CFL_main()
        
        elif(key == '5'):
            from NamesOverTime.ethnicityMain import ethnicityMain
            ethnicityMain()
        
        elif(key == '6'):
            try:
                from MostFrequentViz.mainMFV import mainMFV
                mainMFV()
                
            except Exception as e: 
                print(e)
                pass


        else:
            exit(0)

        print("\nDo you want to use another function?")
        print("y) Yes")
        print("n) No")
        key = '0'
        try:
            key = key_input(['y','n'])
        except:
            print("input error")

elif allExists == False:
    print("Therefore the whole program has been terminated")
    exit(0)