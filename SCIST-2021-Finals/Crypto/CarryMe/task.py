#!/usr/bin/python2

from secret import flag
from string import printable

alpha = printable[:36]

def carry(mod , n):
    res = ""
    while n:
        res += alpha[n % mod]
        n //= mod

    return res[::-1]

res = []
for i in range(2 , len(alpha)):
    res.append("{}{}".format(alpha[i] , carry(i , ord(flag[i - 2]))))

with open("output" , "w") as f:
    f.write(" ".join(res))

