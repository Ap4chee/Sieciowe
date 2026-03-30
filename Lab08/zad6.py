import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8143))
s.listen(1)
c, a = s.accept()
c.send(b'* OK witam\r\n')
while True:
    d = c.recv(1024).decode()
    if not d:
        break
    tag = d.split(' ')[0]
    if 'LOGIN' in d:
        c.send((tag + ' OK siema\r\n').encode())
    elif 'LOGOUT' in d:
        c.send(b'* BYE no to papa\r\n' + (tag + ' OK\r\n').encode())
        break
    else:
        c.send((tag + ' BAD nie umiem\r\n').encode())
c.close()
