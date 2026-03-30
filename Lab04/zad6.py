import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8005))
while True:
    d, a = s.recvfrom(1024)
    host = d.decode().strip()
    try:
        ip = socket.gethostbyname(host)
    except:
        ip = 'nie wiem'
    s.sendto(ip.encode(), a)
