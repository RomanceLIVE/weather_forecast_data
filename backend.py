import requests
API_key = "5a5d2ecd19542c28d9b4c6e3cf1a7dbd"

def get_data(location, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_key}"
    response = requests.get(url)                                                   # changed city_id with location
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    # 8 because there are 8 info outputs per day (8 times 5 days = 40)
    filtered_data = filtered_data[:nr_values] #from 0 to nr_values

    return filtered_data

if __name__ == "__main__":
    print(get_data(location="Bucharest", forecast_days=3))