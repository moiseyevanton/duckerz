from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

FLAG = bytes_to_long(flag)

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 2**16 + 1
ct = pow(FLAG, e, n)

print(f'n: {n}')
print(f'e: {e + p}')
print(f'ct: {ct}') 
