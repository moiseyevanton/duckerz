def create_list(code: str) -> list:
    if not code:
        return codel
    
    tmp = code[0:3]
    if int(tmp) >= 128:
        codel.append(int(tmp[:2]))
        code = code[2:]
        return create_list(code)
    else:
        codel.append(int(tmp))
        code = code[3:]
        return create_list(code)

    
t = "90759385917668101124114107451064646106426547436542114109466512711265113110441194611299"
codel = []

codel = create_list(t)
flag = "".join(chr(i ^ 30) for i in codel)

print(flag)
