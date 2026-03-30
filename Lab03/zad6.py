import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)

liczba1 = input("Podaj pierwsza liczbe: ")
operator = input("Podaj operator (+, -, *, /): ")
liczba2 = input("Podaj druga liczbe: ")

wiadomosc = liczba1 + " " + operator + " " + liczba2
s.sendto(wiadomosc.encode(), ("212.182.24.27", 2902))

odpowiedz, adres = s.recvfrom(1024)
print("Wynik:", odpowiedz.decode())

s.close()
