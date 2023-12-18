#!/usr/bin/env python3
import os
import random
direct = os.getcwd()

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')
print(os.getcwd())

from SpecificName.SNInputFunctions import *
from SpecificName.SNProcessingFunctions import *

region_options = ["Alberta","BC","Quebec","NewBrunswick","NovaScotia","USA"]
region_years = [[1980,2020],[1923,2021],[1980,2020],[1980,2018],[1920,2022],[1923,2021]]

#input_functions:
#single_year_input()
def single_in_testing():
    goAgain = True
    print("Without any input value:")
    year1 = single_year_input([])
    print(year1)

    while (goAgain == True):
        region = region_input()
        year = single_year_input(region)
        print(year)
        print("Run function again? y/n")
        key = key_input(['y','n'])
        goAgain = False
        if key == 'y':
            goAgain = True

#two_year_input()
def two_in_testing():
    goAgain = True
    print("Without any input value:")
    year1 = two_year_input([])
    print(year1)

    while (goAgain == True):
        region = region_input()
        year = two_year_input(region)
        print(year)
        print("Run function again? y/n")
        key = key_input(['y','n'])
        goAgain = False
        if key == 'y':
            goAgain = True

#open_csv()
def open_csv_testing():
    n=1

    print("run all? y/n")
    run_all = key_input(['y','n'])
    userIn = run_all

    if (userIn == 'n'):
        print("Run normal cases test? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):
        for region in region_options:
            csvs = open_csv(region)
            try:
                if (len(csvs) != 4 or csvs[0] == None or csvs[1] == None):
                    print("here")
                    raise Exception
                csvs[2].close()
                csvs[3].close()
                print("Test #"+str(n),":",region,"csv file success")
            except:
                print("General test", str(n), "failed.")
            print('\n', end='')
            n+= 1
    userIn = run_all

    if (userIn == 'n'):
        print("Run custom test cases? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):
        print("Test #"+str(n)+": empty name")
        csvs = open_csv('')
        if (csvs == None):
            print("Test Pass")
        else:
            print("Test Fail")
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": invalid name")
        csvs = open_csv('SillyLad')
        if (csvs == None):
            print("Test Pass")
        else:
            print("Test Fail")
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": int name")
        csvs = open_csv(1984)
        if (csvs == None):
            print("Test Pass")
        else:
            print("Test Fail")
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": file directory name")
        csvs = open_csv('../M_BC')
        if (csvs == None):
            print("Test Pass")
        else:
            print("Test Fail")
        print('\n', end='')
        n+=1


#processing_functions:
#highest_rank_year()
def highest_year_rank_test():
    n=1
    print("run all? y/n")
    run_all = key_input(['y','n'])
    userIn = run_all
    if (userIn == 'n'):
        print("Run custom cases? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):
        
        print("Test #"+str(n)+": empty name - should throw error")
        highest_rank_year(['',"BC", [1980,2018]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": backwards years - should work")
        highest_rank_year(['James',"USA", [2000,1980]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": string years - should throw error")
        highest_rank_year(['James',"BC", ["what","year"]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": empty years - should throw error")
        highest_rank_year(['Emma',"Quebec", []])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": not a name - should work but return 0")
        highest_rank_year(['1920s',"BC", [1980,2018]])
        n+=1
        print("\n", end='')
    
    userIn = run_all

    if (userIn == 'n'):
        print("Run generic cases test? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):

        for i in range(len(region_options)):
            print("Test #"+str(n)+": "+region_options[i])
            n+=1
            for j in range(3):
                year1 = random.randint(region_years[i][0],region_years[i][1])
                year2 = random.randint(region_years[i][0],region_years[i][1])
                highest_rank_year(["James",region_options[i],[year1, year2]])
            print('\n', end='')


#most_uses_year()
def most_uses_year_test():
    n=1
    print("run all? y/n")
    run_all = key_input(['y','n'])
    userIn = run_all

    if (userIn == 'n'):
        print("Run custom cases? y/n")
        userIn = key_input(['y','n'])
    if(userIn == 'y'):
        
        print("Test #"+str(n)+": empty list - should throw error")
        most_uses_year([])
        n+=1
        print("\n", end='')
        
        print("Test #"+str(n)+": empty name - should throw error")
        most_uses_year(['',"BC", [1980,2018]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": invalid region - should throw error")
        most_uses_year(['John',"SillyLand", [1980,2018]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": invalid years - should throw error")
        most_uses_year(['John',"BC", [1869,2072]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": single year - should throw error")
        most_uses_year(['John',"BC", [2000]])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": no year - should throw error")
        most_uses_year(['John',"Alberta"])
        n+=1
        print("\n", end='')

        print("Test #"+str(n)+": backwards years - should work")
        most_uses_year(['John',"USA", [2018,2000]])
        n+=1
        print("\n", end='')

    userIn = run_all

    if (userIn == 'n'):
        print("Run generic cases test? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):

        for i in range(len(region_options)):
            print("Test #"+str(n)+": "+region_options[i])
            n+=1
            for j in range(3):
                year1 = random.randint(region_years[i][0],region_years[i][1])
                year2 = random.randint(region_years[i][0],region_years[i][1])
                most_uses_year(["Claire",region_options[i],[year1, year2]])
            print('\n', end='')


#single_rank_year()
def single_year_rank_test():
    n=1

    print("run all? y/n")
    run_all = key_input(['y','n'])
    userIn = run_all

    if (userIn == 'n'):
        print("Run custom cases test? y/n")
        userIn = key_input(['y','n'])
    if (userIn == 'y'):
    
        print("Test #"+str(n)+": empty list - should throw error")
        single_year_rank([])
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": empty name - should throw error")
        single_year_rank(['','USA', 2000])
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": blank year - should throw error")
        single_year_rank(['Claire','BC',''])
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": massive year - should throw error")
        single_year_rank(['Claire','Alberta',99999999999999999999999999999999])
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": invalid region - should throw error")
        single_year_rank(['Jeremy','sillySpace',2000])
        print('\n', end='')
        n+=1

        print("Test #"+str(n)+": string year - should throw error")
        single_year_rank(['Emily','BC',"what"])
        print('\n', end='')
        n+=1


    userIn = run_all

    if (userIn == 'n'):
        print("Run general random year test? y/n")
        userIn = key_input(['y','n'])

    if (userIn == 'y'):
        for j in range(len(region_options)):
            print("Test #"+str(n)+": "+region_options[j])
            n+=1
            for i in range(3):
                year = random.randint(region_years[j][0], region_years[j][1])
                single_year_rank(["John",region_options[j],year])
            print('\n', end='')

def test_main():
    print("What function test?")
    print("1 - single year input")
    print("2 - two year input")
    print("3 - open_csv")
    print("4 - single year rank")
    print("5 - most uses year")
    print("6 - highest Rank year")
    run_test = key_input(['1','2','3', '4', '5', '6'])

    if run_test == '1':
        single_in_testing()
    if run_test == '2':
        two_in_testing()
    if run_test == '3':
        open_csv_testing()
    if run_test == '4':
        single_year_rank_test()
    if run_test == '5':
        most_uses_year_test()
    if run_test == '6':
        highest_year_rank_test()

test_main()