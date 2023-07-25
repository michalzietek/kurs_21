import json

import requests
from geopy.geocoders import Nominatim

API_URL = "https://api.open-meteo.com/v1/forecast"
class WeatherForecast:

    def __init__(self, date, city):
        self.date = date
        self.city = city
        self.weather_forecast = self.load_data_from_file()

    def load_data_from_file(self):
        with open("opady.txt", mode="r+") as file:
            data_in_file = file.read()

        return json.loads(data_in_file) if data_in_file else {}

    def retrieve_data_from_api(self, latitude, longitude):
        response = requests.get(url=API_URL,
                                params={
                                    "latitude": latitude,
                                    "longitude": longitude,
                                    "start_date": self.date,
                                    "end_date": self.date,
                                    "hourly": "rain",
                                    "daily": "rain_sum",
                                    "timezone": "Europe/London"
                                })
        data = json.loads(response.text)
        return data

    def find_coordinates_for_city(self):
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(self.city)
        return location.latitude, location.longitude

    def check_raining_sum(self, data):
        raining_sum = data.get("daily").get("rain_sum")[0]
        if raining_sum > 0.0:
            return "Bedzie padać"
        elif raining_sum == 0.0:
            return "Nie bedzie padac"
        else:
            return "Nie wiem"

    def retrieve_data(self):
        city_data = self.weather_forecast.get(self.city)
        if city_data:
            if city_data.get(self.date):
                print("Pobralem z pliku")
                return city_data[self.date], False
        latitude, longitude = self.find_coordinates_for_city()
        data = self.retrieve_data_from_api(latitude, longitude)
        raining_data = self.check_raining_sum(data)
        print("Zapytalem API")
        return raining_data, True

    def transform_data_in_file(self, raining_info):
        '''
        tutaj laczymy dane z pliku z danymi aplikacji(api)
        '''
        if self.weather_forecast.get(self.city):
            self.weather_forecast[self.city][self.date] = raining_info
        else:
            self.weather_forecast[self.city] = {}
            self.weather_forecast[self.city][self.date] = raining_info
        return json.dumps(self.weather_forecast).replace("'", '"')

    def write_data_to_file(self, raining_info):
        print("Zapisano plik od nowa")
        with open("opady.txt", mode="w") as file:
            new_data = self.transform_data_in_file(raining_info)
            file.write(new_data)

    def items(self):
        for city in self.weather_forecast.keys():
            for date in self.weather_forecast.get(city).keys():
                yield date, city

    def __iter__(self):
        return iter(self.weather_forecast)

    def __setitem__(self, key, value):
        city, date = key
        city_data = self.weather_forecast.get(city)
        if not city_data:
            self.weather_forecast[city] = {date: None}
        self.weather_forecast[city][date] = value

    def __getitem__(self, item):
        city, date = item
        return self.weather_forecast[city][date]