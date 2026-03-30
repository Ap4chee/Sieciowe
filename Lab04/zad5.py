import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8004))
while True:
    d, a = s.recvfrom(1024)
    ip = d.decode().strip()
    try:
        h = socket.gethostbyaddr(ip)[0]
    except:
        h = 'nie wiem'
    s.sendto(h.encode(), a)
