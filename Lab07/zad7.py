import socket
s = socket.socket()
s.connect(('poczta.interia.pl', 110))
s.recv(1024)
s.send(b'USER pas2017@interia.pl\r\n')
s.recv(1024)
s.send(b'PASS P4SInf2017\r\n')
s.recv(1024)
s.send(b'STAT\r\n')
o = s.recv(1024).decode().split(' ')
if len(o) > 2:
    print('bajty:', o[2])
s.send(b'QUIT\r\n')
