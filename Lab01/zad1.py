nazwa = input("Podaj nazwe pliku: ")

plik = open(nazwa, "r")
zawartosc = plik.read()
plik.close()

plik2 = open("lab1zad1.txt", "w")
plik2.write(zawartosc)
plik2.close()

print("Skopiowano")
