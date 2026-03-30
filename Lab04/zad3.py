import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8002))
while True:
    d, a = s.recvfrom(1024)
    s.sendto(d, a)
