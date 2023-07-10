from polecenia.obliczenia_podatkowe import oblicz_moj_vat, oblicz_moj_podatek
from zaglebione_polecenia.polecenia2.obliczenia_zaglebione_kaloryczne import oblicz_moje_zapotrzebowanie_kaloryczne
from timer_context_manager import Timer
import datetime

print(oblicz_moje_zapotrzebowanie_kaloryczne(80, 1.80))
print(oblicz_moj_podatek(150000))
print(oblicz_moj_vat(1000, 0.23))

pogoda = open("dane_pogodowe.txt")
pogoda.readline()

with Timer():
    print("Zobaczcie co mam najpierw")

with open("dane_pogodowe.txt", mode="r+") as pogoda1:
    pogoda1.write("\nGdańsk, 26.06.2023, Nie padało")
    for line in pogoda1:
        print(line)

with open("responses.xlsx", encoding="utf-8") as excel_file:
    for line in excel_file:
        print(line)


print(datetime.datetime.now() + datetime.timedelta(minutes=15))
