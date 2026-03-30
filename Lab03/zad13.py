import socket

hex_dane = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
bajty = bytes.fromhex(hex_dane.replace(" ", ""))

port_src = int.from_bytes(bajty[0:2], "big")
port_dst = int.from_bytes(bajty[2:4], "big")
dane = bajty[8:].decode()

print("Port zrodlowy:", port_src)
print("Port docelowy:", port_dst)
print("Dane:", dane)

wiadomosc = "zad14odp;src;" + str(port_src) + ";dst;" + str(port_dst) + ";data;" + dane

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)
s.sendto(wiadomosc.encode(), ("212.182.24.27", 2910))
odpowiedz, adres = s.recvfrom(1024)
print("Serwer:", odpowiedz.decode())
s.close()
