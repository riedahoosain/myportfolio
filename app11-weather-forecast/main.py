# A data web app that visualizes the weather forecast for the next five days of any city.
# Uses the Weather API on https://openweathermap.org/api
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(
    layout='centered', page_title="Weather Forecast", page_icon="16.png")

# Add title, text input, slider, selectbox and subheader
st.header("Weather Forecast for the next days")
place = st.text_input("Place")
days = st.slider("Forcast Days", min_value=1, max_value=5,help="Select the number of days of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:

    # Get the Temperature or Sky Data
    try:
        filtered_data = get_data(place, days)

    
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]            
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)    


        if option == "Sky":
            images = {"Clear": "images/clear.png","Clouds": "images/cloud.png","Rain": "images/rain.png","Snow": "images/snow.png",}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]       

            st.image(images_path, width=115)
    except KeyError:
        st.info(f"{place} does not exist. Please make sure the place entered is spelt correctly")