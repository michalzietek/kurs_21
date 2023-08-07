from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def run_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class ElecticMaintenance(ABC):

    @abstractmethod
    def utilize_batteries(self):
        pass

    @abstractmethod
    def check_power_level(self):
        pass


class OilMaintenance(ABC):
    @abstractmethod
    def load_fuel(self):
        pass

    @abstractmethod
    def check_oil_level(self):
        pass

class DieselEngine(Engine, OilMaintenance):
    def load_fuel(self):
        pass

    def check_oil_level(self):
        pass

    def run_engine(self):
        pass

    def stop_engine(self):
        pass
