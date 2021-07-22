#!/usr/bin/python

from pwn import xor
from Crypto.Util.number import *

# Reference https://github.com/sliedes/xor_factor

# extend bits
def extend(a , k):
    ext = 1 << (k - 1)
    assert a < ext , "extend error"
    yield a
    yield a | ext 

# check bits_k factor after mask
def check(k , p , q , n , x):
    mask = (1 << k) - 1
    p &= mask
    q &= mask
    n &= mask
    pq = (p * q) & mask

    return pq == n and p ^ q == (x & mask)

def factor(n , x):
    trace = set([(p , q) for p in [0 , 1] for q in [0 , 1]
            if check(1 , p , q , n , x)])

    bits = n.bit_length() // 2

    for k in range(2 , bits + 1):
        res = set()
        for sp , sq in trace:
            for tp in extend(sp , k):
                for tq in extend(sq , k):
                    np , nq = sorted([tp , tq])
                    if check(k , np , nq , n , x):
                        res.add((np , nq))
        trace = res

    for p , q in trace:
        if p != 1 and p * q == n:
            return p , q

    assert False , "Factor unknown"

if __name__ == "__main__":
    exec(open("output" , "r").read())
    p , q = factor(n , x)

    d = inverse(e , (p - 1) * (q - 1))
    
    f1 = long_to_bytes(pow(c , d , n))
    f2 = (xor(c2.decode("hex") , f1))

    print(f1 + f2)

