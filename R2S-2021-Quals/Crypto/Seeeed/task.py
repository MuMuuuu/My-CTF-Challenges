#!/usr/bin/python3

from random import *
from Crypto.Util.number import getPrime , bytes_to_long
from secret import flag
from time import time
from gmpy2 import next_prime

m = bytes_to_long(flag)
e = 0x10001
N = 1083431725045970484586186177942248908050424478782004838696639
t = int(time())
seed(t)

def seeed(t , tmp):
    if t == 0:
        return tmp
    
    tmp = randint(1e10 , 1e20)
    seed(tmp)

    return seeed(t - 1 , tmp)

def encrypt(n , m , e):
    c = pow(m , e , n)

    return c

m = pow(m , 1 , pow(0x100 , len(flag) - 3))
get = lambda b : (m & (255 << (8 * b))) >> (8 * b)

p_ls = [int(next_prime(N // seeed(i , t - i))) for i in range(m.bit_length() // 8 + 1)]
q_ls = [getPrime(i.bit_length())  for i in p_ls]
n_ls = [q_ls[i] * p_ls[i] for i in range(len(q_ls))]
c_ls = [encrypt(n_ls[i] , get(i) , e) for i in range(len(n_ls))]

with open("output" , "w") as f:
    f.write("n = {}\n".format(n_ls))
    f.write("c = {}\n".format(c_ls))
    f.write("e = {}\n".format(e))

