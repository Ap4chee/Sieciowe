import socket
import time
t1 = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5555))
s.send(b'x')
s.recv(1024)
s.close()
t2 = time.time()
print('tcp: ', t2-t1)

t1 = time.time()
su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
su.sendto(b'x', ('127.0.0.1', 5556))
su.recvfrom(1024)
t2 = time.time()
print('udp: ', t2-t1)
print('udp jest krotszy bo bez polaczenia')
