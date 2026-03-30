import socket
import sys

adres = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect((adres, port))
    try:
        usluga = socket.getservbyport(port, "tcp")
    except OSError:
        usluga = "nieznana"
    print("Port", port, "jest otwarty -", usluga)
except socket.error:
    print("Port", port, "jest zamkniety")
finally:
    s.close()
