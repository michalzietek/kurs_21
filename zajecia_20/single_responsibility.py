class Car:
    def __init__(self, tire, gearbox, steering_wheel):
        self.tire = tire
        self.engine = Engine()
        self.gearbox = gearbox
        self.steering_wheel = steering_wheel
        self.created_year = 2017


    def change_tire(self):
        print("Zmienilem koło")

    def burn_tire(self):
        print("Spalilem oponę")

    def change_gear(self):
        print("Zmieniłem bieg")

    def change_created_year(self, year):
        self.created_year = year

class Engine:
    def __init__(self):
        self.volume = "2.0l"
        self.power = "150HP"
        self.oil_level = "100%"

    def start_engine(self):
        print("wystartowałem silnik")

    def stop_engine(self):
        print("zatrzymałem silnik")

    def change_oil_level(self, oil_level):
        self.oil_level = oil_level


audi = Car(tire="Michelin", gearbox="skrzynia manualna", steering_wheel="kierownica_sportowa")
audi.engine.start_engine()
