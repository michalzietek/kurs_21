"""
Na podstawie zadania z lekcji 5 (operacje na koncie, sprzedaż/zakup itp.) należy zaimplementować poniższą część:

Saldo konta oraz magazyn mają zostać zapisane do pliku tekstowego, a przy kolejnym uruchomieniu programu ma zostać odczytany.
Zapisać należy również historię operacji (przegląd), która powinna być rozszerzana przy każdym kolejnym uruchomieniu programu.
"""
from zajecia_11.funkcje_do_zarzadzania_plikami import load_saldo_and_magazyn, save_saldo_and_magazyn_to_file, load_history
from enums import WyborKomendy

initial_message = "Witaj w Twoim magazynie. Lista dostępnych komend to:\n" \
                  " 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec"

end_program = False
saldo, magazyn = load_saldo_and_magazyn(file="saldo_i_magazyn.txt")
history = load_history(file="history.txt")
while not end_program:
    print(magazyn)
    print(saldo)
    print(initial_message)
    operation = input("Podaj operację, którą chcesz wykonać ")
    if operation == WyborKomendy.ZMIEN_SALDO.value:
        # Jeżeli chcemy odjąć to dajemy kwotę ujemną
        #TODO dla was poprosić jeszcze o rodzaj operacji (czy dodajemy czy odejmujemy)
        amount = float(input("Podaj kwotę, którą chcesz dodać lub odjąć z konta"))
        saldo += amount
        history.append(f"Wykonano instrukcję saldo, zasilono {amount}")
    if operation == WyborKomendy.SPRZEDAZ.value:
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

    if operation == WyborKomendy.PRZEGLAD.value:
        #TODO jak value bedzie wieksze od naszej listy to wyprintować długość listy len()
        value_from = input("Podaj początkowy zakres")
        value_to = input("Podaj końcowy zakres")
        if not value_to and not value_from:
            print(history)
        if value_from and not value_to:
            print(history[value_from:])

    if operation == WyborKomendy.KONIEC.value:
        end_program = True
        save_saldo_and_magazyn_to_file(file="saldo_i_magazyn.txt", saldo=saldo, magazyn=magazyn)
