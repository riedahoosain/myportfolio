import streamlit as st
import pandas

st.set_page_config(
    layout='wide', page_title="Rieda's Portfolio", page_icon='images/20.png')


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rieda Hoosain")
    aboutme = '''    
    Hello, my name is Rieda, an experienced Technical Savvy individual with a demonstrated history of working in the information technology and services industry. 
    IT and Software Support Engineer skilled in Hardware,Software and Network Support.
    I also have skills in the Software Development Life Cycle (SDLC), SQL, Customer Service, and Technical Support industry.
    Strong information technology professional graduated from Rylands High
    I was a developer in Visual Basic 6 and SQL7 and have taught myself Python using various Courses
    I do hope this website will help people get an idea of what I know.

    Looking for a company that will give me a chance to master Python software development and grow from there

    '''
    st.info(aboutme)

contactme = '''
Below is some of the apps that I have built while learning Python. Feel Free to contact me if you have any questions
'''
st.write(contactme)


col3, col4 = st.columns(2)
df = pandas.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
