#!/usr/bin/python

from string import printable
from Crypto.Util.number import bytes_to_long

alpha = printable[:62] + "!?_{}><"
flag = "SCIST{BasE58???_WhY_n07_us1ng_Base69}"
m = bytes_to_long(flag)

dic = dict(zip(range(69) , alpha))

res = []
while m > 69:
    res.append(m % 69)
    m //= 69
res.append(m)

enc = "".join([dic[i] for i in res])[::-1]

with open("output" , "w") as f:
    f.write("alpha = '{}'\n".format(alpha))
    f.write("enc = '{}'".format(enc))

