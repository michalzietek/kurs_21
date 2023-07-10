import csv
import re


with open("nations.csv", mode="r+") as file:
    for line in file:
        #print(line)
        #print(type(line))
        pass

    writer = csv.writer(file)
    writer.writerow([1, 2, 3, 4, 5, 6, 7, 8])

mail = "Dzien dobry, " \
       "dafadddfd fsfcgstfwrvgrgvt fst rwtvrcg vfsgvrwtfcwras cvswrvtcr fsag fsvas  gr g " \
       "michalzietkowski@gmail.com"

pattern = r'(\w+)@\w+.(com|pl)$'

result = re.search(pattern, mail)
username = result.group(1)
print(username)
print(result.group())


print(result)

phone = input("Podaj swoj numer telefonu z kierunkowym z plusem")
telephone_pattern = r'^\+\d{11}$'

phone_result = re.search(telephone_pattern, phone)
if phone_result:
    print("Gratulacje podałeś dobry numer")
else:
    print("Niestety twój numer jest niepoprawny")
