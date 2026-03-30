import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
s.connect(("ntp.task.gda.pl", 13))
dane = s.recv(1024)
print(dane.decode())
s.close()
