# GUI interface for To-Do App

import functions
import PySimpleGUI as sg

def add_to_todo():
        try:
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except AttributeError:
            print("The was an error and the Todo was not added")
            print("This can happen if the file that writes the todo is not found")


def create_gui():
    '''
    This creates the GUI Interface
    '''

    label = sg.Text("Type in todo")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button("Add")
    exit_button = sg.Button("Exit")
    list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                          enable_events=True, size=[45,10])
    edit_button = sg.Button("Edit")


    window = sg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button],[list_box, edit_button],[exit_button]],
                    font=('Helvetica', 20))
    return window
window = create_gui()
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            add_to_todo()
            '''
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
            except AttributeError:
                print("The was an error and the Todo was not added")
                print("This can happen if the file that writes the todo is not found")
            '''
        case sg.WIN_CLOSED:
            break

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break
         
window.close()
print("Good Bye?")
