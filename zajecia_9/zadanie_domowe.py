'''
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

    Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
    Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
    Polecenie "koniec" - Kończy działanie aplikacji.


Proces tworzenia użytkowników:

    Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
    Polecenie "koniec" - Wraca do pierwszego menu.


Proces zarządzania użytkownikami:

    Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
    Polecenie "koniec" - Wraca do pierwszego menu.


stworzyc system do zarzadzania nasza szkola:
kilka typow menu bedziemy miel
-glowne
-do tworzenia sobie uzytkownikow
-do zarzadzania uzytkownikami

Ogarnac jaka chcemy miec strukture tutaj jezeli chodzi o ta nasza szkole
w momencie tworzenia mozemy sobie skorzystac z jakis funkcji, bo widzimy, ze nasz kod się powtarza

'''
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}"


class Teacher:
    def __init__(self, name, surname, subject, grades):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grades = grades

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Zajęcia: {self.subject}, Klasy: {self.grades}"

#w domu potworzyli sobie klasy dla Nauczyciela i wychowawcy i zmienili je w naszej szkole


our_school = {
    "klasy": {
        "1a": {
            "uczniowie": [Student(name="Jan", surname="Kowalski")],
            "wychowawca": {
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        },
        "2a": {
            "uczniowie": [Student(name="Jan", surname="Nowak")],
            "wychowawca": {
                "imie": "Marta",
                "nazwisko": "Daszek"
            }
        },
    },
    "nauczyciele": [Teacher(name="Andrzej", surname="Iwan", subject="WF", grades=["1a", "2b"])]
}




def create_new_grade(grade):
    our_school["klasy"][grade] = {
        "uczniowie": [],
        "wychowawca": {}
    }

def create_student_in_existing_grade(name, surname, grade):
    our_school["klasy"][grade]["uczniowie"].append(Student(name=name, surname=surname))

def create_new_student(name, surname, grade):
    grade_exists = our_school.get("klasy").get(grade)
    if not grade_exists:
        create_new_grade(grade)
    create_student_in_existing_grade(name, surname, grade)

def find_grade_by_class_number(class_number):
    for grade_number, grade in our_school["klasy"].items():
        if grade_number == class_number:
            return f"Uczniowie to: {grade['uczniowie']} wychowawca to: {grade['wychowawca']}"
    return "Niestety nie znaleziono twojej klasy"

def find_class_teachers(class_number):
    found_teachers = []
    for teacher in our_school.get("nauczyciele"):
        if class_number in teacher.grades:
            found_teachers.append(teacher)
    return found_teachers

def find_student_by_name(name, surname):
    our_text = ""
    for grade_number, grade in our_school["klasy"].items():
        for student in grade.get("uczniowie"):
            if name == student.name and surname == student.surname:
                teachers = find_class_teachers(grade_number)
                for teacher in teachers:
                    our_text += f" Nauczyciel: {teacher.name} {teacher.surname} z przedmiotem: {teacher.subject} \n"
                return our_text
    return "Niestety twoja klasa nie ma żadnych zajęć"


initial_menu = "Witaj w swojej szkole. Podaj proszę co chcesz zrobić:\n 1.Uwtórz\n 2.Zarządzaj\n 3.Koniec\n"
create_menu = "Podaj jakiego użytkownika chcesz utworzyć:\n 1.Uczeń \n 2.Nauczyciel \n 3.Wychowawca \n 4.Koniec"
manage_menu = "Podaj kim chcesz zarządzać: \n 1.Klasa \n 2.Uczeń \n 3.Nauczyciel \n 4.Wychowawca \n 4.Koniec"
finish_program = False
while not finish_program:
    main_guess = input(initial_menu)
    if main_guess == "1":
        #wchodzimy w tryb dodawania czegokolwiek do naszej szkoly
        create_input = input(create_menu)
        if create_input == "1":
            name = input("Podaj imię ucznia")
            surname = input("Podaj nazwisko ucznia")
            grade = input("Podaj klasę ucznia")
            create_new_student(name, surname, grade)
            print(our_school)

    elif main_guess == "2":
        manage_input = input(manage_menu)
        if manage_input == "1":
            class_number = input("Podaj nazwę klasy")
            text_to_display = find_grade_by_class_number(class_number)
            print(text_to_display)
        elif manage_input == "2":
            student_name = input("Podaj imię ucznia: ")
            student_surname = input("Podaj nazwisko ucznia: ")
            text = find_student_by_name(student_name, student_surname)
            print(text)
