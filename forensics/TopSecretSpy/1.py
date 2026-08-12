import subprocess

# запускаем tshark, забираем stdout как текст
out = subprocess.run(
    ["tshark", "-r", "DeepIpSpy.pcap",
     "-T", "fields", "-e", "udp.srcport", "-e", "udp.dstport"],
    capture_output=True, text=True, check=True
).stdout

# парсим в список кортежей (src, dst)
pairs = []
for line in out.splitlines():
    if not line.strip():
        continue
    src, dst = line.split("\t")        # tshark разделяет поля табом
    pairs.append((int(src), int(dst)))

# сортируем по src port (это индекс символа)
pairs.sort(key=lambda t: t[0])

flag = ""

for src, dst in pairs:
    dst_m = dst + 68
    sim = 32768 - dst
    flag += chr(sim)
    print(f"{src} -> {sim} -> {chr(sim)}")

print(flag)    

