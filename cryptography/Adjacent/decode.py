from pathlib import Path

base_dir = Path(__file__).resolve().parent

with open(base_dir / "Contiguous" / "res.txt", "r", encoding="utf-8") as file:
    text = file.read()

decode = ""

a = 7
b = 20
a_inv = 15  # обратное к 7 по модулю 26

for char in text:
    if char.isalpha():
        if char.islower():
            enc = ord(char) - ord('a')
            dec = (a_inv * (enc - b)) % 26
            decode += chr(dec + ord('a'))
        else:
            enc = ord(char) - ord('A')
            dec = (a_inv * (enc - b)) % 26
            decode += chr(dec + ord('A'))
    else:
        decode += char

print(decode)
