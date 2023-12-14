import streamlit as st
from send_email import send_email

st.set_page_config(layout='wide', page_title='Contact Us',
                   page_icon='images/message.png')

st.header('Contact Us:')
with st.form(key="email_forms"):

    user_email = st.text_input("Your Email Address")
    user_message = st.text_area('Message', key='user_message')
    submit_button = st.form_submit_button("Submit")
    submit_button = False

    message = f"""\
Subject: Message from {user_email}

From: {user_email}
{user_message}

Sent from My Python Portfolio Website
"""


# Check if user entered data and then sends email
    if st.form_submit_button:
        if user_email.strip() != "":
            if user_message.strip() != "":
                send_email(message)
                st.info("Your Email was sent successfully")
                submit_button = False
            else:
                st.info(
                    "Please make sure you entered an email address and content in the text area")