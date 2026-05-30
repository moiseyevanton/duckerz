import base64
from pathlib import Path

base_dir = Path(__file__).resolve().parent
text = []

with open(base_dir / "polyglot.txt", "r", encoding="utf-8") as file:
    for line in file:
        text.append(line)

for r in text:
    print(r)

flag1 = bytes.fromhex(text[0]).decode()
print(flag1)
print(type(flag1))

flag2 = text[1].encode().decode('unicode_escape').strip()
print(flag2)
print(type(flag2))

flag3 = base64.b64decode(text[2]).decode()
print(flag3)
print(type(flag3))

flag = flag1 + flag2 + flag3
print(flag)

