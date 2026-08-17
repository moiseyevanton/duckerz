import ast

with open("crypt2/output") as f:
    data = f.read().strip()

data = ast.literal_eval(data)    # b'...' -> реальные байты

flag = ''
for i in range(len(data)):
    flag += chr(data[i] ^ i)

print(flag)
