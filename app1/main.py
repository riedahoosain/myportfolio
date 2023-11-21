# Todo List System

todos = []
print("Welcome to the Todo List system")
print("You can add, edit, show a todo or exit program")


# Accept User input
while True:   
    user_action = input("Type add, edit, show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'show':
            for index, item in enumerate(todos):
                print(f"{index}: {item}")

        case 'exit':
            break


print("Thank for you using the Todo List System")   
