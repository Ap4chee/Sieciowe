import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8010))
while True:
    d, a = s.recvfrom(1024)
    t = d.decode()
    if 'TAK' in t:
        s.sendto(b'TAK', a)
    elif 'NIE' in t:
        s.sendto(b'NIE', a)
    else:
        s.sendto(b'BAD SYNTAX', a)
