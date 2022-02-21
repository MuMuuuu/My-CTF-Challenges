#!/usr/bin/python3

from secret import flag , key
from string import ascii_lowercase as digits , ascii_uppercase as lowercase , digits as uppercase

def caesar_enc(data , key , alpha):
    data = "".join([alpha[(alpha.index(data[i]) + len(alpha) + alpha.index(key[i % len(key)])) % len(alpha)] for i in range(len(data))])
    return data

alpha = lowercase + uppercase + digits + "{_?.}"
flag = caesar_enc(flag , key , alpha)
assert len(key) == 8

with open("output" , "w") as f:
    f.write(f"flag = '{flag}'\n")

