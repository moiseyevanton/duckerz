from math import *

flag = b'\x1c-\x1b#\x1d*2S(\x0c\n\nO\x08J<7\x1bJ\x0c\x1bC=\x1c7/\t\x0f@7\x1b\x0c\x1d\r\x0cJU'
print('[*] Hello this is simple cipher program. Enter the message: ')
message = str(input())
if message == "Give me flag":
    print("[*] where 'please'?")
elif message == "Give me flag please":
    print("[*] None. GLHF")

key = ord(message[len(message)-1])
list_output = []
flag_ouput = []
for i in range(0, len(message)):
    list_output.append(chr(ord(message[i])+key))
for i in range(0, len(flag)):
        flag_ouput.append(chr(flag[i]+key))

str_ouput = ''.join(list_output)
str_flag = ''.join(flag_ouput)

print('[*] This is your cipher text: ', str_ouput.encode())
print('[*] This is flag output: ', str_flag)