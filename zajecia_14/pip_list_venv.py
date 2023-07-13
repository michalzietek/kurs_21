import math
import numpy

pi = math.pi
def check_if_i_am_adult(age):
    if age>18:
        print("Jesteś pełnoletni")
        return True
    else:
        print("Nie jesteś pełnoletni")
        return False

def check_if_i_am_adult_new_version(age):
    text_to_display = "Jesteś pełnoletni" if age>18 else "Nie jesteś pełnoletni"
    print(text_to_display)
    return True if age>18 else False

def check_salary(salary):
    return salary < sum(salaries)/len(salaries) and salary%3==0

#age = input("Podaj mi swój wiek")
#check_if_i_am_adult(int(age))
#check_if_i_am_adult_new_version(int(age))
students = ["Jacek", "Marek", "Antek", "Marta"]
female_students = []
for student in students:
    if student.endswith("a"):
        female_students.append(student)
female_students_1 = ["Michal" for student in students if student.endswith("a")]
salaries = [1000, 5000, 3000, 4500, 6000, 7000, 1200]
salaries_above_average = [salary for salary in salaries if check_salary(salary)]
print(salaries_above_average)
print(female_students)
print(female_students_1)
["to co chcemy dodac do listy" "petla w ktorej te zmiany beda dodawane"
 " - tutaj zawsze musi byc jakas struktura albo zmienna po ktorej mozna iterowac"
  "(opcjonalnie) warunek logiczny czyli if na obciecie tej naszej petli"]
our_school = {
    "Michal": 5,
    "Jacek": 4,
    "Maciej": 3,
    "Tomek": 6,
    "Artur": 1
}

students_who_passed_the_exam = [student for student, grade in our_school.items() if grade > 1]
students_who_passed_exam_with_grades = {student: our_school.get(student) for student in our_school.keys()}

for student in our_school.keys():
    print(student)
    our_school.get(student)

alpha_digits = [digit for digit in "Michal123++/" if digit.isdigit()]

my_array = numpy.array([1, 2, 3, 4, 5, 6,])
print(my_array)