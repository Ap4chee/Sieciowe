import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 587))
s.listen(1)
c, a = s.accept()
c.send(b'220 elo\r\n')
while True:
    d = c.recv(1024).decode()
    if 'EHLO' in d or 'HELO' in d:
        c.send(b'250 ok\r\n')
    elif 'MAIL' in d or 'RCPT' in d:
        c.send(b'250 ok\r\n')
    elif 'DATA' in d:
        c.send(b'354 dawaj\r\n')
    elif '\r\n.\r\n' in d:
        c.send(b'250 git\r\n')
    elif 'QUIT' in d:
        c.send(b'221 nara\r\n')
        break
    else:
        c.send(b'500 zle\r\n')
c.close()
