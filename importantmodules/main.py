# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
import glob
import csv
myfiles = glob.glob("files/*.txt") #show all files with txt extension

print(myfiles) #list of files in path

#Access each file in the list and print contents in text format
for filepath in myfiles:
    #print(filepath)
    with open(filepath, 'r') as file:
        print(file.read())

#Access and load CSV files
with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")