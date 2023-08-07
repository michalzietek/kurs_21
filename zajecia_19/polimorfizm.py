class Zwierze:
    def zawyj(self):
        print("miauu")

    def daj_mleko(self):
        print("Dalem mleko")

class Lew(Zwierze):
    def zawyj(self):
        print("rawwr")

class Zebra(Zwierze):
    def zawyj(self):
        print("Nie potrafie wyc")

lew = Lew()
zebra = Zebra()
zwierze = Zwierze()
print(isinstance(lew, Zwierze))
print(isinstance(lew, Zebra))
print(isinstance(lew, Lew))
lew.daj_mleko()

def przedstaw_zwierze(zwierze: Zwierze):
    print(zwierze)

przedstaw_zwierze(lew)
przedstaw_zwierze(zebra)


