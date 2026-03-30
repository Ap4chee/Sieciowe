import socket
import ssl
ctx = ssl.create_default_context()
try:
    s = socket.create_connection(('212.182.24.27', 993))
    s = ctx.wrap_socket(s, server_hostname='212.182.24.27')
    print(s.recv(1024))
    s.send(b'A1 LOGIN pasinf@infumcs.edu P4SInf2017\r\n')
    print(s.recv(1024))
    s.send(b'A2 STATUS Inbox (MESSAGES)\r\n')
    print(s.recv(1024))
    s.send(b'A3 LOGOUT\r\n')
    print(s.recv(1024))
except:
    print('serwer na 212.182.24.27 odrzuca polaczenie')
