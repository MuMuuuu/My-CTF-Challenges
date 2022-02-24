#!/usr/bin/python3

from secret import flag , key , iv
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from math import log

def extend(s):
    tmp = sum([ord(s[~i]) * pow(256 , len(s) - i - 1) for i in range(len(s))])
    tmp = pow(tmp , 1 , pow(0x100 , 3))
    key = ""

    for i in range(int(log(tmp , 256)) + 1):
        key += chr(tmp % 256)
        tmp >>= 8

    return key[::-1] + key + key[::-1] + key + key[::-1] + "\x00"


def encrypt(key , data , iv):
    assert len(key) == 16
    blow = Blowfish.new(key=key.encode() , mode=Blowfish.MODE_CBC , iv=iv)
    return blow.encrypt(data)

cipher = encrypt(extend(key) , pad(flag , 16) , iv)
iv , cipher = [i.hex() for i in [iv , cipher]]

with open("output" , "w") as f:
    f.write(f"cipher = {cipher}\n")
    f.write(f"iv = {iv}\n")
