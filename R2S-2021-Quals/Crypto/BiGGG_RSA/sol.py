#!/usr/bin/python3
from gmpy2 import isqrt , is_square , is_prime
from Crypto.Util.number import long_to_bytes , inverse

exec(open("output" , "r").read())

def fermat(n):
    assert not is_prime(n)

    a = isqrt(n) + 1

    while not is_square(pow(a , 2) - n):
        a += 1

    b = isqrt(pow(a , 2) - n)
    p = a + b
    q = a - b

    assert p * q == n

    return int(p) , int(q)

def dec(primes , e , c):
    phi = 1
    n = 1

    for i in primes:
        phi *= (i - 1)
        n *= i
       
    d = inverse(e , phi)
    m = pow(c , d , n)
    flag = long_to_bytes(m)
    
    return flag.decode("latin-1")

primes = []

for i in range(8):
    try:
        p , n = fermat(n)
        primes.append(p)
    except :
        primes.append(n)
        break

flag = dec(primes , e , c)
print(flag)

