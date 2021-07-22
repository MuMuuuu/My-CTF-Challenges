# CarryMe 

## Description

Where the hell is source code ??

Released : [output](./output)

## Task

```
21010011 32111 41021 5313 6220 7234 8163 953 a109 b47 c70 d3a e7b f49 g35 h5a i62 j2a k4f l4f m24 n48 o23 p3k q1n r47 s3b t3a u3k v1h w3p x1g y38 z3k
```

觀察那些數值跟小通靈一下  
可以大概猜到他是每個字轉成不同進位制的結果  
第一個數字就表示是第幾進位制  
出題的方式在 [task](./task.py)

## Solve

全部依照 2 ~ z (36 進位制) 的方式轉換回去  

```python
#!/usr/bin/python

from string import printable

alpha = printable[:36]
f = open("output" , "r").read().strip().split(" ")

res = ""

for i in range(len(f)):
    res += chr(int(f[i][1:] , i + 2))

print(res)
```

