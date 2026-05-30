from pathlib import Path

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

base_dir = Path(__file__).resolve().parent

with open(base_dir / "crypt1.txt", "r", encoding="utf-8") as file:
    text = file.read()

result = ""

for char in text:
    if char in alphabet_lower:
        index = alphabet_lower.index(char)
        new_index = (index - 15) % 26
        result += alphabet_lower[new_index]

    elif char in alphabet_upper:
        index = alphabet_upper.index(char)
        new_index = (index - 15) % 26
        result += alphabet_upper[new_index]

    else:
        result += char

print(result)