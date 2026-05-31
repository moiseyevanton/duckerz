ciphertext1 = bytes.fromhex(
    "1d70170afcb2dc4c93f2f869d87ccd2b6fbaf52e07e6c3b13d2f41bf98"
)

ciphertext2 = bytes.fromhex(
    "1c483633d883ef599ae2d3738e29d47749f1a93178bbc88f001578f082"
)

plaintext1 = b"Embracing the joy of learning"

# Восстанавливаем ключ
key = bytes(c ^ p for c, p in zip(ciphertext1, plaintext1))

# Расшифровываем второе сообщение
plaintext2 = bytes(c ^ k for c, k in zip(ciphertext2, key))

print(plaintext2.decode())