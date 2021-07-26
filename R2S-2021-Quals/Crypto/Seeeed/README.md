# Seeeeed

## Description

Seacat700 lost at the time , can you help him get seed of the time to back to TwinkleMoon30 ?

Released : [task.py](./task.py) , [output](./output)

## Task

這題先拆幾個重點

```python
def seeed(t , tmp):
    if t == 0:
        return tmp
    
    tmp = randint(1e10 , 1e20)
    seed(tmp)

    return seeed(t - 1 , tmp)
```

這 function 會做 t 次的 seed(randint(1e10 , 1e20))

```python
m = pow(m , 1 , pow(0x100 , len(flag) - 3))
get = lambda b : (m & (255 << (8 * b))) >> (8 * b)
```

m 做的運算主要是把最前面三個字 `R2S` 去掉  
只是做的方式 tricky 一點  
get 實際上就是取 m 的第 -(b + 1) 個字

```python
p_ls = [int(next_prime(N // seeed(i , t - i))) for i in range(m.bit_length() // 8 + 1)]
q_ls = [getPrime(i.bit_length())  for i in p_ls]
n_ls = [q_ls[i] * p_ls[i] for i in range(len(q_ls))]
c_ls = [encrypt(n_ls[i] , get(i) , e) for i in range(len(n_ls))]
```

接著就是奇特的 prime generation  
看 `p_ls` 的部分就好 p 的產生方式就是 N 除經過 `seed()` t 次之後回傳的 tmp 再 next_prime  
同時因為初始就是 `seed(time)` 所以只要 bf 出 time  
之後的 seed(randint(1e10 , 1e20)) 都是已知的了 就可以知道 n 的 factor

## Solve

只需要簡單的爆破 time 同時 check 是否產出的是正確的 factors

```python
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
```

Timestamp : `Sun Jun 27 10:11:40 2021`

## Unintended Solution

由於 encrypt 的方式是只把每個字單獨拉出來做 RSA Encryption  
所以可以用爆搜 (20 ~ 128) * len(flag - 3) 的方式做 而且比較快

要注意因為 get 是從後面開始取 所以要 reverse 一下 flag

```python
#!/usr/bin/python

exec(open("./output" , "r").read())

flag = ""

for i in range(len(n)):
    for char in range(20 , 128):
        if pow(char , e , n[i]) == c[i]:
            flag += chr(char)
            break

print("R2S" + flag[::-1])
```

我很抱歉 當初沒注意到這件事情 QQ  
有機會的話會在 Final 出 Revenge 的
