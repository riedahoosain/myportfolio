# GUI interface for To-Do App

import functions
import PySimpleGUI as sg

def add_to_todo():
        try:
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
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
    window = sg.Window('My To-Do App',
                    layout=[[label, input_box, add_button],[exit_button]],
                    font=('Helvetica', 20))
    return window
window = create_gui()
while True:
    event, values = window.read()
    #print(event)
    #print(values)
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
        case "Exit":
            break
         
window.close()
print("Good Bye?")
