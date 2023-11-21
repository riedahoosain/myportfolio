# Todo List System

todos = []
print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")


# Accept User input
while True:   
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add'| 'a':
            todo = input("Enter a todo: ")
            todos.append(todo)
            todos.sort()

        case 'edit' | 'e':
            number = int(input("Number of the todo to edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'show' | 's':
            print("List of todos")
            todos.sort()
            for index, item in enumerate(todos):
                print(f"{index + 1}: {item}")
            print(f"Total items to do is: {len(todos)}")

        case 'complete' | 'c':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)            

        case 'exit':
            break


print("Thank for you using the Todo List System")   
