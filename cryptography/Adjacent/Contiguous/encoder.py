
# from secret import FLAG
FLAG = 'DUCKERZ'
cp = ""
a = 7
b = 20

for letter in FLAG:
    if letter.isalpha(): # проверка на наличие буквы, если есть то вернет true
        if letter.islower(): # провера что буква не заглавная, если так то true 
            tmp = ord(letter) - ord('a') # ord переводит символ в его силовое значение 
            enc = (a * tmp + b) % 26 
            cp += chr(enc + ord('a'))     
        else:
            tmp = ord(letter) - ord('A')
            enc = (a * tmp + b) % 26
            cp += chr(enc + ord('A'))
    else:
        cp += letter

with open('res.txt', 'w') as file:
    file.write(cp)
