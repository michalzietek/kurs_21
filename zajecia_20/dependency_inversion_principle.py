from abc import ABC, abstractmethod

class EngineInterface(ABC):
    @abstractmethod
    def run_engine(self):
        pass


    @abstractmethod
    def stop_engine(self):
        pass


class Engine(EngineInterface):
    def run_engine(self):
        print("Uruchomilem silnik")

    def stop_engine(self):
        print("Zatrzymalem silnik")

class ElectricEngine(Engine):
    def run_engine(self):
        print("Wystartowalem silnik elektryczny")

    def stop_engine(self):
        print("Zatrzymalem silnik elektryczny")


electric_engine = ElectricEngine()
electric_engine.stop_engine()
electric_engine.run_engine()