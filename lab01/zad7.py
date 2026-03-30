import socket
import sys

adres = sys.argv[1]

print("Skanuje porty dla", adres)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    wynik = s.connect_ex((adres, port))
    if wynik == 0:
        print("Port", port, "jest otwarty")
    s.close()

print("Skanowanie zakonczone")
