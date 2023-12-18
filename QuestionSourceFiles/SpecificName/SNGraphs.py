#!/usr/bin/env python3
#functions:
#plot_graph: takes in 4 parameters for data then graphs it
#rank_over_time: takes a string (name) processes rank data then calls plot_graph
#uses_over_time: takes a string (name) processes uses data then calls plot_graph

import os
direct = os.getcwd()
errorCheck = 0 #used to not stop full program only these functions

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')

try:
    import matplotlib.pyplot as plt
    from SpecificName.SNInputFunctions import *
except:
    print("Error: could not import processing functions - SNGraphs")
    errorCheck = 1


def plot_graph(name, years, data, n): #plots data from other functions
    try:
        plt.plot(years,data)
        plt.xlabel("Year")

        #changes the labels depending on data its displaying
        if n == 'o':
            plt.ylabel("Number of uses")
            title = "Popularity of "+name+" over time"

        if n == 'r':
            plt.ylabel("Rank")
            title = "Rank of "+name+" over time"
            plt.gca().invert_yaxis()
    
        #plots displays the graph
        plt.title(title)
        plt.show()
    except:
        print("Error: Unable to graph data")


def rank_over_time(name): #gathers data for rank graph
    if errorCheck != 1:

        try:
            region = region_input()
            print("\nDo you want to see that name in male or female files?")
            print("1) Male")
            print("2) Female")
            gender = key_input(['1','2'])

            csv_files = open_csv(region[0])
            if csv_files != None:
                #uses file for selected gender
                if (gender == "1"):
                    csv_file = csv_files[0]
                elif (gender == '2'):
                    csv_file = csv_files[1]

                years = []
                rank = []

                #adds every datapoint to the lists
                for row in csv_file:
                    if row[1].upper() == name.upper():
                        years.append(int(row[0]))
                        rank.append(int(row[3]))
                csv_files[2].close()
                csv_files[3].close()

                if (len(years) != 0 and len(rank) != 0):
                    plot_graph(name, years, rank, "r")
                else:
                    print("Not enough data to graph that name")
        except:
            print("Error: Data for graph could not be gathered")


def uses_over_time(name): #gathers data for num uses graph
    try:
        region = region_input()
        print("\nDo you want to see that name in male or female files?")
        print("1) Male")
        print("2) Female")
        gender = key_input(['1','2'])

        csv_files = open_csv(region[0])
        #uses file for selected gender
        if csv_files != None:
            if (gender == "1"):
                csv_file = csv_files[0]
            elif (gender == '2'):
                csv_file = csv_files[1]

            years = []
            occurance = []

            #adds datapoints to lists for graphing
            for row in csv_file:
                if row[1].upper() == name.upper():
                    years.append(int(row[0]))
                    occurance.append(int(row[2]))
            csv_files[2].close()
            csv_files[3].close()

            if (len(years) != 0 and len(occurance) != 0):
                plot_graph(name, years, occurance, "o")
            else:
                print("Not enough data to graph that name")
    except:
        print("Error: Data for graph could not be gathered")
