import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8110))
s.listen(1)
c, a = s.accept()
c.send(b'+OK hej\r\n')
while True:
    d = c.recv(1024).decode()
    if 'USER' in d or 'PASS' in d:
        c.send(b'+OK super\r\n')
    elif 'STAT' in d:
        c.send(b'+OK 1 100\r\n')
    elif 'QUIT' in d:
        c.send(b'+OK hejka\r\n')
        break
    else:
        c.send(b'-ERR nic\r\n')
c.close()
