todos = []
print("Welcome to the Todo List system")
print("You can add or show a todo or exit program")


# Accept User input
while True:   
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Thank for you using the Todo List System")   
