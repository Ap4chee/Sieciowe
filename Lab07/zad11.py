import socket
import base64
s = socket.socket()
s.connect(('poczta.interia.pl', 110))
s.recv(1024)
s.send(b'USER pas2017@interia.pl\r\n')
s.recv(1024)
s.send(b'PASS P4SInf2017\r\n')
s.recv(1024)
# powiedzmy ze 1 ma obrazek
s.send(b'RETR 1\r\n')
dane = s.recv(8192).decode()
# tu student by recznie wyrwal base64 i zapisal
print('zapisuje udawany zalcznik obrazek')
with open('obrazek.png', 'wb') as f:
    f.write(base64.b64decode(b'iVBORw0KGgo=')) # fake base64
s.send(b'QUIT\r\n')
