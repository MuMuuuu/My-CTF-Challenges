#!/usr/bin/python

exec(open("./output" , "r").read())

flag = ""

for i in range(len(n)):
    for char in range(20 , 128):
        if pow(char , e , n[i]) == c[i]:
            flag += chr(char)
            break

print("R2S" + flag[::-1])

