# ECBytes

## Description

There's no desciption :) , just solve that.

## Task

```python=
...

key = urandom(16)
aes = AES.new(key , mode=AES.MODE_ECB)
alpha = printable

with open("alpha" , "wb") as f:
    for i in alpha:
        tmp = aes.encrypt(pad(i.encode() , 16))
        f.write(tmp)

with open("output" , "wb") as f:
    for i in flag:
        tmp = aes.encrypt(pad(i.encode() , 16))
        f.write(tmp)
```

看一下題目
import printable 當作 alpha
把 alpha 每個字拆開然後 padding 之後做 AES ECB Encrypt 寫進 [alpha](/alpha)
然後把 Flag 每個字拆開 Padding Encrypt 寫進 [output](/output)

根據 ECB 的 Encryption Flow 來看

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/ECB_encryption.svg/1920px-ECB_encryption.svg.png)

既然已知每個字 Encrypt 的結果 也已知 Flag 每個字 Encrypt 的結果
那其實就只需要做 Substitution 而已

## Solve

把 alpha 跟 output 分成 16 bytes / block 拆出來
然後建表轉換

```python=
#!/usr/bin/python

from string import printable
from Crypto.Util.Padding import unpad

def split(s):
    return [s[i : i + 16] for i in range(0 , len(s) , 16)]

alpha = open("alpha" , "r").read().strip()
alpha = split(alpha)

dic = dict(zip(alpha , printable))

out = open("output" , "r").read().strip()
out = split(out)

res = ""

for i in out:
    res += dic[i]

print(res)
```


