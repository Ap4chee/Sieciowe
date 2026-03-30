import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8006))
s.listen(1)
c, a = s.accept()
while True:
    d = c.recv(20)
    if not d: break
    c.send(d)
c.close()
