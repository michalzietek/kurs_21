import csv
import json
import pickle
from typing import List
from abc import abstractmethod

from zajecia_19.exceptions import WrongFileExtensionError


class FileHandler:

    def __init__(self):
        self.input_file = None
        self.output_file = None
        self.changes_in_file: List[str] = []
        self.matrix = []

    @abstractmethod
    def read_data_from_file(self):
        raise WrongFileExtensionError(message="Nie ma takiego rozszerzenia, jedyne opcje to .pkl, .txt, .csv, .json")

    def load_parameters(self, input_file, output_file, changes_in_file):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_in_file = changes_in_file


    def change_data_in_our_matrix(self):
        for incoming_change in self.changes_in_file:
            data_to_change = incoming_change.split(",")
            x_value = int(data_to_change[0])
            y_value = int(data_to_change[1])
            self.matrix[x_value][y_value] = data_to_change[2]

    def download_data_to_matrix(self, matrix):
        self.matrix = matrix

    @abstractmethod
    def write_data_to_file(self):
        raise WrongFileExtensionError(message="nie ma takiego rozszerzenia")


class CSVFileHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                self.matrix.append(line)


    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(self.matrix)


class JsonFileHandler(FileHandler):
    def read_data_from_file(self):
        with open(self.input_file) as file:
            self.matrix = json.load(file)

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            json.dump(self.matrix, file)

class PickleFileHandler(FileHandler):
    def read_data_from_file(self):
        with open(self.input_file, mode="rb") as file:
            self.matrix = pickle.load(file)

    def write_data_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.matrix, file)
