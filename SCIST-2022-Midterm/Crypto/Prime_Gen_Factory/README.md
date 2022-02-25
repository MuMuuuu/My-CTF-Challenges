 # Prime Generate Factory

## Description
一樣忘記存了 笑死

Released : [task.py](./task.py) , [output](./output)

## Task

分段分析一下

```python
gen_list = [getPrime(1011) for i in range(len(flag))]
n_list = [gen_list[i - 1] * gen_list[i] for i in range(len(gen_list))]
```

這邊產了一個 prime list 循環組成 n  
所以可以知道每個 prime 必定會出現兩次 那就可以用 GCD 的方式方解

```python
flag = [bytes_to_long((flag[i - 2] + flag[i - 1] + flag[i]).encode()) for i in range(len(flag))]
```

這邊則是把 flag 三個字取出  
`abcde` -> `[abc , bcd , cde , dea , eab]`

## Solution

知道原理之後就是 coding 而已  
combinations 把所有可能的 n 互相 GCD 分解後就可以一個一個拚 Flag ㄌ

要注意 n 跟 flag 是有 shuffle 過的

```python
#!/usr/bin/python3

from Crypto.Util.number import long_to_bytes , GCD , inverse
from string import printable
from itertools import combinations 

flag = b"SC"
exec(open("output" , "r").read())

res = []
factor = []
for i in combinations(n_list , 2):
     tmp = GCD(i[0] , i[1])
     if tmp != 1 and tmp not in factor:
        factor.append(tmp)

for n , c in zip(n_list , c_list):
    for p in factor:
        if n % p == 0:
            q = n // p
            phi = (p - 1) * (q - 1)
            res.append([c , inverse(e , phi) , n])
            break

while 1:
    for i in res:
        m = long_to_bytes(pow(*i))

        if m[:2] == flag[-2:]:
            flag += chr(m[-1]).encode()
            print(flag)
            del res[res.index(i)]
    if len(flag) == 36:
        print(flag)
        break
```
