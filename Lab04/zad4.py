import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8003))
while True:
    d, a = s.recvfrom(1024)
    tex = d.decode()
    try:
        wynik = str(eval(tex))
    except:
        wynik = 'blad'
    s.sendto(wynik.encode(), a)
