# BiGGG_RSA

## Description

Seems normal Public Key is too ez for you.  
Let's change it into a bigger value.

Released : [task.py](./task.py) , [output](./output)

## Task

這題主要重點就是這段

```python
n = 1
tmp = getPrime(50)

for i in range(7):
    n *= tmp
    tmp = next_prime(n)
```

我們會得到一個很大的 n  
但是因為我們是直接 n 乘上他的 next_prime  
就會導致中間相差過小 可以直接使用 Fermat Factor

## Solve

From [OAlienO's blog](https://oalieno.github.io/old/algorithm/factoring/fermat/)

![](https://i.imgur.com/rlpw6ni.png)

分解出 n 的因數之後就是簡單的 Decryption 了

```python
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
```

## Another Solution

實際上也可以丟部分工具做分解 Ex. sympy

這邊推薦這個工具  
[Alpertron ECM](https://www.alpertron.com.ar/ECM.HTM)

速度滿快的  
分解這題的速度大概三秒鐘

![](https://i.imgur.com/rQ3nj1t.png)

