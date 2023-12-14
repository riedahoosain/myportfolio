import streamlit as st
from send_email import send_email
import pandas

st.set_page_config(layout='wide', page_title='Contact Us',
                   page_icon='images/message.png')

df = pandas.read_csv('topics.csv')

st.header('Contact Us:')
with st.form(key="email_forms"):

    # Create a select box with options from csv

    #df = pandas.read_csv('topics.csv')
    #topic_list = []
    #for index, row in df.iterrows():
     #   topic_list.append(row['topic'])

    user_email = st.text_input("Your Email Address")    
    selected_option = st.selectbox("What Topic do you want to discuss", df["topic"])
    user_message = st.text_area('Message', key='user_message')
    submit_button = st.form_submit_button("Submit")
    submit_button = False

    message = f"""\
Subject: Message from {user_email}

From: {user_email}
Topic: {selected_option}
{user_message}

Sent from My Python Portfolio Website
"""

    if st.form_submit_button:
        if user_email.strip() != "":
            if user_message.strip() != "":
                if selected_option.strip() != "":
                    send_email(message)
                    st.info("Your Email was sent successfully")

                else:
                    print("")
                    st.info("Please make sure you entered an email address and content in the text area")