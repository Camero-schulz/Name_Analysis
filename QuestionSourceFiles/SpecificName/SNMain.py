#!/usr/bin/env python3
import os
direct = os.getcwd()
errorCheck = 0 #used to not stop full program only these functions

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')

try:
    from SpecificName.SNInputFunctions import *
    from SpecificName.SNProcessingFunctions import *
    from SpecificName.SNGraphs import *
except:
    print("Error: could not import processing functions - SNMain")
    errorCheck = 1 


def specific_main():
    if (errorCheck != 1):
        name = ''
        i = 0
        #gets name input, will take any non-blank non-empty string
        while (len(name) == 0 and i<20):
            if i==19:
                print("\nWarning: entering another invalid name with exit the function", end = '')
            name = input("\nEnter the name you want to use: ").strip()
            if (len(name) == 0 and i!=19):
                print("Cannot leave name blank")
            i+=1 #end potential infinite loops
        if len(name) != 0:

            print("\nHow would you like to use that name?")
            print("1) Find how the name ranked in a given year")
            print("2) Find what year the name ranked the highest")
            print("3) View of a graph of the names rank over time")
            print("4) Find what year the most people were given that name")
            print("5) View of a graph of the number of uses of that name over time")
            print("0) Go back")
            print("press number key to select")
            try:
                function_choice = key_input(['0','1','2','3','4','5'])
            except:
                print("Error: could not get user input")

            if (function_choice == '1'): #rank single year
                try:
                    region_data = region_input()
                    if (region_data != None):
                        single_input = single_year_input(region_data)
                        if single_input != None:
                            single_year_rank([name,region_data[0], single_input])
                        else:
                            raise Exception
                    else:
                        raise Exception
                except:
                    print("Error: Could not run single_year_rank")


            elif (function_choice == '2'): #highest ranking year
                try:
                    region_data = region_input()
                    if (region_data != None):
                        interval_input = two_year_input(region_data)
                        if interval_input != None:
                            highest_rank_year([name, region_data[0], interval_input])
                        else:
                            raise Exception
                    else:
                        raise Exception
                except:
                    print("Error: Could not run highest_rank_year")


            elif (function_choice == '3'): #graph of rank over time
                try:
                    rank_over_time(name)
                except:
                    print("Error: could not run rank_over_time")


            elif(function_choice == '4'): #highest number of uses
                try:
                    region_data = region_input()
                    if (region_data != None):
                        interval_input = two_year_input(region_data)
                        if interval_input != None:
                            most_uses_year([name, region_data[0], interval_input])
                        else:
                            raise Exception
                    else:
                        raise Exception
                except:
                    print("Error: Could not run most_uses_year")


            elif(function_choice == '5'): #graph of number of uses
                try:
                    uses_over_time(name)
                except:
                    print("Error: Could not run uses_over_time")
            
            elif(function_choice == '0'):
                return None