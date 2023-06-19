student_1 = "Marcin Brzeczyszczykiewicz"
student_2 = "Michal Zietkowski"
student_3 = "Maciej Dlugosz"
student_4 = "Adam Wawszczyk"
zadanie_1_student_1 = True
zadanie_1_student_2 = False
students = ["Marcin Brzeczyszczykiewicz", "Michal Zietkowski", "Maciej Dlugosz", "Adam Wawszczyk", True, 11, [1, 2, 3]]
new_student = students[0]
new_student = "Maja"
students_length = len(students)
print(students)
print(students[1:4:2])
'''
#students_name = input("Podaj imie studenta: ")
#students_surname = input("Podaj nazwisko studenta: ")
#new_student = students_name + students_surname
#students.append(new_student)
students.insert(0, "Ula Nowak")
students.append("Marcin Zabawa")
print(type(students))
zadanie_1 = [True, False, True, True]
new_students = ["Filip Jedynak", "Maciej Nowak"]
actual_students_list = students + new_students
print(actual_students_list)
#students.remove("Marcin Brzeczyszczykiewicz")
print(students)
print(students.index("Michal Zietkowski"))
#students[2] = "Adam Nowak"
print("Michal Zietkowski" in students)
print(bool([0]))
#print(students[0])
for index, student in enumerate(students):
    print(index)
    if student == "Michal Zietkowski":
        students[index] = "Mateusz Zietkowski"
    print(type(student) == str)

print(students)

my_tuple = (1, 2, 3, False)
print(id(my_tuple))
my_tuple_1 = tuple((1, 2, 3, False))
new_int = int("123")
print(new_int)
print(id(my_tuple_1))
#print(my_tuple)
#print
users = [
    ("Michal Zietkowski", 180, 85),
    ("Michal Zietkowski", 185, 95),
    ("Michal Zietkowski", 185, 95),
]
print(my_tuple.index(3))
print(my_tuple[0])
for user in users:
    print(user[0])


students_set = {"Michal Zietkowski", "Jan Wojcik", "Andrzej Wojcik", 1, 2, False}
print(students_set)
for student in students_set:
    print(student)
students_set.remove("Michal Zietkowski")
students_set.add("Jacek Szkudlarek")
print(students_set)

students_dict = {
    "student_1": "Michal Zietkowski",
    "student_2": "Jan Wojcik",
    "student_3": "Andrzej Wojcik",
}
new_students_dict = {
    "student_1": {
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "oceny": [2,3,4,1],
        "nauczyciel": "Jacek Grabowski"
    },
    "student_2": {
        "imie": "Michal",
        "nazwisko": "Wojcik",
        "oceny": [2, 3, 4, 1],
        "nauczyciel": "Jacek Grabowski"
    },

}
print(students_dict["student_1"])
print(students_dict.get("student_4", "Michal Zietkowski"))
print(students_dict)
students_dict["student_4"] = "Jacek Szkudlarek"
#students_dict.get("student_4") = "Nowa wartosc" <- nie jesteśmy w stanie przypisać wartości do słownika
students_dict["student_4"] = "Michal Zietkowski"
print(students_dict)
for key, student in new_students_dict.items():
    for detail_key, detail in student.items():
        print(f"{detail_key} : {detail}")

print(students_dict)
'''