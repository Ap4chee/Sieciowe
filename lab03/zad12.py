import socket

def wyslij_wszystko(sock, dane):
    wyslano = 0
    while wyslano < len(dane):
        ile = sock.send(dane[wyslano:])
        wyslano = wyslano + ile

def odbierz_wszystko(sock, ile_bajtow):
    dane = b""
    while len(dane) < ile_bajtow:
        paczka = sock.recv(ile_bajtow - len(dane))
        if not paczka:
            break
        dane = dane + paczka
    return dane

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("212.182.24.27", 2908))

wiadomosc = input("Podaj wiadomosc: ")

if len(wiadomosc) < 20:
    wiadomosc = wiadomosc.ljust(20)
elif len(wiadomosc) > 20:
    wiadomosc = wiadomosc[:20]

wyslij_wszystko(s, wiadomosc.encode())

odpowiedz = odbierz_wszystko(s, 20)
print("Odpowiedz:", odpowiedz.decode())

s.close()
