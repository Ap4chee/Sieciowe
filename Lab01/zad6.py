import socket
import sys

adres = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect((adres, port))
    print("Polaczono z", adres, "na porcie", port)
except socket.error:
    print("Nie udalo sie polaczyc z", adres, "na porcie", port)
finally:
    s.close()
