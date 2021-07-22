#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import urandom
from secret import flag
from string import printable

key = urandom(16)
aes = AES.new(key , mode=AES.MODE_ECB)
alpha = printable

with open("alpha" , "wb") as f:
    for i in alpha:
        tmp = aes.encrypt(pad(i.encode() , 16))
        f.write(tmp)

with open("output" , "wb") as f:
    for i in flag:
        tmp = aes.encrypt(pad(i.encode() , 16))
        f.write(tmp)

