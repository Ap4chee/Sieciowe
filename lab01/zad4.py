import socket
import sys

adres = sys.argv[1]

try:
    nazwa = socket.gethostbyaddr(adres)
    print("Hostname:", nazwa[0])
except socket.herror:
    print("Nie znaleziono hostname dla tego adresu")
