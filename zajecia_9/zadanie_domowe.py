class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}"


class Teacher:

    szkola = "szkola nr 4"

    def __init__(self, name, surname, subject, grades):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grades = grades

    def __repr__(self):
        return f"Imię: {self.name}, Nazwisko: {self.surname}, Zajęcia: {self.subject}, Klasy: {self.grades}, Szkoła: {self.szkola}"

    def check_how_many_classes_teacher_has(self):
        return len(self.grades)

    def show_me_my_name(self):
        print(f"Twoje imie to {self.name}")

    @classmethod
    def zmien_moja_szkole(cls, nowa_szkola):
        cls.szkola = nowa_szkola

    @staticmethod
    def przywitaj_sie():
        print("Czesc moj swiecie")


#w domu potworzyli sobie klasy dla Nauczyciela i wychowawcy i zmienili je w naszej szkole

teacher = Teacher(name="Andrzej", surname="Iwan", subject="WF", grades=["1a", "2b"])
teacher2 = Teacher(name="Andrzej", surname="Iwan", subject="WF", grades=["1a", "2b"])
teacher.zmien_moja_szkole("szkola numer 1")
teacher2.zmien_moja_szkole("szkola numer 2")
teacher.przywitaj_sie()

print(teacher2)
print(teacher)
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
    "nauczyciele": [Teacher(name="Andrzej", surname="Iwan", subject="WF", grades=["1a", "2b"]),
                    Teacher(name="Andrzej", surname="Iwan", subject="WF", grades=["1a", "2b"])],
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
