import socket
import base64
s = socket.socket()
s.connect(('poczta.interia.pl', 587))
s.recv(1024)
s.send(b'EHLO ggg\r\n')
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

plik = base64.b64encode(b'jakis tekst w pliku').decode()
msg = (
    'MIME-Version: 1.0\r\n'
    'Content-Type: multipart/mixed; boundary=sep\r\n\r\n'
    '--sep\r\n'
    'czesc to mail z pikiem\r\n'
    '--sep\r\n'
    'Content-Type: text/plain; name="plik.txt"\r\n'
    'Content-Transfer-Encoding: base64\r\n'
    'Content-Disposition: attachment; filename="plik.txt"\r\n\r\n'
    f'{plik}\r\n'
    '--sep--\r\n.\r\n'
)
s.send(msg.encode())
s.recv(1024)
s.send(b'QUIT\r\n')
s.recv(1024)
