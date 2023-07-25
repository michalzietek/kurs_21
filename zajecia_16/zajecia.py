import sympy

def literuj_wyraz(wyraz: str):
    counter = 0
    for letter in wyraz:

        return letter

def literuj_wyraz_za_pomoca_generatora(wyraz: str):
    for letter in wyraz:
        yield letter

def find_first_numbers(numbers):
    for number in range(numbers):
        if sympy.isprime(number):
            yield number


#first_numbers = find_first_numbers(1000)

def numbers_generator():
    for number in range(0, 5):
        yield number


class Student:

    def __init__(self, klasa, ocena_zachowania):
        self.klasa = klasa
        self.oceny_koncowe = {}
        self.ocena_zachowania = ocena_zachowania
        self.srednia_ocen = self.oblicz_srednia_ocen()
        self.index = 0


    def __str__(self):
        return f'Uczen z klasy {self.klasa} z srednia ocen {self.srednia_ocen}'

    def __repr__(self):
        return f"Reprezentacja ucznia z klasy {self.klasa}"

    def oblicz_srednia_ocen(self):
        suma_ocen = 0
        for ocena in self.oceny_koncowe.values():
            suma_ocen += ocena
        return suma_ocen/len(self.oceny_koncowe) if suma_ocen>0 else 0

    def __float__(self):
        return self.srednia_ocen

    def __setitem__(self, key, value):
        self.oceny_koncowe[key] = value

    def __getitem__(self, item):
        return self.oceny_koncowe.get(item)

    def __iter__(self):
        return iter(self.oceny_koncowe)

    def __next__(self):
        ilosc_przedmiotow = list(self.oceny_koncowe.keys())
        klucz = ilosc_przedmiotow[self.index]
        value = self.oceny_koncowe[klucz]
        self.index += 1
        return klucz, value


student = Student("1a", "dostateczne")
student2 = Student("1a", "bardzo dobre")
students = [student, student2]
student.oceny_koncowe["matematyka"] = 5
student["jezyk polski"] = 2
student.srednia_ocen = student.oblicz_srednia_ocen()
student2.oceny_koncowe["matematyka"] = 3
student2.srednia_ocen = student2.oblicz_srednia_ocen()

print(next(student))
print(next(student))
