#!/usr/bin/python3

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from math import log
from string import printable

def extend(s):
    tmp = sum([ord(s[~i]) * pow(256 , len(s) - i - 1) for i in range(len(s))])
    tmp = pow(tmp , 1 , pow(0x100 , 3))
    key = ""

    for i in range(int(log(tmp , 256)) + 1):
        key += chr(tmp % 256)
        tmp >>= 8

    return key[::-1] + key + key[::-1] + key + key[::-1] + "\x00"


def decrypt(key , data , iv):
    assert len(key) == 16
    blow = Blowfish.new(key=key.encode() , mode=Blowfish.MODE_CBC , iv=iv)
    return blow.decrypt(data)

exec(open("output" , "r").read())
cipher , iv = [bytes.fromhex(i) for i in [cipher , iv]] 

for i in printable:
    for j in printable:
        for k in printable:
            res = decrypt(extend(i + j + k) , cipher , iv)
            if b"SCIST" in res:
                print(res.decode())
                exit()

