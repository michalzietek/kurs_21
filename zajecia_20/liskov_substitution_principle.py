from abc import abstractmethod


class Engine:
    def __init__(self):
        self.volume = "2.0l"
        self.power = "150HP"
        self.oil_level = "100%"
        self.engine_type = "Diesel"

    def start_engine(self):
        print("wystartowałem silnik")

    def stop_engine(self):
        print("zatrzymałem silnik")

    def change_oil_level(self, oil_level):
        self.oil_level = oil_level

    @abstractmethod
    def load_fuel(self):
        pass


class ElectirEngine(Engine):

    def load_fuel(self):
        print("Naładuj baterię :)")