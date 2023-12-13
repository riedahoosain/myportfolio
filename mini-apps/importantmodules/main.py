import glob
import csv
import shutil
import webbrowser

def globfunction():
    ''' 
    The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, 
    although results are returned in arbitrary order. 
    
    '''
    myfiles = glob.glob("files/*.txt")  # show all files with txt extension

    print(myfiles)  # list of files in path

    # Access each file in the list and print contents in text format
    for filepath in myfiles:
        # print(filepath)
        with open(filepath, 'r') as file:
            print(file.read())


def csvfunction():
    ''' Access and load CSV files '''
    with open("files/weather.csv", 'r') as file:
        data = list(csv.reader(file))

    print(data)
    city = input("Enter a city: ")
    for row in data[1:]:
        if row[0] == city:
            print(f"The temperature for {row[0]} is: {row[1]} ")      

def shutilfunction():
    ''' Zips files in a directory'''
    shutil.make_archive("output", "zip", "files")


def webbrowserfunction():
    ''' Loads a URL in this case we using it to load google using default browser and search for something'''
    user_term = input("Enter a Search Term: ").replace(" ", "+")
    webbrowser.open(f"https://www.google.com/search?q={user_term}")



choice = input(''' 
Enter a Function to Run
1. csv
2. glob
3. shutil
4. webbrowser               
''')

if choice == "1":
    csvfunction()
elif choice == "2":
    globfunction()
elif choice == "3":
    shutilfunction()
else:
    webbrowserfunction()


