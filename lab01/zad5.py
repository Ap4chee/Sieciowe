import socket
import sys

hostname = sys.argv[1]

try:
    adres = socket.gethostbyname(hostname)
    print("Adres IP:", adres)
except socket.gaierror:
    print("Nie znaleziono adresu IP dla tego hostname")
