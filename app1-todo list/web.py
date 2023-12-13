# Web interface for To-Do App
# Uses streamlit for a web app
# This app allows users to add and complete a To-Do list
# This app can also be used for a shopping list or anything that requires a list
# the file in FILEPATH needs to exist where the app is or the program will create a new blank file

import streamlit as st
import functions  # All functions sits in this module # get_todos and write_todos sits here
import os  

todos = functions.get_todos()

def add_to_do():
     
    todo = st.session_state['new_todo']   
    todo = todo + "\n"    
    todos.append(todo)
    functions.write_todos(todos)
    
   

# MAIN PROGRAM STARTS HERE:

# Checks if the todo file exists which is stored in constant variable FILEPATH
# Creates a new file it does not exist
if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, 'w') as file:
        pass

st.set_page_config(page_title="My ToDo App", page_icon="icon.png")
st.title("My Todo App")
st.subheader("This app is used to create a todo or any list for that matter")
st.subheader("List of todos")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()


st.text_input(label="Add todo", placeholder="Add new to do...",label_visibility="hidden",
              on_change=add_to_do, key='new_todo')