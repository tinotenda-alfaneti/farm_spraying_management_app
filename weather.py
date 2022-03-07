import requests
import os
from dotenv import load_dotenv


load_dotenv()

URL_LINK = os.environ.get('WEATHER_URL')
API_KEY = os.environ.get('WEATHER_API_KEY')

class Weather:
    
    # initialising the instance variables taking the parameter of city
    def __init__(self, town):
        self.town = town
        self.parameters = {"key": API_KEY, "q": self.town, "days": 3,"day":'day'}
        self.response = None
        self.wind_speed = 0
        self.temperature = 0
        self.humidity = 0
        self.chance_of_rain = 0
        self.date = None
        self.weather_info = None
    
    def get_weather_info(self):

        self.response = requests.get(url=URL_LINK, params=self.parameters)
        return self.response.json()
    
    def day_weather_forecast(self, day):

        self.weather_info = self.get_weather_info()

        first_part = self.weather_info['forecast']['forecastday'][day]['day']
        self.date = self.weather_info['forecast']['forecastday'][day]['date']
        self.temperature = first_part['avgtemp_c']
        self.humidity = first_part['avghumidity']
        self.wind_speed = first_part['maxwind_kph']
        self.chance_of_rain = first_part['daily_chance_of_rain']

        return self.date, self.wind_speed, self.temperature, self.humidity, self.chance_of_rain
    
    def __str__(self):
        return f"The weather information for {self.town}"

# test_weather_record = Weather("Accra")
# print(test_weather_record.day_weather_forecast(0))
# print(test_weather_record.day_weather_forecast(1))
# print(test_weather_record.day_weather_forecast(2))