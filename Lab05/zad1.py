import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('212.182.24.27', 2912))
while True:
    a = input('Podaj liczbe: ')
    s.send(a.encode())
    odp = s.recv(1024).decode()
    print(odp)
    if 'zgadles' in odp.lower() or 'wygrana' in odp.lower(): 
        break
s.close()
