# Todo List System

def get_todos(filepath):
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()  # Save File to List
            return todos_local
    except FileNotFoundError:
        print("File or Dir not found")


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # Save List to File with added items

def add_to_todo(user_action_local):
        todo = user_action_local[4:] + "\n"

        # todo = input("Enter a todo: ") + "\n"

        todos = get_todos('files/todos.txt')
        todos.append(todo)

        write_todos('files/todos.txt', todos)



print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")

# Accept User input
while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        add_to_todo(user_action)

        ##todo = user_action[4:] + "\n"

        # todo = input("Enter a todo: ") + "\n"

        ##todos = get_todos('files/todos.txt')
        ##todos.append(todo)

        ##write_todos('files/todos.txt', todos)

        # with open('files/todos.txt', 'w') as file:
        # file.writelines(todos)  # Save List to File with added items

    elif user_action.startswith("show"):
        print("List of todos")

        todos = get_todos('files/todos.txt')

        # new_todos =[item.strip('\n') for item in todos] #List Comprehension. a For Loop written in one short line

        for index, item in enumerate(todos):
            print(f"{index + 1}: {item}", end="")
        print('\n')
        print(f"Total items to do is: {len(todos)}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # number = int(input("Number of the todo to edit: "))
            number = number - 1
            todos = get_todos('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)

            # with open('files/todos.txt', 'w') as file:
            # file.writelines(todos)  # Save List to File with added items

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

            # number = int(input("Number of the todo to complete: "))
            number = int(user_action[9:])
            todos = get_todos('files/todos.txt')

            index = (number - 1)
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)  # Remove item from the todos list

            write_todos('files/todos.txt', todos)

            # with open('files/todos.txt', 'w') as file:
            # file.writelines(todos)  # Save List to File with removed items

            print(f"Todo {todo_to_remove} was removed from the list")
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
