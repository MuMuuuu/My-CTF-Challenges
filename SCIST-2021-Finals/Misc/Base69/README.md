# Base69

## Description

Maybe something good this way.
Oh here's a Base69 , maybe I can use this to charging shell.

> Hint : 0 point
> It's not like Base64 or Base32 , maybe you can try other Bases' Serial Alogrithm.

Released : [output](./output)

## Task

```python
alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?_{}><'
enc = '2hk>t?GBbU_ijB1Xa>pQK69_e1e2n>FCoPL9Zd??x9_y68fvF'
```

這題題目名稱跟 Hint 都已經很佛心的說是 Base 系列然後不是 64 或是 32 了  
所以可以透過 Google 其他 Base 系列的實作方式去試試看

原先想要出 2 的某次方 可是 64 32 16 都有人做過了  
再弄也只會變成 Substitution Cipher 所以就學了 58 下去做

## Solve

實際上 Base58 的實作過程就跟 58 進位制的概念相同  
所以這題就是 69 進位制 可以根據提供的 alpha 去定義數值  
接著喇一喇就可以解掉了  


```python
#!/usr/bin/python

from string import printable
from Crypto.Util.number import long_to_bytes

alpha = printable[:62] + "!?_{}><"
exec(open("output" , "r").read())

enc = enc[::-1]
rec = dict(zip(alpha , range(69)))

res = 0

for i in range(len(enc)):
    res += pow(69 , i) * rec[enc[i]]

print(long_to_bytes(res))
```

