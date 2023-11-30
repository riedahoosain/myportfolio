# Todo List System     

print("Welcome to the Todo List system")
print("You can add, edit, complete, show a todo or exit program")


# Accept User input
while True:   
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()
    
    
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"        
    
        #todo = input("Enter a todo: ") + "\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines() #Save File to List       


        todos.append(todo)
        
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos) #Save List to File with added items
    
    
    elif user_action.startswith("show"):
        print("List of todos")        
        
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        #new_todos =[item.strip('\n') for item in todos] #List Comprehension. a For Loop written in one short line            

        for index, item in enumerate(todos):
            print(f"{index + 1}: {item}", end="")
        print('\n')        
        print(f"Total items to do is: {len(todos)}")        

    
    elif user_action.startswith("edit"):    
        number = int(user_action[5:])
        #number = int(input("Number of the todo to edit: "))
        number = number - 1        
      
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines() #Save File to List     

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        
        with open('files/todos.txt', 'w') as file:
                file.writelines(todos) #Save List to File with added items
                

    
    elif user_action.startswith("complete"): #Removes the Todo from the file since it has been completed

        #number = int(input("Number of the todo to complete: "))
        number = int(user_action[9:])

        
        with open('files/todos.txt', 'r') as file:
                todos = file.readlines() #Save File to List  
        
        index = (number - 1)
        todo_to_remove = todos[index].strip('\n')        

        todos.pop(index) #Remove item from the todos list

        with open('files/todos.txt', 'w') as file:
             file.writelines(todos) #Save List to File with removed items
        
        print(f"Todo {todo_to_remove} was removed from the list")


    
    elif user_action.startswith("exit"):
        break

    else:
         print("You have not entered a valid command")
        


print("Thank for you using the Todo List System")   
