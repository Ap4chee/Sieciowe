import socket
s = socket.socket()
s.connect(('poczta.interia.pl', 110))
s.recv(1024)
s.send(b'USER pas2017@interia.pl\r\n')
s.recv(1024)
s.send(b'PASS P4SInf2017\r\n')
s.recv(1024)
s.send(b'LIST\r\n')
lista = s.recv(2048).decode().split('\r\n')
for l in lista:
    if ' ' in l and l.split(' ')[0].isdigit():
        num, roz = l.split(' ')
        print('wiadomosc: ', num, ' rozmair: ', roz)
s.send(b'QUIT\r\n')
