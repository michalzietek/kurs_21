"""
def check_whether_user_has_shortened_work_time(users_job):
    return users_job == "Policjant" # zwroci tutaj albo
     True jeśli jest albo False jeśli nie ma

def check_my_age(users_age, users_job="Programista", *args, **kwargs):
    print(args)
    for argument in args:
        print(argument)
        if argument > 3999:
            print("Masz dobrze płatną pracę")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    if check_whether_user_has_shortened_work_time(users_job):
        if users_age < 18:
            return "Nie powinineneś jeszcze pracować"
        elif 18 < users_age < 40:
            return "Jesteś w stanie pracować"
        else:
            return "Jesteś już w wieku emerytalnym"
    else:
        if users_job == "Nauczyciel":
            return "Jesteś nauczycielem"
        return "Nie weszlismy w zaden warunek"

my_job = input("Podaj gdzie pracujesz ")
my_age = int(input("Podaj swój wiek "))

if my_job == "Konserwator":
    displayed_text = check_my_age(my_age, my_job, 4000)
elif my_job == "Programista":
    displayed_text = check_my_age(my_age, my_job, liczba_projektow=21)
elif my_job == "Nauczyciel":
    displayed_text = check_my_age(my_age,  users_job=my_job)
else:
    displayed_text = check_my_age(my_age, my_job)
def check_my_grades(*args):
    for grade in args:
        if grade == 1:
            print("Dostales jedynke")
check_my_grades(1,2,3,1,5,6,3)
"""


class Przepis:
    def __init__(self, jajka, maka, cukier, bakalie=None):
        self.jajka = jajka
        self.maka = maka
        self.cukier = cukier
        self.duperele = bakalie

    def ubij_jajka(self):
        print(f"Ubito {self.jajka} jajek")

    def zmniejsz_przepis_o_jedno_jajko(self):
        self.jajka -= 1

    def __str__(self):
        return f"Skladniki na ciasto to:\n Jajka: {self.jajka}, ....."

    def pokaz_mi_moje_skladniki(self):
        return f"{self.jajka} = "


ciasto_marchewkowe = Przepis(3, 400, 100)
kakaowiec = Przepis(jajka=5, maka=250, cukier=150, bakalie=1000)
makowiec = Przepis(jajka=4, maka=150, cukier=200, bakalie=100)

ciasto_marchewkowe.zmniejsz_przepis_o_jedno_jajko()


def funkcja():
    pass


ciasto_marchewkowe.ubij_jajka()
kakaowiec.ubij_jajka()
print(ciasto_marchewkowe)
