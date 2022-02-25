#!/usr/bin/python3

from Crypto.Util.number import long_to_bytes , GCD , inverse
from string import printable
from itertools import combinations 

flag = b"SC"
exec(open("output" , "r").read())

res = []
factor = []
for i in combinations(n_list , 2):
     tmp = GCD(i[0] , i[1])
     if tmp != 1 and tmp not in factor:
        factor.append(tmp)

for n , c in zip(n_list , c_list):
    for p in factor:
        if n % p == 0:
            q = n // p
            phi = (p - 1) * (q - 1)
            res.append([c , inverse(e , phi) , n])
            break

while 1:
    for i in res:
        m = long_to_bytes(pow(*i))

        if m[:2] == flag[-2:]:
            flag += chr(m[-1]).encode()
            print(flag)
            del res[res.index(i)]
    if len(flag) == 36:
        print(flag)
        break

