#!/usr/bin/env python3

import pandas as pd
import sys
import getopt
import csv
import os


def main(argv):
  try:
    (opts, args) = getopt.getopt(argv, "i:", ["input="])  # i = input file name
  except getopt.GetoptError:

    print("2")
    print("Usage: ./alberta.py -i <input file name>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print("3")
      print("Usage: ./alberta.py -i <input file name>")
      sys.exit()
    elif opt in ("-i", "--input"):
      print("working")
      inputFileName = arg  #total

  df = pd.read_csv(inputFileName, delimiter=',')
  print(df.shape)
  print(df.columns)

  titles = list(df.columns)
  titles[0], titles[1], titles[2], titles[3], titles[4] = titles[4], titles[
    3], titles[1], titles[2], titles[0]

  df = pd.DataFrame(df, columns=titles)
  df['Gender'] = df['Gender'].replace(['Boy'], 'M')
  df['Gender'] = df['Gender'].replace(['Girl'], 'F')

  df['First Name'] = df['First Name'].str.upper()

  df = df.rename(columns={"First Name": "Name", "Frequency": "Number", "Ranking by Gender & Year": "Rank"})

  groupedM = df.groupby(df['Gender'])
  dfM = groupedM.get_group('M')
  dfM = pd.DataFrame(dfM)
  dfM = dfM.drop(columns=['Gender'])
  print(dfM)

  groupedF = df.groupby(df['Gender'])
  dfF = groupedF.get_group('F')
  dfF = pd.DataFrame(dfF)
  dfF = dfF.drop(columns=['Gender'])
  print(dfF)

  dfM.to_csv('M_Alberta.csv', index=False)
  dfF.to_csv('F_Alberta.csv', index=False)


#df = df.sort_values(by=['Year', 'Count'])  #print(df)
#df.to_csv('albertaNames.csv', index=False)

if __name__ == "__main__":
  main(sys.argv[1:])
