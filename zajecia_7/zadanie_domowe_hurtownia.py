'''
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

    saldo
     sprzedaż
    zakup
    konto
    lista
    magazyn
    przegląd
    koniec


Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

    saldo - Program pobiera kwotę do dodania lub odjęcia z konta. ->
     dostajemy przelew albo go komus zlecamy(np dla pracownikow) + dp tego dodajemy wpis do historii
    sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
    sprzedajemy produkt i potrzebujemy do tego sprawdzic:
    -czy towar jest na magazynie
    -nie potrzebuje sprawdzic salda
    po wykonaniu operacji:
    -usunac produkt z magazynu
    -dodac kwote do naszego salda
    w momencie, gdy operacja się nie powiedzie to i tak zapisujemy do historii ale z informacją, że operacja się nie udała!
    zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    kupujemy produkt:
    -najpierw musimy sprawdzic czy nas na niego stac
    Jesli nas stac to:
    -dodac produkt do magazynu:
        -jezeli produkt jest na magazynie to dodac ilosc
        -jezeli produktu nie ma to dodac nowy produkt
    -zmniejszyc stan naszego konta
    dodajemy dane do historii
    Jeśli nas nie stać:
    -Wyrzucić błąd, że nas nie stać
    konto - Program wyświetla stan konta.
    lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
    magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
    - tutaj danymi wejsciowymi bedzie nazwa i trzeba wyszukac w naszym magazynie po nazwie
    przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
    - jezeli chcemy wiecej operacji niz faktycznie ich bylo, to wyrzucamy blad i podajemy ilosc operacji
    - W przeciwnym wypadku printujemy naszą historię(listę)
    koniec - Aplikacja kończy działanie.


Dodatkowe wymagania:

    Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
    Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
    Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
    Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.



'''
saldo = 8000.0
magazyn = {
    "rower": {
        "ilość": 2,
        "cena": 100
    },
    "łódka": {
        "ilość": 3,
        "cena": 1500
    }
}
history = []
initial_message = "Witaj w Twoim magazynie. Lista dostępnych komend to:\n" \
                  " 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec"

end_program = False
while not end_program:
    print(magazyn)
    print(saldo)
    print(initial_message)
    operation = input("Podaj operację, którą chcesz wykonać ")
    if operation == "1":
        # Jeżeli chcemy odjąć to dajemy kwotę ujemną
        #TODO dla was poprosić jeszcze o rodzaj operacji (czy dodajemy czy odejmujemy)
        amount = float(input("Podaj kwotę, którą chcesz dodać lub odjąć z konta"))
        saldo += amount
        history.append(f"Wykonano instrukcję saldo, zasilono {amount}")
    if operation == "2":
        print(magazyn)
        # przyklad dla Piotrka
        #product, amount = tuple(input("Podaj nazwę produktu, który chcesz kupić").replace(" ", "").split(","))
        #amount = float(amount)
        product = input("Podaj nazwę produktu: ")
        #TODO zmienić na floaty bo np kg
        amount = int(input("Podaj ilość, którą chcesz sprzedać: "))
        product_found = False
        #najpierw sprawdzmy czy mamy towar
        for item, item_details in magazyn.items():
            if product == item:
                item_details["ilość"] -= amount
                saldo += (item_details["cena"] * amount)
                product_found = True
                history.append(f"Sprzedano {product} w ilości {amount}")
                break
        if not product_found:
            history.append(f"Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie")

    if operation == "7":
        #TODO jak value bedzie wieksze od naszej listy to wyprintować długość listy len()
        value_from = input("Podaj początkowy zakres")
        value_to = input("Podaj końcowy zakres")
        if not value_to and not value_from:
            print(history)
        if value_from and not value_to:
            print(history[value_from:])
