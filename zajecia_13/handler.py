import csv
from typing import List


class FileHandler:

    def __init__(self, input_file, output_file, changes_in_file):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_in_file: List[str] = changes_in_file
        self.matrix = []

    def read_data_from_file(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                self.matrix.append(line)


    def change_data_in_our_matrix(self):
        for incoming_change in self.changes_in_file:
            data_to_change = incoming_change.split(",")
            x_value = int(data_to_change[0])
            y_value = int(data_to_change[1])
            self.matrix[x_value][y_value] = data_to_change[2]

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(self.matrix)

    def run_program(self):
        self.read_data_from_file()
        self.change_data_in_our_matrix()
        self.write_data_to_file()
