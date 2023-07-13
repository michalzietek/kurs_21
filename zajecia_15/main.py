import json

import requests
from geopy.geocoders import Nominatim

API_URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}" \
          "&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"


def retrieve_data_from_api(latitude, longitude, searched_date):
    response = requests.get(API_URL.format(latitude=latitude, longitude=longitude, searched_date=searched_date))
    data = json.loads(response.text)
    return data

def find_coordinates_for_city(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude

def check_raining_sum(data: dict):
    raining_sum = data.get("daily").get("rain_sum")[0]
    if raining_sum > 0.0:
        return "Bedzie padać"
    elif raining_sum == 0.0:
        return "Nie bedzie padac"
    else:
        return "Nie wiem"

def read_data_from_file():
    with open("opady.txt", mode="r+") as file:
        data_in_file = file.read()

    return json.loads(data_in_file) if data_in_file else {}

def transform_data_in_file(data, city, date, raining_info):
    '''
    tutaj laczymy dane z pliku z danymi aplikacji(api)
    '''
    if data.get(city):
        data[city][date] = raining_info
    else:
        data[city] = {}
        data[city][date] = raining_info
    return json.dumps(data).replace("'", '"')


def write_data_to_file(data, city, date, raining_info):
    print("Zapisano plik od nowa")
    with open("opady.txt", mode="w") as file:
        new_data = transform_data_in_file(data, city, date, raining_info)
        file.write(new_data)


def retrieve_data(file_data, city, date):
    city_data = file_data.get(city)
    if city_data:
        if city_data.get(date):
            print("Pobralem z pliku")
            return city_data[date], False
    latitude, longitude = find_coordinates_for_city(city)
    data = retrieve_data_from_api(latitude, longitude, date)
    raining_data = check_raining_sum(data)
    print("Zapytalem API")
    return raining_data, True

city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę")
date = input("Podaj datę, dla której chcesz sprawdzić pogodę")
'''
class WeatherAPI:

    def __init__(self, date, city):
        self.date = date
        self.city = city
        self.longitude, self.latitude = self.find_coordinates_for_city()
        self.file_data = self.read_data_from_file()
        self.raining_data = None

    def find_coordinates_for_city(self):
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(self.city)
        return location.latitude, location.longitude

    def read_data_from_file(self):
        with open("opady.txt", mode="r+") as file:
            data_in_file = file.read()

        return json.loads(data_in_file) if data_in_file else {}

    def check_raining_sum(self, data: dict):
        raining_sum = data.get("daily").get("rain_sum")[0]
        if raining_sum > 0.0:
            return "Bedzie padać"
        elif raining_sum == 0.0:
            return "Nie bedzie padac"
        else:
            return "Nie wiem"

    def retrieve_data_from_api(self):
        response = requests.get(API_URL.format(latitude=self.latitude,
                                               longitude=self.longitude,
                                               searched_date=self.date))
        data = json.loads(response.text)
        return data

    def retrieve_data(self):
        city_data = self.file_data.get(city)
        if city_data:
            if city_data.get(date):
                print("Pobralem z pliku")
                return city_data[date], False
        data = self.retrieve_data_from_api()
        self.raining_data = self.check_raining_sum(data)

    def write_data_to_file(self):
        print("Zapisano plik od nowa")
        with open("opady.txt", mode="w") as file:
            new_data = self.transform_data_in_file(self.raining_data)
            file.write(new_data)

    def transform_data_in_file(self, raining_info):
        if data.get(city):
            data[city][date] = raining_info
        else:
            data[city] = {}
            data[city][date] = raining_info
        return json.dumps(data).replace("'", '"')
'''
data = read_data_from_file()
raining_data, write_new_data_to_file = retrieve_data(data, city, date)
if write_new_data_to_file:
    write_data_to_file(data, city, date, raining_data)