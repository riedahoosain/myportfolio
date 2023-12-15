# Connects to NASA and loads Astronomy Image of the Day
# Images changes daily

import streamlit as st
import requests
api_key = "IeWIqeNilaDEDxOCAg09sco7zCcIGhHHLSjS8Cpu"
url = "https://api.nasa.gov/planetary/apod?api_key=IeWIqeNilaDEDxOCAg09sco7zCcIGhHHLSjS8Cpu"


# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
title = content["title"]
image_url = content["url"]
image_explanation = content["explanation"]

#Create Webpage and load title, url and explanation of Astronomy Image of the Day
st.set_page_config(page_title='Astronomy Image of the Day')
st.header(title)
st.image(image_url)
st.write(image_explanation)

