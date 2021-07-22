#!/usr/bin/python

from Crypto.Cipher import Blowfish
from Crypto.Util.Counter import new
from Crypto.Util.number import bytes_to_long
from random import randint
from os import urandom
from secret import flag

key = urandom(4)
iv = urandom(8)
xor = lambda a , b : "".join([chr(ord(i) ^ ord(j)) for i , j in zip(a , b)])

def change_type(i):
    if type(i) == str:
        return int(i.encode("hex") , 16)
    elif type(i) in (int , long):
        return (["0" , ""][len(hex(long(i))) % 2] + hex(long(i))[2:-1]).decode("hex")

def slice(flag):
    leng = len(flag) // 2
    return [flag[:leng] , flag[leng:]]

def encrypt(s , key=key):
    ctr = new(16 , initial_value=change_type(iv)) 
    blow = Blowfish.new(key , mode=Blowfish.MODE_CTR , counter=ctr)

    return blow.encrypt(s)

def miller_robin(n , k=20):
    if n == 2:
        return True
    elif not (n % 2 and n % 3 and n % 5):
        return False
    
    d = n - 1
    r = 0
    while ~d & 1:
        r += 1
        d >>= 1

    for i in range(k):
        a = randint(2 , n - 2)
        x = pow(a , d , n)

        if x == 1 or x == n - 1:
            continue
        else:
            for j in range(r - 1):
                x = pow(x , 2 , n)
                if x == n - 1:
                    break
            else:
                return False
    return True

def gen(bits):
    while 1:
        tmp = urandom(bits // 8)
        if miller_robin(change_type(tmp)):
            return change_type(tmp)

if __name__ == "__main__":
    p = gen(400)
    q = gen(400)
    n = p * q
    e = 0x10001

    x = xor(encrypt(change_type(p)) , encrypt(change_type(q)))
    f1 , f2 = slice(flag)
    c = pow(change_type(f1) , e , n)
    
    c2 = xor(encrypt(f2) , encrypt(f1))

    with open("output" , "w") as f:
        f.write("n = {}\n".format(n))
        f.write("e = {}\n".format(e))
        f.write("c = {}\n".format(c))
        f.write("x = {}\n".format(change_type(x)))
        f.write("iv = '{}'\n".format(iv.encode("hex")))
        f.write("c2 = '{}'\n".format(c2.encode("hex")))        

