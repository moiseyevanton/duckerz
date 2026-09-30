with open("warmup", "rb") as f:
    data = f.read()

enc = data[0x2010:0x2010+32]   # твой срез
enc = enc.rstrip(b"\x00")      # убрать нули в конце

ror3 = lambda x: ((x >> 3) | (x << 5)) & 0xFF
flag = bytes(ror3(b) for b in enc).decode()
print(flag)