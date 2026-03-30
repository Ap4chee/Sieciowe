import socket
import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen(1)
while True:
    c, a = s.accept()
    x = c.recv(1024)
    d = str(datetime.datetime.now())
    c.send(d.encode())
    c.close()
