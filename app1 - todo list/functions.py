# Function to read todos from the file
def get_todos(filepath="files/todos.txt"):
    """Reads todos text file and saves to the list """
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()  # Save File to List
            return todos_local
    except FileNotFoundError:
        print("File or Dir not found")


# Function to write todos to the file
def write_todos(todos_arg, filepath="files/todos.txt"):
    """Writes the list to todos text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # Save List to File with added items
