# CTRSA

## Description

Warning This is the hardest Crypto challenge (maybe not)

Who says that asymmetric can't use with symmetric.  
I use both of them to encrypt my flag.  
I think it's double security.  

Released : [task.py](./task.py) , [output](./output)

## Task

這題打開會發現 Code 很長  
就先挑重點來看 (全部都是重點 ヽ(ﾟ∀。)ﾉ)  

```python
...
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
...
```

這部分其實不用全部看懂 可以看 n = p * q  那邊去猜 gen 在幹嘛  
實際上 `miller_robin` 這個 function 就是在做 [Miller Rabin 的演算法](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) (錯字是彩蛋啦哈哈)  
主要就只是做強偽證來產生兩個 400 bits 的質數 p , q  
然後這是我第一次刻 Miller Rabin (((

往下看
```python
...

xor = lambda a , b : "".join([chr(ord(i) ^ ord(j)) for i , j in zip(a , b)])

def change_type(i):
    if type(i) == str:
        return int(i.encode("hex") , 16)
    elif type(i) in (int , long):
        return (["0" , ""][len(hex(long(i))) % 2] + hex(long(i))[2:-1]).decode("hex")

...

def encrypt(s , key=key):
    ctr = new(16 , initial_value=change_type(iv)) 
    blow = Blowfish.new(key , mode=Blowfish.MODE_CTR , counter=ctr)

    return blow.encrypt(s)

...

x = xor(encrypt(change_type(p)) , encrypt(change_type(q)))
...
```

`change_type` 只是在做字串跟數值間的轉換  
先把 p q 兩個質數轉成字串後做 encrypt 之後再互相 xor  
這裡就牽涉到第一個考點了  

![](https://upload.wikimedia.org/wikipedia/commons/3/3f/Ctr_encryption.png)

根據 CTR 的 Encryption Flow 來看  
當你 Nonce 跟 Counter 相同的話  
實際上就只是 Plaintext 在做 One Time Pad 而已  
這種狀況稱為 [CTR Nonse Reuse Attack](https://crypto.stackexchange.com/questions/2991/why-must-iv-key-pairs-not-be-reused-in-ctr-mode)  
所以經過 xor 之後 Counter 經過 Encryption 的部分就已經被抵銷了  
我們拿到的 x 實際上就只是 `xor(change_type(p) , change_type(q))`  

往後看就只是把 flag 切成兩部分之後 一個做 RSA Encryption 一個做 One Time Pad
```python
...

def slice(flag):
    leng = len(flag) // 2
    return [flag[:leng] , flag[leng:]]

...

    f1 , f2 = slice(flag)
    c = pow(change_type(f1) , e , n)
    
    c2 = xor(encrypt(f2) , encrypt(f1))

...
```

最後把 x , n , e , c , c2 , iv 寫進 [output](./output)

## Solve

統合一下拿到的資訊  
- <img src="https://latex.codecogs.com/gif.latex?p*q%20%2C%20p%20%5Coplus%20q%20%2C%20f_1%20%5Coplus%20f_2" />  
實際上在拿到 p\*q 跟 p⊕ q 後就可以分解出 p 跟 q 了  

我們只需要確認 LSB 是多少 就可以開始對 bits 往前做 BFS + 剪枝  
我的作法是從 [xor_factor](https://github.com/sliedes/xor_factor ) 這邊學來的  

大概概念就是爆搜每個位置的 bit 之後  
確認在 & mask 的情況下是否符合我們提供的 n 跟 x  
符合就加進 list 裡面 之後再去確認是否有一組是 n 的 factor  

拿到 p q 之後就可以做 RSA Decryption 再做 One Time Pad

```python
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
```

