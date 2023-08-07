from zajecia_21.manager import Manager

manager = Manager(history_file="history.txt", magazyn_and_saldo_file="saldo_i_magazyn.txt")

@manager.assign("Saldo")
def change_saldo(manager: Manager):
    amount = float(input("Podaj kwotę, którą chcesz dodać lub odjąć z konta"))
    manager.saldo += amount
    manager.history.append(f"Wykonano instrukcję saldo, zasilono {amount}")


@manager.assign("Sprzedaz")
def sell_item(manager: Manager):
    print(manager.magazyn)
    # przyklad dla Piotrka
    # product, amount = tuple(input("Podaj nazwę produktu, który chcesz kupić").replace(" ", "").split(","))
    # amount = float(amount)
    product = input("Podaj nazwę produktu: ")
    # TODO zmienić na floaty bo np kg
    amount = int(input("Podaj ilość, którą chcesz sprzedać: "))
    product_found = False
    # najpierw sprawdzmy czy mamy towar
    for item, item_details in manager.magazyn.items():
        if product == item:
            item_details["ilość"] -= amount
            manager.saldo += (item_details["cena"] * amount)
            product_found = True
            manager.history.append(f"Sprzedano {product} w ilości {amount}")
            break
    if not product_found:
        manager.history.append(f"Nie udało się sprzedać towaru {product}, mamy go za mało na magazynie")


@manager.assign("Historia")
def lookup_for_data(manager: Manager):
    # TODO jak value bedzie wieksze od naszej listy to wyprintować długość listy len()
    value_from = input("Podaj początkowy zakres")
    value_to = input("Podaj końcowy zakres")
    if not value_to and not value_from:
        print(manager.history)
    if value_from and not value_to:
        print(manager. history[value_from:])