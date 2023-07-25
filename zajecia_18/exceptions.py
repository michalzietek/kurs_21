wiek = input("Podaj mi swoj wiek ")
try:
    print(f"Twoj wiek to {int(wiek)}")
except (ValueError, ArithmeticError):
    print("Przepraszam musisz podać swój wiek jako cyfrę")
except AttributeError:
    print("inny atrybut")
finally:
    print("Wywolalem finalna instrukcje")
