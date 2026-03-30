import socket

adres = input("Podaj adres IP: ")

try:
    socket.inet_aton(adres)
    print("Adres IP jest poprawny")
except socket.error:
    print("Adres IP jest niepoprawny")
