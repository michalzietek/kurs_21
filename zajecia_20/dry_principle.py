cena_za_kg = 10
ilosc = 0.5
cena_twoich_truskawek = cena_za_kg * ilosc
print(f"Cena truskawek, które kupiłeś to {cena_twoich_truskawek}")
if cena_twoich_truskawek> 50:
    print("nie możesz za to zapłacić")
elif cena_twoich_truskawek < 2:
    print("Twoje truskawki sa chyba nieświeże")