# GUI interface for To-Do App
# This app allows users to add edit and complete a To-Do list
# This app can also be used for a shopping list or anything that requires a list
# the file todos.txt needs to exist where the app is or the program will create a new blank file

import functions
import PySimpleGUI as sg
import time
import os

def create_gui():
    '''
    This creates the GUI Interface
    '''
    sg.theme("Black")

    clock = sg.Text("", key="clock")
    label = sg.Text("Type in todo")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button("Add", mouseover_colors="red",tooltip="Add a ToDo")    
    edit_button = sg.Button("Edit",mouseover_colors="red", tooltip="Edit a ToDo")
    complete_button = sg.Button("Complete",mouseover_colors="red",tooltip="Complete/Remove ToDo")
    exit_button = sg.Button("Exit",mouseover_colors="red", tooltip="Exit the program")
    list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
    info_text = sg.Text("ℹ️", key="information")

    menu_layout = [[clock],
                   [label],
                   [input_box],
                   [list_box,],
                   [info_text],
                   [add_button, edit_button, complete_button, exit_button]]
    # Stores the GUI Layout in a list which is then used when loading GUI

    window = sg.Window('My To-Do App', layout=menu_layout, font=('Helvetica', 20))
    return window

def add_to_todo():
    '''
    Adds a todo to the list
    '''
    try:
        todos = functions.get_todos()       
        new_todo = values['todo'].strip()
        new_todo = new_todo + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")

    except AttributeError:
        print("The was an error and the Todo was not added")
        print("This can happen if the file that writes the todo is not found")


def edit_to_do():
    try:
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + '\n'
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")

    except IndexError:
        window['information'].update(
            value="Please select an item first before you Edit")
        sg.popup("Please select an item first before you Edit",
                 font=('Helvetica', 20))


def complete_to_do():
    try:
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")
    except IndexError:
        window['information'].update(
            value="Please select an item first before you click Complete")
        sg.popup("Please select an item first before you click Complete",
                 font=('Helvetica', 20))


#MAIN PROGRAM

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

window = create_gui()
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  

    match event:
        case "Add":
            if values['todo'].strip() == "":
                window['information'].update(value="Please enter a todo before adding")
                sg.popup("Please enter a todo before adding", font=('Helvetica', 20))
            else:
                add_to_todo()

        case "Edit":
            edit_to_do()

        case "Complete":
            complete_to_do()

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Exit" | sg.WIN_CLOSED:
            break       

window.close()