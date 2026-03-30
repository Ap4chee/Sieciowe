import socket
s = socket.socket()
s.connect(('poczta.interia.pl', 110))
s.recv(1024)
s.send(b'USER pas2017@interia.pl\r\n')
s.recv(1024)
s.send(b'PASS P4SInf2017\r\n')
s.recv(1024)

s.send(b'LIST\r\n')
lista = s.recv(4096).decode().split('\r\n')
max_r = 0
max_id = -1
for l in lista:
    if ' ' in l and l.split(' ')[0].isdigit():
        num, roz = l.split(' ')
        if int(roz) > max_r:
            max_r = int(roz)
            max_id = int(num)
print('najweikszy to', max_id)
if max_id > 0:
    s.send(f'RETR {max_id}\r\n'.encode())
    print(s.recv(4096).decode())
s.send(b'QUIT\r\n')
