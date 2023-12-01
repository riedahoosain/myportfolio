# This app reads numbers from a text file and calculates the average
# Needs a file called data.txt in a files/ directory

def get_average():
    try:
        with open("files/data.txt", "r") as file:
            data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        average_local = sum(values) / len(values)
        return average_local
    except FileNotFoundError:
        print("File or Dir not found")


average = get_average()
print(average)
