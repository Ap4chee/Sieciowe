import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)

wiadomosc = input("Podaj wiadomosc: ")
s.sendto(wiadomosc.encode(), ("212.182.24.27", 2901))

odpowiedz, adres = s.recvfrom(1024)
print("Odpowiedz:", odpowiedz.decode())

s.close()
