import socket
import base64
s = socket.socket()
s.connect(('poczta.interia.pl', 587))
s.recv(1024)
s.send(b'EHLO x\r\n')
s.recv(1024)
s.send(b'AUTH LOGIN\r\n')
s.recv(1024)
s.send(base64.b64encode(b'pas2017@interia.pl') + b'\r\n')
s.recv(1024)
s.send(base64.b64encode(b'P4SInf2017') + b'\r\n')
s.recv(1024)
s.send(b'MAIL FROM: <pas2017@interia.pl>\r\n')
s.recv(1024)
s.send(b'RCPT TO: <pas2017@interia.pl>\r\n')
s.recv(1024)
s.send(b'DATA\r\n')
s.recv(1024)

msg = (
    'MIME-Version: 1.0\r\n'
    'Content-Type: text/html\r\n\r\n'
    '<b>pogrubienie</b> <i>pochylenie</i> <u>podkreslenie</u>\r\n.\r\n'
)
s.send(msg.encode())
s.recv(1024)
s.send(b'QUIT\r\n')
