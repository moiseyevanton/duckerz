import base64
from pathlib import Path

base_dir = Path(__file__).resolve().parent

with open(base_dir / "crypt3.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)

text = base64.b64decode(text).decode()
print(text)


text = base64.b32decode(text).decode()
print(text)

flag = ''.join(chr(int(x)) for x in text.split())

print(flag)