import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {location}")



""" 
def get_data(days):
    dates = ["2022-01-01", "2022-01-02", "2022-01-03"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures 
"""

if location:
    # Get the temperature/sky data
    filtered_data = get_data(location, days)

    if options == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if options == "Sky":
        images = {"Clear":"clear.png","Clouds":"clouds.png","Rain":"rain.png","Snow":"snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width=115)


