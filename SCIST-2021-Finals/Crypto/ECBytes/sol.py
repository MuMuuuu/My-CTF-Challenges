#!/usr/bin/python

from string import printable
from Crypto.Util.Padding import unpad

def split(s):
    return [s[i : i + 16] for i in range(0 , len(s) , 16)]

alpha = open("alpha" , "r").read().strip()
alpha = split(alpha)

dic = dict(zip(alpha , printable))

out = open("output" , "r").read().strip()
out = split(out)

res = ""

for i in out:
    res += dic[i]

print(res)

