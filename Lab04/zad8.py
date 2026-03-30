import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8007))
s.listen(1)
c, a = s.accept()
wymagane = 20
while True:
    d = c.recv(wymagane)
    if len(d) == wymagane:
        c.send(b'odebralem cale 20')
        break
c.close()
