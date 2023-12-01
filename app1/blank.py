#This is just a temp space I will add or test things before adding to my programs
#This is also use to scribble temp info and code
'''
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Total Value cannot be zero")
'''

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")
     
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list" )
