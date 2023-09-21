import requests
API_key = "5a5d2ecd19542c28d9b4c6e3cf1a7dbd"

def get_data(location, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_key}"
    response = requests.get(url)                                                   # changed city_id with location
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(location="Bucharest"))