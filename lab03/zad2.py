import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.24.27", 2900))

wiadomosc = input("Podaj wiadomosc: ")
s.send(wiadomosc.encode())

odpowiedz = s.recv(1024)
print("Odpowiedz:", odpowiedz.decode())

s.close()
