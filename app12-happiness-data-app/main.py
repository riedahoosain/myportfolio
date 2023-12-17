# A data web app that plots data and shows the comparison
import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Happiness Data App")

# Selected Options in a Tuple
tuple_x = ("Country", "Happiness", "GDP", "Social Support", "Life Expectancy",
           "Freedom to make life choices", "Generosity", "Corruption")
tuple_y = ("Country", "Happiness", "GDP", "Social Support", "Life Expectancy",
           "Freedom to make life choices", "Generosity", "Corruption")

# Load Website
st.header("In Search for Happiness")
data_x = st.selectbox("Select the data for the X-axis",
                      (tuple_x))
data_y = st.selectbox("Select the data for the Y-axis",
                      (tuple_y))

# Load CSV data from file
df = pd.read_csv("happy.csv")

st.subheader(f"{data_x} and {data_y}")

# Get Data based on the options user chooses and returns the value


def get_data(data_x, data_y):

    match data_x:
        case "Country":
            selected_headers_x = df["country"]
        case "Happiness":
            selected_headers_x = df["happiness"]
        case "GDP":
            selected_headers_x = df["gdp"]
        case "Social Support":
            selected_headers_x = df["social_support"]
        case "Life Expectancy":
            selected_headers_x = df["life_expectancy"]
        case "Freedom to make life_choices":
            selected_headers_x = df["freedom_to_make_life_choices"]
        case "Generosity":
            selected_headers_x = df["generosity"]
        case "Corruption":
            selected_headers_x = df["corruption"]

    match data_y:
        case "Country":
            selected_headers_y = df["country"]
        case "Happiness":
            selected_headers_y = df["happiness"]
        case "GDP":
            selected_headers_y = df["gdp"]
        case "Social Support":
            selected_headers_y = df["social_support"]
        case "Life Expectancy":
            selected_headers_y = df["life_expectancy"]
        case "Freedom to make life_choices":
            selected_headers_y = df["freedom_to_make_life_choices"]
        case "Generosity":
            selected_headers_y = df["generosity"]
        case "Corruption":
            selected_headers_y = df["corruption"]

    return selected_headers_x, selected_headers_y


x, y = get_data(data_x, data_y)

# Show the data on graph
figure = px.scatter(x=x, y=y, labels={"x": data_x, "y": data_y})
st.plotly_chart(figure)
