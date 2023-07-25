from abc import ABC, abstractmethod

class Samochod(ABC):

    @abstractmethod
    def zbuduj_silnik(self):
        pass


    @abstractmethod
    def zaloz_opony(self):
        pass

class Meredes(Samochod):

    def zbuduj_silnik(self):
        print("zbudowalem silnik mercedesa")

    def zaloz_opony(self):
        print("założyłem opony")

mercedes = Meredes()
mercedes.zbuduj_silnik()