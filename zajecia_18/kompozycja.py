class Silnik:
    def __init__(self, pojemnosc, moc):
        self.pojemnosc = pojemnosc
        self.moc = moc

    def uruchom(self):
        print(f"Uruchomilem silnik o pojemności {self.pojemnosc} i mocy {self.moc}")

class Samochod:
    def __init__(self, marka, model, rocznik, silnik: Silnik):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.silnik = silnik

    def odpal_silnik(self):
        self.silnik.uruchom()

silnik_20_tdi = Silnik(pojemnosc=2000, moc=150)
samochod = Samochod(marka="BMW", model="seria 3", rocznik=2019, silnik=silnik_20_tdi)
samochod.odpal_silnik()