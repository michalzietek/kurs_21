from enum import Enum

class WyborKomendy(Enum):
    ZMIEN_SALDO = "1"
    SPRZEDAZ = "2"
    ZAKUP = "3"
    KONTO = "4"
    LISTA = "5"
    MAGAZYN = "6"
    PRZEGLAD = "7"
    KONIEC = "8"