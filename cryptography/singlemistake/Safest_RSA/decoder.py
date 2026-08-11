vals = {}
for line in open('out.txt'):
    if ':' in line:
        k, v = line.split(':', 1)
        vals[k.strip()] = int(v.strip())
n, esump, ct = vals['n'], vals['e'], vals['ct']

# print(n)
# print(leaked) - e + p , где e = 65537, p - простое число
e = 65537
p = esump - e
q = n // p
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi) 
m = pow(ct, d, n)  
# print(ct)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big'))