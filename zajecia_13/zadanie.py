'''
Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

     <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
     <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
    <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na podane miejsce.


Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".
drzwi,3,7,0
kanapka,12,5,1
pedzel,22,34,5
plakat,czerwony,8,kij


python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
'''
import csv
import sys

from zajecia_13.handler import FileHandler

def read_data_from_file(file):
    matrix = []
    with open(file) as file:
        reader = csv.reader(file)
        for line in reader:
            matrix.append(line)
    return matrix

def change_data_in_our_matrix(matrix, incoming_data):
    data_to_change = incoming_data.split(",")
    x_value = int(data_to_change[0])
    y_value = int(data_to_change[1])
    matrix[x_value][y_value] = data_to_change[2]

def write_data_to_file(file, matrix):
    with open(file, mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)
'''
matrix = read_data_from_file(file="zadanie_13.csv")
for argument in sys.argv[3:]:
    change_data_in_our_matrix(matrix, argument)
print(matrix)
write_data_to_file("out.csv", matrix)
'''

FileHandler(
    input_file=sys.argv[1],
    output_file=sys.argv[2],
    changes_in_file=sys.argv[3:]
).run_program()
