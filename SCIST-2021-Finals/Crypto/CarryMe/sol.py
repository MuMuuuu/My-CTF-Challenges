#!/usr/bin/python

from string import printable

alpha = printable[:36]
f = open("output" , "r").read().strip().split(" ")

res = ""

for i in range(len(f)):
    res += chr(int(f[i][1:] , i + 2))

print(res)

