'''
Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi elementów dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

    Liczbę paczek wysłanych
    Liczbę kilogramów wysłanych
    Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
    Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik


Restrykcje:

    Waga elementów musi być z przedziału od 1 do 10 kg.
    Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
    W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
    W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.


Przykład 1:

    Ilość elementów: 2
    Wagi elementów: 7, 9

Podsumowanie:

    Wysłano 1 paczkę (7+9)
    Wysłano 16 kg
    Suma pustych kilogramów: 4kg
    Najwięcej pustych kilogramów ma paczka 1 (4kg)


Przykład 2:

     Ilość elementów: 6
    Wagi elementów: 3, 6, 5, 8, 2, 3

Podsumowanie:

    Wysłano 2 paczki (3+6+5, 8+2+3)
    Wysłano 27 kg
    Suma pustych kilogramów: 13kg
    Najwięcej pustych kilogramów ma paczka 2 (7kg)


Przykład 3:
 Ilość elementów: 8

    Wagi elementów: 7, 14
     Podsumowanie:
    Wysłano 1 paczkę (7)
    Wysłano 7 kg
    Suma pustych kilogramów: 13kg
    Najwięcej pustych kilogramów ma paczka 13
'''

'''
moja skrocona TODO lista:
na podstawie danych (ilosc paczek, wagi poszczegolnych elementow) podać rozwiązania pytań:

dane początkowe:
- ilość paczek
- wagi poszczególnych elementów - te wagi musimy podawać jedna po drugiej i patrzeć na ograniczenia, które mamy! w takim razie musimy skorzystać z pętli
do tego rozwiązania najlepiej użyć pętli while


Restrykcje:

    Waga elementów musi być z przedziału od 1 do 10 kg.
    Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
    W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana. - tutaj wiemy, że musimy mieć tymczasową wartość wagi paczki
    W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.




WYJSCIE PROGRAMU, CO MUSIMY OBLICZYĆ:
- ilości wysłanych paczek, teoretycznie pasowałoby parcels_amount, ale możemy zakończyć program wcześniej i ta ilość paczek faktycznie wysłanych będzie mniejsza od ilości podanej na początku
- liczby kilogramów wysłanych - odhaczone przez kilograms_sent
- sumy pustych kilogramów - mamy 2 wartosci - parcels_sent i kilograms_sent - robimy formula = parcels_sent * 20(kg) - kilograms_sent
- znalezienia paczki z największą ilością pustych kilogramów i podania tej wagi - w petli oprocz dodawania parcel_weight w momencie
 gdy zakoncze program( wartosc bedzie ponizej 1 lub powyzej 10) to sprawdzam
  czy ilosc wolnego miejsca w paczce jest wieksza od biggest_gap_in_weight i albo to zostawiam albo zmieniam to sprawdzenie zrobimy
   w momencie kiedy mamy nastepna paczke



'''
parcels_amount = input("Podaj ilosc paczek:")
maximum_weight = 20
kilograms_sent = 0
parcel_weight = 0
stop_program = False
parcels_sent = 1
parcel_number = 1
biggest_gap_in_weight = 0
parcel_with_biggest_gap = None
while not stop_program:
    element = float(input("Podaj wagę elementu"))
    if not element in range(10):
        stop_program = True
        #TODO zeby tutaj tez wykonac sprawdzenia wagi paczki i pustych kilogramów
    else:
        if parcel_weight + element > 20:
            if 20 - parcel_weight > biggest_gap_in_weight:
                biggest_gap_in_weight = 20 - parcel_weight
                parcel_with_biggest_gap = parcel_number
                print(parcel_with_biggest_gap)
            if parcel_number == int(parcels_amount):
                print("niestety nie masz juz dostepnych paczek, element został usunięty")
                stop_program = True
                break
            parcel_weight = 0
            parcel_weight += element
            parcel_number += 1
            parcels_sent += 1
            kilograms_sent += element
        else:
            parcel_weight += element
            kilograms_sent += element
        # TODO wykombinowac jak zakoczyc program, kiedy nie chcemy juz podawac kolejnego elementu
        # nie będzie do końca działąło, bo mamy ograniczenie do 20kg - wiec tutaj musicie skorzystać z instrukcji warunkowej if
        # jezeli parcel weight i waga elementu beda wieksze od 20 to tworzymy nowa paczke, zerujemy parcel weight, dodajemy do niej 1 element i zwiekszamy ilosc paczek wyslanych

print(f"Wyslano kilogramow: {kilograms_sent}")
print(f"Ilosc wyslanych paczek: {parcels_sent}")
print(f"Paczka z najmniejsza wagą to: {parcel_with_biggest_gap}, ważyła ona {20 - biggest_gap_in_weight}")
print("Zakonczylismy program")