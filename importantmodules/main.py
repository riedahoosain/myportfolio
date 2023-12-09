import glob
import csv

# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.
def globfunction():    
    myfiles = glob.glob("files/*.txt") #show all files with txt extension

    print(myfiles) #list of files in path

    #Access each file in the list and print contents in text format
    for filepath in myfiles:
        #print(filepath)
        with open(filepath, 'r') as file:
            print(file.read())

def csvfunction():
#Access and load CSV files
    with open("files/weather.csv", 'r') as file:
        data = list(csv.reader(file))

    print(data)
    city = input("Enter a city: ")
    for row in data:
        if row[0] == city:
            print(f"The temperature for {row[0]} is: {row[1]} ")


choice = input(''' 
Enter a Function to Run
1. CSV
2. Glob
''')

if choice == "1":
    csvfunction()
elif choice == "2":
    globfunction()