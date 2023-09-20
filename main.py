import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {location}")

def get_data(days):

    dates = ["2022-01-01", "2022-01-02", "2022-01-03"]
    temperatures = [10, 11, 15]
    temperatures = [days*i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
