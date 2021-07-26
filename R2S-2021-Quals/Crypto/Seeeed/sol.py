#!/usr/bin/python3

from random import *
from Crypto.Util.number import long_to_bytes , inverse
from gmpy2 import next_prime
from time import time

t = int(time())
N = 1083431725045970484586186177942248908050424478782004838696639

exec(open("./output" , "r").read())

def seeed(t , tmp):
    if t == 0:
        return tmp
    
    tmp = randint(1e10 , 1e20)
    seed(tmp)

    return seeed(t - 1, tmp)

def decrypt(p , q , e , c):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e , phi)

    try:
        return chr(pow(c , d , n))
    except:
        return "?"

while(1):
    t -= 1
    seed(t)

    p1 = next_prime(N // t)
    q1 = n[0] // p1

    if decrypt(p1 , q1 , e , c[0]) == "}":
        break

seed(t)
p_ls = [int(next_prime(N // seeed(_ , t - _))) for _ in range(len(n))]
q_ls = [n[i] // p_ls[i] for i in range(len(n))]

flag = "R2S" + "".join([decrypt(p_ls[i] , q_ls[i] , e , c[i]) for i in range(len(n))])[::-1]

print(flag)
