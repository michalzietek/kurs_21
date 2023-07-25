from zajecia_17.weather_forecast import WeatherForecast

'''
Zoptymalizuj kod z poprzedniego zadania z pogodą.

Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku, a także odpytywania API.

Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:

     __setitem__
     __getitem__
     __iter__
     items


Wykorzystaj w kodzie poniższe zapytania:

    weather_forecast[date] da odpowiedź na temat pogody dla podanej daty
    weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już zapisanych rezultatów przy wywołaniu
    weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda
'''
def run_program(weather_forecast: WeatherForecast):
    weather_info, write_to_file = weather_forecast.retrieve_data()
    weather_forecast.write_data_to_file(weather_info)


forecast_object = WeatherForecast(date="2023-07-25", city="Poznan")
run_program(forecast_object)
for item in forecast_object.items():
    print(item)

for city in forecast_object:
    print(f"{city}")

forecast_object["Wroclaw", "2023-07-24"] = "Sucho jak w moim portfelu"
print(forecast_object["Wroclaw", "2023-07-24"])