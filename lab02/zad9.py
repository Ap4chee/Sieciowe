import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)

adres_ip = input("Podaj adres IP: ")
s.sendto(adres_ip.encode(), ("212.182.24.27", 2906))

odpowiedz, adres = s.recvfrom(1024)
print("Hostname:", odpowiedz.decode())

s.close()
