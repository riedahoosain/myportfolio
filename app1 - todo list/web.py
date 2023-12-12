# Web interface for To-Do App
# This app allows users to add and complete a To-Do list
# This app can also be used for a shopping list or anything that requires a list
# the file in FILEPATH needs to exist where the app is or the program will create a new blank file

import streamlit as st
import functions  # All functions sits in this module # get_todos and write_todos sits here
import time
import os


st.set_page_config(page_title="My ToDo App", page_icon="icon.png")
st.title("My Todo App")
st.subheader("This app is used to create a todo or any list for that matter")
st.subheader("List of todos")

# Checks if the todo file exists which is stored in constant variable FILEPATH
# Creates a new file it does not exist
if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, 'w') as file:
        pass

todos = functions.get_todos()
for item in todos:
    st.checkbox(item)
st.write('\n')
if len(todos) == 0:
    st.write("List is empty")
else:
    st.write(f"Total items to do is: {len(todos)}")

st.text_input(label="Add todo", placeholder="Add a new to do", label_visibility="hidden")
