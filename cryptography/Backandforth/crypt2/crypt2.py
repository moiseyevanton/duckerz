from math import *

print('Enter the messsage: ')
message = input()
output = ''
for i in range(len(message)):
    output += chr(ord(message[i])^i)

print(output, "GLHF")