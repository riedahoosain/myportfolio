# A data web app that visualizes the weather forecast for the next five days of any city.
import streamlit as st
import pandas as pd

st.set_page_config(
    layout='centered', page_title="Weather Forecast", page_icon="16.png")
st.header("Weather Forecast for the next days")
place = st.text_input("Place")
days = st.slider("Forcast Days", min_value=1, max_value=5,help="Select the number of days of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

