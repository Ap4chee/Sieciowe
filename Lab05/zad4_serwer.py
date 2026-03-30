import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5555))
s.listen(1)
c, a = s.accept()
c.recv(1024)
c.send(b'ok')
c.close()
s.close()

su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
su.bind(('127.0.0.1', 5556))
d, a = su.recvfrom(1024)
su.sendto(b'ok', a)
su.close()
