#!/usr/bin/python

from string import printable
from Crypto.Util.number import long_to_bytes

alpha = printable[:62] + "!?_{}><"
exec(open("output" , "r").read())

enc = enc[::-1]
rec = dict(zip(alpha , range(69)))

res = 0

for i in range(len(enc)):
    res += pow(69 , i) * rec[enc[i]]

print(long_to_bytes(res))

