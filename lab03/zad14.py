import socket

hex_dane = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
bajty = bytes.fromhex(hex_dane.replace(" ", ""))

port_src = int.from_bytes(bajty[0:2], "big")
port_dst = int.from_bytes(bajty[2:4], "big")

dlugosc_naglowka = (bajty[12] >> 4) * 4
dane = bajty[dlugosc_naglowka:].decode()

print("Port zrodlowy:", port_src)
print("Port docelowy:", port_dst)
print("Dane:", dane)

wiadomosc = "zad13odp;src;" + str(port_src) + ";dst;" + str(port_dst) + ";data;" + dane

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)
s.sendto(wiadomosc.encode(), ("212.182.24.27", 2909))
odpowiedz, adres = s.recvfrom(1024)
print("Serwer:", odpowiedz.decode())
s.close()
