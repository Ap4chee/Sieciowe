import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.24.27", 2908))

wiadomosc = input("Podaj wiadomosc: ")

if len(wiadomosc) < 20:
    wiadomosc = wiadomosc.ljust(20)
elif len(wiadomosc) > 20:
    wiadomosc = wiadomosc[:20]

s.send(wiadomosc.encode())

odpowiedz = s.recv(20)
print("Odpowiedz:", odpowiedz.decode())

s.close()
