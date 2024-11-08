import requests
from ApiKey import api
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15


def get_weather_data(city_name, api_key):
    """Fetch the weather data from the API for a given city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Return the data as JSON
    else:
        print(f"Error: Unable to retrieve weather data for {city_name}")
        return None


def display_weather(city_name, api_key):
    weather_data = get_weather_data(city_name, api_key)

    if weather_data:
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        print(f"Weather in {city_name}: {description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print(f"No weather data available for {city_name}")

city_name = input("Enter the name of the municipality: ")

display_weather(city_name, api)

