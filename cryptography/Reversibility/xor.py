from pathlib import Path

base_dir = Path(__file__).resolve().parent
name_list = []
value_list = []

def xor(a, b):
    return bytes(
        x ^ y
        for x, y in zip(a, b)
    )

with open(base_dir / "reversibility.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, value = line.strip().split(": ")
        name_list.append(name)
        value_list.append(value)

print(name_list)
print(value_list)

key1 = bytes.fromhex(value_list[0])

key1_xor_key2 = bytes.fromhex(value_list[1])

key2_xor_key3 = bytes.fromhex(value_list[2])

flag_xor_key1_xor_key3_xor_key2 = bytes.fromhex(value_list[3]) 

flag_xor_key3_xor_key2 = xor(flag_xor_key1_xor_key3_xor_key2, key1)

flag = xor(flag_xor_key3_xor_key2, key2_xor_key3)

print(flag)
