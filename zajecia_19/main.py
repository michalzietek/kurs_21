'''
Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

     <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
     <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv, out.json, out.txt lub out.pickle
     <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.


Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.json”.
python reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
pobieramy dane z pliku typu csv ale zapisujemy do obiektu typu json
'''
import sys


from zajecia_19.file_handler import FileHandler, CSVFileHandler, JsonFileHandler, PickleFileHandler

input_file = sys.argv[1]
output_file = sys.argv[2]
changes_in_file = sys.argv[3:]
file_reader = None
if input_file.split(".")[-1] == "csv":
    file_reader = CSVFileHandler()
elif input_file.split(".")[-1] == "json":
    file_reader = JsonFileHandler()
elif input_file.endswith(".pkl"):
    file_reader = PickleFileHandler()
else:
    file_reader = FileHandler()

file_reader.read_data_from_file()
file_reader.load_parameters(input_file=input_file, output_file=output_file, changes_in_file=changes_in_file)
file_reader.change_data_in_our_matrix()

if output_file.endswith(".csv"):
    file_writer = CSVFileHandler()
elif output_file.endswith(".json"):
    file_writer = JsonFileHandler()
elif output_file.endswith(".pkl"):
    file_writer = PickleFileHandler()
else:
    file_writer = FileHandler()

file_writer.load_parameters(input_file=input_file, output_file=output_file, changes_in_file=changes_in_file)
file_writer.matrix = file_reader.matrix
file_writer.write_data_to_file()