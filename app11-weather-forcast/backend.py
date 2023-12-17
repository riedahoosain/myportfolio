import requests
API_KEY = "20842ff75b793afea034fc4aef66393b"
place = "Cape Town"

def get_data(place, forecast_days=None, data_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if data_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if data_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place, forecast_days=1, data_type="Sky"))
