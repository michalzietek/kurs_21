class Car:
    def __init__(self, tire, gearbox, steering_wheel, engine):
        self.tire = tire
        self.engine = engine
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