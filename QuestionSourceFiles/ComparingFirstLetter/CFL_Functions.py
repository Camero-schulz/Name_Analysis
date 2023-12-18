import csv
import pandas as pd


# FOR FILE / GENDER INPUT
def determineFile(genderInput, fileOptions, fileInput):

  names = []     # list of all male or female names 

  # Male names
  if (genderInput == '1' or genderInput == '3'):
    gender = "male"
    try:
      inputFileName = ("../CSVFiles/M_"+fileOptions[fileInput]+".csv") # opens male file of region
    except FileNotFoundError:
      print("ERROR: File not found")
      sys.exit()


  # Female names
  elif (genderInput == '2'):
    gender = "female"
    try:
      inputFileName = ("../CSVFiles/F_"+fileOptions[fileInput]+".csv") # opens female file of region
    except FileNotFoundError:
      print("ERROR: File not found")
      sys.exit()


  else:
    print("ERROR: File(s) not found")
    sys.exit()


  return (names, gender, inputFileName)


# TO DETERMINE THE COMPLETE RANGE OF YEARS
def rangeOfYears(inputFileName):
  f = open(inputFileName,'rb')
  
  next(f)
  begYear = f.read(4)     # reads begining year

  f.seek(-50, 2)          # seeks to end of file
  endYear = f.readline()  # reads line so the next line begins with the year
  endYear = f.read(4)     # reads end year

  f.close()

  return int(begYear), int(endYear)


# FOR YEAR INPUT
def timeFrame(yearInput, begYear, endYear):
  
  years = []
  ERROR_Message = "Please enter a year between {0} and {1}\n".format(begYear, endYear)

  # 1. Over a single year
  if yearInput == '1':
    while True:

      try: 

        userInput = eval(input("Enter a year: "))
        if (userInput >= begYear and userInput <= endYear):
          years.append(userInput)
          break
        else:
          print(ERROR_Message) 

      except NameError:
        print(ERROR_Message)


  # 2. Over a period of years
  elif yearInput == '2':
    while True:

      try:

        userInput = eval(input("Input a year and hit <ENTER> (Input 0 to terminate loop): "))
        if userInput == 0:
          break
        elif (userInput >= begYear and userInput <= endYear):
          years.append(userInput)
        else:
          print(ERROR_Message) 

      except NameError:
        print(ERROR_Message)


  # 3. Every single year
  elif yearInput == '3':
    for i in range (begYear, endYear+1):
      years.append(i)


  else:
    print("ERROR: Please enter the correct number: ")

  return years


# FOR EFFICIENCY INPUT
def efficiency (entryInput):

  if entryInput == '2':
    ignore = 1
  elif entryInput == '3':
    ignore = 2
  elif entryInput == '4':
    ignore = 5
  elif entryInput == '5':
    ignore = 10
  else: 
    ignore = 0

  return ignore


# Function finds all of the names that starts with the letter entered by the user 
def openCSVFileName(inputFileName, names, year, userInput, totalNames, ignore):

  # Reads CSV file
  with open(inputFileName) as csvDataFile:

    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter=',')

    # Goes through each row of the file and appends each corresponding name to names
    for row in csvReader:

      if (int(row[0]) == year):
        if row[1][0] == userInput:
          totalNames.append(row[1])
          if int(row[2]) > ignore: 
            names.append(row[1])

  totalNames = set(totalNames)  # Removes duplicate names
  totalNames = list(totalNames)

  names = set(names)            # Removes duplicate names
  names = list(names)
  return names, totalNames


def openCSVFileTotal(inputFileName, total, years, name):

  addTotal = []

  # Reads file as df and locates every matching name
  df = pd.read_csv(inputFileName, delimiter=',')
  df = df.loc[df['Name'] == name]

  # locates matching years
  for i in range (len(years)):
    dfY = df.loc[df['Year'] == years[i]]
    addTotal.append(dfY['Number'].sum()) # list of all total values for a name 

  # sums all total values and appends result to total
  total.append(sum(addTotal)) 

  return total