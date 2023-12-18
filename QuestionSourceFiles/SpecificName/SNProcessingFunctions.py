#Functions:
#single_year_rank(): Finds the rank of a given name in a given year and region and prints the results. Takes a list [str(name),str(region name),int(year)]
#most_uses_year(): Finds and prints the year that a given name was used the most in a given region. Takes a list [str(name),str(region name),[int(year),int(year)]]
#highest_ranks_year(): Finds and prints the year that a given name was ranked the highest in a given region. Takes a list [str(name),str(region name),[int(year),int(year)]]
#All functions tested using SpecificNameTesting.py

import os
direct = os.getcwd()
errorCheck = 0 #used to not stop full program only these functions

if (direct[-18:] == 'teamprojectcis2250'):
    os.chdir('QuestionSourceFiles')
elif (direct[-12:] == 'SpecificName'):
    os.chdir('..')

try:
    from SpecificName.SNInputFunctions import *
except:
    print("Error: could not import processing functions - SNProcessingFunctions")
    errorCheck = 1


#single_year_rank:
#prints the rank of a name in a given year
#takes a list [str(name),str(region name),int(year)]
def single_year_rank(region_data):
    if errorCheck != 1: #checks that functions were imported properly
        if (oneYearInputCheck(region_data) == -1):
            print("Error: invalid input for highest_rank_year")
        else:
            files = open_csv(region_data[1])
            if files != None:
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

                #prints out values only if the desired data has been found
                if (len(m_placement) == 4):
                    print("In",m_placement[0], region_data[0],"was rank",m_placement[3],"for men with",m_placement[2],"occurences")
                if (len(f_placement) == 4):
                    print("In",f_placement[0], region_data[0],"was rank",f_placement[3],"for women with",f_placement[2],"occurences")
                if (len(f_placement) == 0 and len(m_placement) == 0):
                    print("There is no data for the name",region_data[0],"in",region_data[2])


#most_uses_year:
#prints out the year that the name was used the most times
#takes a list [str(name),str(region name),[int(year),int(year)]]
#returns nothing
def most_uses_year(region_data):
    if errorCheck != 1:
        if (twoYearInputCheck(region_data) == -1):
            print("Error: invalid input for highest_rank_year")
        else:
            region_data[2].sort()

            files = open_csv(region_data[1])
            if (files != None):
                csv_m = files[0]
                csv_f = files[1]

                m_top_year = [0,region_data[0].upper(),0,0] #establishing row in format for comparison
                f_top_year = [0,region_data[0].upper(),0,0]

                for row in csv_m:
                    if(int(row[0]) < region_data[2][0] or int(row[0]) > region_data[2][1]): #checks to see if row is within the interval of years
                        pass
                    else:
                        if(row[1].upper() == region_data[0].upper()): #checks if name matches
                            row[2] = int(row[2].strip())
                            if (row[2] > m_top_year[2]): #compares number of occurences against previous leader
                                m_top_year = row

                for row in csv_f:
                    if(int(row[0]) < region_data[2][0] or int(row[0]) > region_data[2][1]):
                        pass
                    else:
                        if(row[1].upper() == region_data[0].upper()):
                            row[2] = int(row[2].strip())
                            if (row[2] > f_top_year[2]):
                                f_top_year = row
                files[2].close()
                files[3].close()

                #only prints data if name was found in interval
                if m_top_year[0] != 0:
                    print("The most men where named",m_top_year[1].capitalize(),"in",m_top_year[0],"with",m_top_year[2])
                if f_top_year[0] != 0:
                    print("The most women where named",f_top_year[1].capitalize(),"in",f_top_year[0],"with",f_top_year[2])
                if (m_top_year[0] == 0 and f_top_year[0] == 0):
                    print("There is no data for the name",region_data[0],"between",region_data[2][0],"and",region_data[2][1])

#highest_rank_year:
#prints out what year the name was ranked the highest
#takes a list [str(name),str(region name),[int(year),int(year)]]
def highest_rank_year(region_data):
    if errorCheck != 1:
        if (twoYearInputCheck(region_data) == -1):
            print("Error: invalid input for highest_rank_year")
        else:
            region_data[2].sort()

            files = open_csv(region_data[1])
            if files != None:
                csv_m = files[0]
                csv_f = files[1]

                f_highest_ranks = []
                m_highest_ranks = []
                m_top_rank = [0,region_data[0],0,999999999] #arbitrary number that is larger than any files have
                f_top_rank = [0,region_data[0],0,999999999]
                
                for row in csv_m:
                    if(int(row[0]) < region_data[2][0] or int(row[0]) > region_data[2][1]): #checks if row is within year range
                        pass
                    else:
                        row[1] = row[1].strip()
                        if(row[1].upper() == region_data[0].upper()): #checks if row name is same as desired name
                            row[3] = int(row[3].strip())
                            if (row[3] < m_top_rank[3]): #if the current row rank is higher than the current leader
                                m_top_rank = row #sets row as new leader
                                m_highest_ranks = [] #empties list
                                m_highest_ranks.append(row)
                            elif (row[3] == m_top_rank[3]):
                                m_highest_ranks.append(row) #adds row to list if rank is equal to leader
                            
                for row in csv_f:
                    if(int(row[0]) < region_data[2][0] or int(row[0]) > region_data[2][1]):
                        pass
                    else:
                        row[1] = row[1].strip()
                        if(row[1].upper() == region_data[0].upper()):
                            row[3] = int(row[3].strip())
                            if (row[3] < f_top_rank[3]):
                                f_top_rank = row
                                f_highest_ranks = []
                                f_highest_ranks.append(row)
                            elif (row[3] == f_top_rank[3]):
                                f_highest_ranks.append(row)
                files[2].close()
                files[3].close()

                #prints info only if the name was found
                if(len(m_highest_ranks) != 0):
                    print(m_top_rank[1].capitalize(),"was rank",m_top_rank[3],"for men in",len(m_highest_ranks),"year(s):")
                    for i in range(len(m_highest_ranks)): #prints each year that is in the tie
                        if i < (len(m_highest_ranks)-1):
                            print(m_highest_ranks[i][0]+", ", end = '')
                        else:
                            print(m_highest_ranks[i][0])
                if(len(f_highest_ranks) != 0):
                    print(f_top_rank[1].capitalize(),"was rank",f_top_rank[3],"for women in",len(f_highest_ranks),"year(s):")
                    for i in range(len(f_highest_ranks)):
                        if i < (len(f_highest_ranks)-1):
                            print(f_highest_ranks[i][0]+", ", end = '')
                        else:
                            print(f_highest_ranks[i][0])
                if (len(m_highest_ranks) == 0 and len(f_highest_ranks) == 0):
                    print("There is no data for the name",region_data[0],"between",region_data[2][0],"and",region_data[2][1])


def twoYearInputCheck(region_data):
    if (len(region_data) != 3):
        return -1
    if (len(region_data[0]) == 0):
        return -1
    if (len(region_data[1]) == 0):
        return -1
    if (len(region_data[2]) != 2):
        return -1
    if (len(str(region_data[2][0]))!=4):
        return -1
    if (len(str(region_data[2][1]))!=4):
        return -1
    try:
        dummy1 = int(region_data[2][0])
        dummy2 = int(region_data[2][1])
    except:
        return -1

    return 0

def oneYearInputCheck(region_data):
    if (len(region_data) != 3):
        return -1
    if (len(region_data[0]) == 0):
        return -1
    if (len(region_data[1]) == 0):
        return -1
    if (len(str(region_data[2])) != 4):
        return -1
    try:
        dummy = int(region_data[2])
    except:
        return -1
    
    return 0