import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 4444))
s.listen(1)
c, a = s.accept()
wylosowana = random.randint(1, 100)
while True:
    try:
        d = c.recv(1024)
        L = int(d.decode())
        if L > wylosowana:
            c.send(b'mniej')
        elif L < wylosowana:
            c.send(b'wiecej')
        else:
            c.send(b'zgadles')
            break
    except:
        c.send(b'to nie liczba')
c.close()
s.close()
