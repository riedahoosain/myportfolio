import streamlit as st

st.set_page_config(layout='wide', page_title='Contact Us', page_icon='images/message.png')

st.header('Contact Us:')
with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area('Message')
    submit_button = st.form_submit_button("Submit")
    if st.form_submit_button:
        print(f"Your email is {user_email} and you wrote {user_message}")