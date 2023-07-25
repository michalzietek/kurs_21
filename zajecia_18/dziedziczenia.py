class Ciasto:
    def __init__(self, maka, jajka, mleko, drozdze = None):
        self.maka = maka
        self.jajka = jajka
        self.mleko = mleko
        self.drozdze = drozdze

    def upiecz_ciasto(self):
        print(f"Upieklem ciasto z {self.maka} maki")

    def ubij_jajka(self):
        self.jajka = 0
        print("Nie masz już jajek")

class Makowiec:
    def __init__(self, maka, jajka, mleko, drozdze, mak):
        self.maka = maka
        self.jajka = jajka
        self.mleko = mleko
        self.drozdze = drozdze
        self.mak = mak

    def zrob_mak(self):
        print("Zrobilem mak")


class Makowiec_Krolewski(Ciasto):

    def __init__(self, maka, jajka, mleko):
        super().__init__(maka, jajka, mleko)


    def ubij_jajka(self):
        super().ubij_jajka()
        print("Jajka ubilem ale na makowiec krolewski")

makowiec_podstawowy = Makowiec(maka=100, jajka=2, mleko=100, drozdze=20, mak=30)
makowiec_podstawowy.zrob_mak()

makowiec_krolewski = Makowiec_Krolewski(maka=100, jajka=2, mleko=300)
makowiec_krolewski.upiecz_ciasto()
makowiec_krolewski.ubij_jajka()

class Auto:
    def uruchom_silnik(self):
        print("uruchomilem silnik auta")

class Autobus:
    def uruchom_silnik(self):
        print("uruchomilem silnik autobusu")

class Mercedes(Autobus, Auto):
    def __init__(self):
        pass

    def uruchom_silnik(self):
        Auto.uruchom_silnik(self)
        self.sprawdz_czy_masz_oba_kierunkowskazy()
        self.wylacz_kierunkowskaz()

    def wylacz_kierunkowskaz(self):
        self.sprawdz_czy_masz_oba_kierunkowskazy()
        print("wylaczylem kierunkowskaz")

    def sprawdz_czy_masz_oba_kierunkowskazy(self):
        print("Sprawdzono czy masz obydwa kierunkowskazy sprawne")
mercedes = Mercedes()
mercedes.uruchom_silnik()

auto = Auto()

class BMW(Autobus, Auto):
    def wylacz_kierunkowskaz(self):
        print("Nie masz kierunkowskazow")

    def uruchom_silnik(self):
        super().uruchom_silnik()
        self.wylacz_kierunkowskaz()

typ_auta = input("Podaj mi marke swojego auta")
if typ_auta == "Mercedes":
    auto = Mercedes()
elif typ_auta == "BMW":
    auto = BMW()

auto.uruchom_silnik()
