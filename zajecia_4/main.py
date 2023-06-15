import sys

my_name = "Michal"
print(my_name)
print("cos do napisania")
'''
my_age = int(input("Podaj swój wiek: "))
my_sex = None
if  21 > my_age >= 18:
    my_sex = "Male"
    print("Gratulacje jesteś pełnoletni")
    print(my_sex)
elif my_age < 18:
    print("Nie mozesz decydodwać sam o sobie")
elif 95 > my_age >= 21:
    print("Mozesz glosowac na wyborach")
else:
    print("Nie masz praw wyborczych")
print(my_sex)
'''
my_age = 10
'''
my_job = input("Podaj swój zawód")
while my_job!="Programista":
    print("Masz super inny ciekawy zawód, nie musisz siedzieć 24 godzin dziennie przed komputerem")
    if my_job == "Tester manualny":
        break
    else:
        pass
    my_job = input("Podaj swój zawód")
else:
    print("Niestety masz pewnie dużą wadę wzroku!")

while my_age < 18:
    if my_age < 16:
        print(f"Przed Toba jeszcze sporo lat do pełnoletności {my_age}")
    else:
        print("To już zaraz")
    my_age += 1
print("Jesteś już pełnoletni")

for letter in my_name:
    if letter == "M":
        continue
    print(letter)

my_job = input("Podaj swoją pracę ")
match my_job:
    case "Nauczyciel":
        print("Musisz mieć sporą wiedzę z danego przedmiotu")
    case "Kierowca":
        print("Musisz dobrze prowadzić pojazdy")
    case "Tancerz":
        print("Musisz dobrze czuć rytm")
    case "Polityk":
        print("Musisz dobrze kłamać")
    case "Polityk":
        print("Dobrze klamiesz")
    case _:
        print("Nie znaleziono twojego zawodu")


match my_age:
    case _ if 0>my_age>18:
        print("Nie jesteś pełnoletni")
    case _ if 18>=my_age>21:
        print("Jesteś pełnoletni, ale nie możesz być wybranym")

if my_job == "Nauczyciel":
    print("eeee")
elif my_job == "Kierowca":
    print("eeafea")
else:
    print("Nie znaleziono twojej pracy")
'''
slownik = {
    "1": {
        "uczniowie": [],
        "dupa": "1234"
    }
}
for key, value in slownik.items():
    print(key, value)