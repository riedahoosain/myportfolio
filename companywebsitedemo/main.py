# Sample Website of a Company and Personel


import streamlit as st
import pandas

st.set_page_config(
    layout='wide', page_title='Innovative Technology', page_icon='images/icon.png')
st.header('Innovative Technology')

# About Company Data
about_website = '''
Welcome to Innovative Technology, your dedicated partner in navigating the dynamic world of information technology. 
Established with a passion for excellence and a commitment to client success, we take pride in delivering top-notch 
IT support services tailored to meet the unique needs of businesses across South Africa.

'''
st.write(about_website)
st.subheader('Our Team')

# Three Columns to split data instead of having one big row
col1, col2, col3 = st.columns(3)

# Import personnel data from csv file using pandas
df = pandas.read_csv('data.csv', sep=',')


# Display Data over the 3 columns

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
