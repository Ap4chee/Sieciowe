import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)

hostname = input("Podaj hostname: ")
s.sendto(hostname.encode(), ("212.182.24.27", 2907))

odpowiedz, adres = s.recvfrom(1024)
print("Adres IP:", odpowiedz.decode())

s.close()
