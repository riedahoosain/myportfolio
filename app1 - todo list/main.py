# Todo List System
# This App alows a user to create a list of Todos that is written or read from a text file
# Users can also edit or complete todos

# from functions import get_todos, write_todos

# All functions sits in this module
# get_todos and write_todos sits here
import functions
import time

# This Function adds a todo
def add_to_todo(user_action_local):
    todo = user_action_local[4:] + "\n"
    todos = functions.get_todos()
    todos.append(todo)
    functions.write_todos(todos)

# This Function shows the todos


def show_to_do():

    print("List of todos")
    todos = functions.get_todos()    
    for index, item in enumerate(todos):
        print(f"{index + 1}: {item}", end="")
    print('\n')
    print(f"Total items to do is: {len(todos)}")
 


# This function edits an existing todo
def edit_to_do(user_action_local):
    number = int(user_action_local[5:])
    number = number - 1
    todos = functions.get_todos()
    new_todo = input("Enter new todo: ")
    todos[number] = new_todo + '\n'
    functions.write_todos(todos)


# This function completes a todo and removes from the file
def complete_to_do(user_action_local):
    number = int(user_action[9:])
    todos = functions.get_todos()
    index = (number - 1)
    todo_to_remove = todos[index].strip('\n')
    todos.pop(index)  # Remove item from the todos list
    functions.write_todos(todos)
    print(f"Todo {todo_to_remove} was removed from the list")


print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")
now = time.strftime("%d %B %Y, %H:%M:%S")
print(f'Today is {now}')
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