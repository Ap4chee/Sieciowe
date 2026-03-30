nazwa = input("Podaj nazwe pliku graficznego: ")

plik = open(nazwa, "rb")
dane = plik.read()
plik.close()

plik2 = open("lab1zad1.png", "wb")
plik2.write(dane)
plik2.close()

print("Skopiowano")
