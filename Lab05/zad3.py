import socket
import time

for p in range(600, 700):
    if str(p).endswith('666'):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)
        try:
            s.sendto(b'PING', ('212.182.24.27', p))
            d, a = s.recvfrom(1024)
            if b'PONG' in d:
                print('znalazlem port', p)
                break
        except:
            pass
        s.close()

t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect(('212.182.24.27', 2913))
print(t.recv(1024).decode())
t.close()
