import socket

hex_dane = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
bajty = bytes.fromhex(hex_dane.replace(" ", ""))

wersja = bajty[0] >> 4
ihl = (bajty[0] & 0x0F) * 4
protokol = bajty[9]
src_ip = str(bajty[12]) + "." + str(bajty[13]) + "." + str(bajty[14]) + "." + str(bajty[15])
dst_ip = str(bajty[16]) + "." + str(bajty[17]) + "." + str(bajty[18]) + "." + str(bajty[19])

print("Wersja:", wersja)
print("IP zrodlowe:", src_ip)
print("IP docelowe:", dst_ip)
print("Protokol:", protokol)

tcp_start = ihl
port_src = int.from_bytes(bajty[tcp_start:tcp_start+2], "big")
port_dst = int.from_bytes(bajty[tcp_start+2:tcp_start+4], "big")
tcp_header_len = (bajty[tcp_start+12] >> 4) * 4
dane = bajty[tcp_start + tcp_header_len:].decode()

print("Port zrodlowy:", port_src)
print("Port docelowy:", port_dst)
print("Dane:", dane)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)

msg1 = "zad15odpA;ver;" + str(wersja) + ";srcip;" + src_ip + ";dstip;" + dst_ip + ";type;" + str(protokol)
s.sendto(msg1.encode(), ("212.182.24.27", 2911))
odp1, adres = s.recvfrom(1024)
print("Serwer czesc A:", odp1.decode())

if "TAK" in odp1.decode():
    msg2 = "zad15odpB;srcport;" + str(port_src) + ";dstport;" + str(port_dst) + ";data;" + dane
    s.sendto(msg2.encode(), ("212.182.24.27", 2911))
    odp2, adres = s.recvfrom(1024)
    print("Serwer czesc B:", odp2.decode())

s.close()
