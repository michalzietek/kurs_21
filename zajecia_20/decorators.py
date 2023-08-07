import time

def wylicz_wynik(dzialanie, pierwsza_liczba, druga_liczba):
    if dzialanie == "dodawanie":
        return dodawanie(pierwsza_liczba, druga_liczba)
    elif dzialanie == "odejmowanie":
        return odejmowanie(pierwsza_liczba, druga_liczba)

def dodawanie(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba

def odejmowanie(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba - druga_liczba


#nasze_dzialanie = input("Podaj operację, która chcesz wykonać")
#print(wylicz_wynik(nasze_dzialanie, 5, 4))

def sprawdz_liczbe():
    print("Sprawdzilem liczbe")

funkcja_do_wykoania = sprawdz_liczbe
funkcja_do_wykoania()

clients = ["Jan", "Zabka", "DPD", "Ikea"]
pracownicy = ["Michal Zietkowski", "Andrzej Duda", "Jan Kowalski"]

def login_required(function):
    print("Sprawdzam, czy jestem zalogowany ")# w prawdziwym zyciu, to pewnie byłoby odpytanie o naszą sesję
    print("Jestem zalogowany")
    function()

def sprawdz_moich_klientow():
    print(clients)

login_required(sprawdz_moich_klientow)

def login_required_decorator(function):
    def wrapper(*args, **kwargs):
        print("Sprawdzam czy jestem zalogowany")
        print("Jestem zalogowany")
        function()
    return wrapper


@login_required_decorator
def sprawdz_liste_pracownikow():
    print(pracownicy)

sprawdz_liste_pracownikow()


def timeit(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Program wykonal sie w czasie {execution_time}")
    return wrapper

@timeit
def uspij_program():
    time.sleep(2)
    print("Wywolalem funkcje")

@timeit
def wyprintuj_wszystkich_klientow():
    for client in clients:
        print(client)

uspij_program()
wyprintuj_wszystkich_klientow()