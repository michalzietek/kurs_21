from abc import abstractmethod

from zajecia_20.car import Car


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

class ElectricEngine(Engine):
    def __init__(self, engine_type):
        super().__init__()
        self.engine_type = engine_type

    def load_fuel(self):
        print("Musisz naladowac baterie")

class DieselEngine(Engine):
    def __init__(self, engine_type):
        super().__init__()
        self.engine_type = engine_type

    def load_fuel(self):
        print("Musisz zatankować diesla")


engine = Engine()
electric_engine = ElectricEngine(engine_type="electric")

electric_audi = Car(tire="Michelin", gearbox="skrzynia automatyczna", steering_wheel="kierownica podstawowa",
                    engine=electric_engine)
