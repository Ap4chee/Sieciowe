import socket
import ssl

ctx = ssl.create_default_context()
try:
    s = socket.create_connection(('212.182.24.27', 993))
    s = ctx.wrap_socket(s, server_hostname='212.182.24.27')
    s.recv(1024)
    s.send(b'A1 LOGIN pasinf@infumcs.edu P4SInf2017\r\n')
    s.recv(1024)
    s.send(b'A2 SELECT Inbox\r\n')
    s.recv(1024)
    s.send(b'A3 SEARCH UNSEEN\r\n')
    odp = s.recv(1024).decode()
    print("Szukam nieprzeczytanych:")
    print(odp)
    s.send(b'A4 STORE 1 +FLAGS (\\Seen)\r\n')
    print("Ustawiono flage na 1")
    s.send(b'A5 LOGOUT\r\n')
except:
    print('brak polaczenia')
