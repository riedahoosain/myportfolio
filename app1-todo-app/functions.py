# Current Path where todos.txt file is being stored
FILEPATH = 'todos.txt'

# Function to read todos from the file
def get_todos(filepath=FILEPATH):
    """Reads todos text file and saves to the list """
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()  # Save File to List
            return todos_local
    except FileNotFoundError:
        print("File or Dir not found")
  


# Function to write todos to the file
def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the list to todos text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # Save List to File with added items

if __name__ == "__main__":
    print("This is from the function module")
