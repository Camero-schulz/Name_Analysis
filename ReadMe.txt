Required Libraries:
os
tty
sys
csv
termios
matplotlib
Tkinter
pandas

===============================

Running Main Program:
Open a linux shell in the teamprojectcis2250 directory

to run the main enter the directory: “cd QuestionSourceFiles/ ”
then use the command “./main.py”

===============================

Running CSV conversion scripts:
open a linux shell in the teamprojectcis2250 directory
change directory to the ConversionSourceFiles directory using the command “cd ConversionSourceFiles”

Running alberta.py: “./alberta.py  -i ../DataFiles/ALBERTADATA/baby-names-frequency_1980_2020.csv”

Running jemQuebec.py: 
Male Names: “./jemQuebec.py -i ../DataFiles/QUEBECDATA/gars1980-2021.csv -o ../CSVFiles/M_Quebec”
Female Names: “./jemQuebec.py -i ../DataFiles/QUEBECDATA/filles1980-2021.csv -o ../CSVFiles/F_Quebec”

Running jemNovaScotia.py: “./jemNovaScotia.py -i ../DataFiles/NSDATA/NS_Top_Twenty_Baby_Names_-_1920-Current.csv -o NovaScotia” 

Running jemNewBrunswick.py: “./jemNewBrunswick.py -i ../DataFiles/NBDATA/NB_Top_20_Popular_Baby_Names_1980-2018___Les_20_noms_de_b_b__populaire_au_N.-B._1980-2018.csv -o NewBrunswick” 

running usa_format: “./usa_format.py”

Running BCDataToStandard:  “./BCDataToStandard.py” 

===============================

Running Test Files:
Open a linux shell in the teamprojectcis2250 directory

to run the SpecificName scaffolding file use the command “./QuestionSourceFiles/SpecificNameTesting.py”

to run the MostFrequent testing file use the command “./QuestionSourceFiles/MostFrequentTest.py”

===============================
Harvard Data set Used for calculating the Ethnicity Probability:
Found at:
Rosenman, Evan; Olivella, Santiago; Imai, Kosuke, 2022, "Race and ethnicity data for first, middle, and last names", https://doi.org/10.7910/DVN/SGKW0K, Harvard Dataverse, V8, UNF:6:W8XaEuBXAsOBsODFZ2TF8Q== [fileUNF]

DataSet used:
first_nameRaceProbs.tab 
Was Downloaded as a csv