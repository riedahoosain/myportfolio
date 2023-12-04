# Todo List System

# Function to read todos from the file
def get_todos(filepath="files/todos.txt"):
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()  # Save File to List
            return todos_local
    except FileNotFoundError:
        print("File or Dir not found")


# Function to write todos to the file
def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # Save List to File with added items


# This Function adds a todo
def add_to_todo(user_action_local):
    todo = user_action_local[4:] + "\n"

    todos = get_todos()
    todos.append(todo)

    write_todos(todos)

# This function shows list of todos


def show_to_do():
    print("List of todos")

    todos = get_todos()

    # new_todos =[item.strip('\n') for item in todos] #List Comprehension. a For Loop written in one short line

    for index, item in enumerate(todos):
        print(f"{index + 1}: {item}", end="")
    print('\n')
    print(f"Total items to do is: {len(todos)}")


# This function edits an existing todo
def edit_to_do(user_action_local):
    number = int(user_action_local[5:])
    number = number - 1
    todos = get_todos()

    new_todo = input("Enter new todo: ")
    todos[number] = new_todo + '\n'

    write_todos(todos)


# This function completes a todo and removes from the file
def complete_to_do(user_action_local):
    number = int(user_action[9:])
    todos = get_todos()

    index = (number - 1)
    todo_to_remove = todos[index].strip('\n')

    todos.pop(index)  # Remove item from the todos list

    write_todos(todos)

    print(f"Todo {todo_to_remove} was removed from the list")


print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")

# Accept User input
while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    # Add a new Todo
    if user_action.startswith("add"):
        add_to_todo(user_action)

    # Show list of To Dos
    elif user_action.startswith("show"):
        show_to_do()

    # Edit a To Do
    elif user_action.startswith("edit"):
        try:
            edit_to_do(user_action)

        except ValueError:
            print("Your command is not valid")
            print("Please make sure that you have entered a number")
            continue

        except IndexError:
            print("Your command is not valid")
            print("There is no item with that number.")
            continue

    # Removes the Todo from the file since it has been completed
    elif user_action.startswith("complete"):
        try:

            complete_to_do(user_action)

        except IndexError:
            print("Your command is not valid")
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Your command is not valid")
            print("Please enter an integer number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have not entered a valid command")


print("Thank for you using the Todo List System")
