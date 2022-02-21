 # Caesar Cipher

## Description
Why these Crypto challenges are so ez ...

Released : [task.py](./task.py) , [output](./output)

## Task

來讀一下 source code

```python
...
from string import ascii_lowercase as digits , ascii_uppercase as lowercase , digits as uppercase

def caesar_enc(data , key , alpha):
    data = "".join([alpha[(alpha.index(data[i]) + len(alpha) + alpha.index(key[i % len(key)])) % len(alpha)] for i in range(len(data))])
    return data

alpha = lowercase + uppercase + digits + "{_?.}"
flag = caesar_enc(flag , key , alpha)
assert len(key) == 8

...
```

caesar_enc 好像有點醜 但是我太習慣這樣寫了 (#  
從 source code 來看  
enc 就是把 data 在 alpha 的位置 + key 在 alpha 的位置 + alpha 的長度後取餘數

看起來是普通的 caesar 但是可以注意到他是有 key 的  
但是其實有 Key 的 Caesar 就是 Vigenere

同時可以注意到 Key 長度是 8 個  
我們已知的 Flag Format 是 `SCIST{?}`


## Solution

已知 Flag Format 且已知 Key 長度之後就可以用 Known Plaintext 的方式推導 Key  
要注意已知的部分只有 7 個 所以需要爆破一個字 然後從結果猜測哪個才是對的

```python 
#!/usr/bin/python3

from string import (
        ascii_lowercase as digits ,
        ascii_uppercase as lowercase ,
        digits as uppercase
        )

alpha = lowercase + uppercase + digits + "{_?.}"
exec(open("output" , "r").read())

find_key = lambda a , b : alpha[(alpha.index(a) - alpha.index(b)) % len(alpha)] 
decrypt = lambda b , a : alpha[(alpha.index(a) - alpha.index(b)) % len(alpha)] 

know = "SCIST{?}"
key = "" 

for i in range(7):
    key += find_key(flag[i] , know[i])

key += find_key(flag[-1] , know[-1])

for c in alpha:
    tmp = key.replace("}" , c)
    res = ""
    for i in range(len(flag)):
        res += decrypt(tmp[i % len(key)] , flag[i])

    print(f"{tmp} {res}")
```
