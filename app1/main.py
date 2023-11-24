# Todo List System

print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")


# Accept User input
while True:   
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()



    match user_action:
        
        case 'add'| 'a':
            todo = input("Enter a todo: ") + "\n"
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines() #Save File to List
           


            todos.append(todo)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos) #Save List to File with added items
            

        case 'edit' | 'e':
            number = int(input("Number of the todo to edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'show' | 's':
            print("List of todos")
            
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            #new_todos =[item.strip('\n') for item in todos] #List Comprehension. a For Loop written in one short line            

            for index, item in enumerate(todos):
                print(f"{index + 1}: {item}", end="")
            print('\n')        
            print(f"Total items to do is: {len(todos)}")

        case 'complete' | 'c':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)            

        case 'exit':
            break


print("Thank for you using the Todo List System")   
