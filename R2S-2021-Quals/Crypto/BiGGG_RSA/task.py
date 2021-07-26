#!/usr/bin/python3
from Crypto.Util.number import getPrime , bytes_to_long , long_to_bytes
from secret import flag
from gmpy2 import next_prime

n = 1
tmp = getPrime(50)

for i in range(7):
    n *= tmp
    tmp = next_prime(n)

e = 0x10001 
m = bytes_to_long(flag)
c = pow(m , e , n)

with open("output" , "w") as f:
    f.write(f"c = {str(c)}\n")
    f.write(f"e = {str(e)}\n")
    f.write(f"n = {str(n)}\n")

