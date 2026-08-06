import string

def rot13(text):
    result = []
    for i in text:
        char = i - 13
        if char < 32:
            char += 95
        result.append(chr(char))

    return "".join(result)


def rot131(text):
    result = []
    for i in text:
        n = ord(i) + 13
        if n > 126:
            n -= 95
        result.append(n)

    return result


def atbash(text):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(alphabet + string.digits + string.punctuation, reversed_alphabet + string.digits[::-1] + string.punctuation[::-1])
    return text.translate(table)


def to_hex(text):
    result = []
    for i in text:
        result.append(hex(ord(i)))

    return result


def xor(text):
    result = []
    for i in text:
        result.append(int(i, 16) ^ 8)

    return result


def xor1(text):
    result = []
    for i in text:
        result.append(int(i) ^ 8)

    return result


def reverse_text(text):
    return text[::-1]


def to_binary(text):
    result = []
    for i in text:
        result.append(bin(ord(i))[2:].zfill(8))

    return " ".join(result)


# text = input()
# print(to_binary(atbash(reverse_text(rot13(xor(to_hex(text)))))))

# okay decompiling __pycache__/easy_reverse.cpython-38.pyc

print(xor1(rot131(reverse_text((atbash("S[=9N=J=Nqb?q@7PWN'Uvn+3-k,"))))))

nums = [68, 85, 67, 75, 69, 82, 90, 123, 99, 114, 121, 112, 55, 48, 95, 49, 110, 95, 114, 51, 118, 51, 114, 53, 51, 63, 125]
print(''.join(chr(n) for n in nums))
