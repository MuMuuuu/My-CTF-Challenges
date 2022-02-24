# Double Meet

## Description
忘記存了 笑死

Hint : Maybe 2² equal to 2 *  2 ?

Released : [task.py](./task.py) , [output](./output)

## Task

```python
...

def extend(s):
    tmp = sum([ord(s[~i]) * pow(256 , len(s) - i - 1) for i in range(len(s))])
    tmp = pow(tmp , 1 , pow(0x100 , 3))
    key = ""

    for i in range(int(log(tmp , 256)) + 1):
        key += chr(tmp % 256)
        tmp >>= 8

    return key[::-1] + key + key[::-1] + key + key[::-1] + "\x00"


def encrypt(key , data , iv):
    assert len(key) == 16
    blow = Blowfish.new(key=key.encode() , mode=Blowfish.MODE_CBC , iv=iv)
    return blow.encrypt(data)

cipher = encrypt(extend(key) , pad(flag , 16) , iv)

...
```

觀察一下 `extend` 會發現他中間做了一長串很噁心的行為  
我們先跳過那邊 注意到他 return 的部分  
再來是 `encrypt` 有 assert key 的長度為 16  
其實稍加推導一下就可以知道他的 `extend` 只是在取一個字串的前 3 個字


## Solution

在注意到 key 其實沒有想像中大的時候就可以開始爆破了  
你可以偷懶猜測我的 key 是用 printable 的 這樣可以減少運算時間

```python
#!/usr/bin/python3

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from math import log

def extend(s):
    tmp = sum([ord(s[~i]) * pow(256 , len(s) - i - 1) for i in range(len(s))])
    tmp = pow(tmp , 1 , pow(0x100 , 3))
    key = ""

    for i in range(int(log(tmp , 256)) + 1):
        key += chr(tmp % 256)
        tmp >>= 8

    return key[::-1] + key + key[::-1] + key + key[::-1] + "\x00"


def decrypt(key , data , iv):
    assert len(key) == 16
    blow = Blowfish.new(key=key.encode() , mode=Blowfish.MODE_CBC , iv=iv)
    return blow.decrypt(data)

exec(open("output" , "r").read())
cipher , iv = [bytes.fromhex(i) for i in [cipher , iv]]

for i in range(1 , 256):
    for j in range(1 , 256):
        for k in range(1 , 256):
            res = decrypt(extend(chr(i) + chr(j) + chr(k)) , cipher , iv)
            if b"SCIST" in res:
                print(res , i + j + k)
                exit()
```

