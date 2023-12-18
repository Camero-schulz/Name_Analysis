#!/usr/bin/env python3
#Idk why I did the list stuff, I think I started with it but its a bit late now to change everything, I don't want to risk breaking everything
#Functions:
#key_input: takes in a list of allowed characters then returns the chacter pressed by user
#region_input: takes user input and returns a list of region data - ["region name",[first year, last year]] 
#single_year_input: takes a region data list. gets user input in the form of a year and returns it
#two_year_input: takes a region data list. gets user input of two years separated by a space and returns them as a list
#open_csv: takes region data list. opens the csv files of the input region and returns a list of 4 items

errorCheck = 0
try:
    import tty
    import sys
    import termios
    import csv
    import os
except:
    print("tty, sys, termios, csv, and os are required to run SNInputFunctions")
    errorCheck = 1 #used to not stop full program only these functions


def key_input(in_options):
    if errorCheck != 1:
        try:
            original_settings = termios.tcgetattr(sys.stdin)
            error_response = 0
            tty.setcbreak(sys.stdin) #makes it so that the terminal takes in a single input at a time and doesn't echo it
            error_response = 1
            while True:
                key = sys.stdin.read(1)  #reads a single keypress
                if key in in_options:
                    print(key)

                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)

                    return key
        except:
            if (error_response == 1): #only runs if the code this is reversing runs
                try:
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)
                except:
                    print("Error: could not access libraries required for key_input")
            return -1


def region_input(): 
    if errorCheck != 1:
        region_options = ["Alberta","BC","Quebec","NewBrunswick","NovaScotia","USA"]
        region_years = [[1980,2020],[1923,2021],[1980,2020],[1980,2018],[1920,2022],[1923,2021]]

        print("\nWhat area would you like to consider?")
        for i in range(1,len(region_options)+1):
            print(str(i)+') '+region_options[i-1])

        print("press number key to select")
        try:
            region_num = int(key_input(['1','2','3','4','5','6']))
            if region_num == -1:
                raise Exception
        except:
            print("Error: could not get user input")
            return None
        return [region_options[region_num-1],region_years[region_num-1]]
    else:
        return None


def single_year_input(region_data):
    if (errorCheck != 1 and len(region_data) == 2):
        while True: #gets years
            print("\nEnter a year (between",str(region_data[1][0]),"and",str(region_data[1][1])+"): ", end='')
            year = input().strip()
            try:
                if(len(year)!=4): #checks input is proper length
                    print("Invalid year")
                    raise Exception
                    
                #checks that input is an integer and in range
                year = int(year) 
                if (region_data[1][0] > year or region_data[1][1] < year):
                    print("A year is out of range")
                    raise Exception
                break
            except:
                pass

        return year
    else:
        return None


def two_year_input(region_data):
    if errorCheck != 1 and len(region_data) == 2:
        while True: #gets years
            print("\nEnter two years separated by a space (between",str(region_data[1][0]),"and",str(region_data[1][1])+") or -1 for all time: ", end='')
            try:
                years = input().strip()

                try:
                    #checks if input was all time
                    years = int(years)
                    if years == -1:
                        years = region_data[1]
                        break
                    else:
                        raise Exception
                except:
                    #otherwise checks if the two inputs are valid years
                    years = years.split()
                    if(len(years)!=2):
                        raise Exception
                    if(len(years[0]) != 4 or len(years[1]) != 4):
                        raise Exception
                    
                    for i in range(2):
                        
                        years[i] = int(years[i])
                        if (region_data[1][0] > years[i] or region_data[1][1] < years[i]):
                            print("A year is out of range")
                            raise Exception
                    break
            except:
                print("invalid years")
                pass

        return years
    else:
        return None


def open_csv(region_data):
    #region_data = regionName
    #ensures that the current directory is valid and gets to correct location
    if errorCheck != 1:
        direct = os.getcwd()
        dir_prefix = ''

        if (direct[-18:] == 'teamprojectcis2250'):
            dir_prefix = ''
        elif (direct[-19:] == 'QuestionSourceFiles'):
            dir_prefix = '../'
        elif (direct[-12:] == 'SpecificName'):
            dir_prefix = '../../'
        else:
            print("Error: invalid running directory")

        try:
            #opens files and makes sure they are valid
            f_file_name = dir_prefix+"CSVFiles/F_"+region_data+".csv"
            m_file_name = dir_prefix+"CSVFiles/M_"+region_data+".csv"
            F_file = open(f_file_name, "r")
            M_file = open(m_file_name, "r")

            if F_file == None or M_file == None:
                raise Exception
            else:
                csv_m = csv.reader(M_file, delimiter = ',')
                next(csv_m)

                #checks to make sure correct formatting
                for row in csv_m:
                    if len(row) != 4:
                        raise Exception
                    row[0] = int(row[0])
                    row[2] = int(row[2])
                    row[3] = int(row[3])
                    break
                csv_f = csv.reader(F_file, delimiter = ',')
                M_file.seek(0)
                next(M_file)

                next(csv_f)
                for row in csv_f:
                    if len(row) != 4:
                        raise Exception
                    row[0] = int(row[0])
                    row[2] = int(row[2])
                    row[3] = int(row[3])
                    break
                F_file.seek(0)
                next(F_file)

                return [csv_m, csv_f,F_file,M_file]

        except:
            print("Error: could not open valid csv data files")
            return None