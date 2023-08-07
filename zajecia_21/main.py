from enums import WyborKomendy
from zajecia_21.functions import manager
from zajecia_21.magazyn_handler import MagazynHandler

initial_message = "Witaj w Twoim magazynie. Lista dostępnych komend to:\n" \
                  " 1. Saldo\n 2. Sprzedaż\n 3. Zakup\n 4. Konto\n 5. Lista\n 6. Magazyn\n 7. Przegląd\n 8. Koniec"
magazyn_handler = MagazynHandler()
end_program = False
while not end_program:
    print(initial_message)
    print(manager.history)
    print(f"saldo: {manager.saldo}")
    print(manager.magazyn)
    operation = input("Podaj operację, którą chcesz wykonać ")
    if operation == WyborKomendy.KONIEC.value:
        end_program = True
        manager.save_saldo_and_magazyn_to_file(file=manager.magazyn_and_saldo_file,
                                               saldo=manager.saldo,
                                               magazyn=manager.magazyn)
        manager.save_history(file=manager.history_file, history=manager.history)
    else:
        manager.execute(operation)
