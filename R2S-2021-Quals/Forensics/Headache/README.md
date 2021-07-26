# Headache

## Description

SeaCat009's has some problems , seems like he has been ideologically transformed.
Can you help him to rebuild his head ?

> Hint : 0 point
> CRC32 is not changed

> Hint : 0 point
> Width and Height < 650

Released : [task.png](./task.png)

## Task

這題已經很佛心的告訴了你 CRC32 是不是沒有變的
同時也給了 IHDR 的範圍 所以只需要修改 Header 然後爆搜長寬

## Solve

首先跟正確的 PNG Header 比對

![](https://i.imgur.com/1PHAWHi.png)

![](https://i.imgur.com/Xe5JJnS.png)

改完 Header 開始爆 IHDR

```python
#!/usr/bin/python
from zlib import crc32 
from struct import pack

img = open("task.png" , "r").read().strip()

IHDR   = img[12 : 16]
width  = img[16 : 20]
height = img[20 : 24]
other  = img[24 : 29]
crc    = img[29 : 33]

print("now : {}".format(" ".join(map(lambda i : i.encode("hex") , [IHDR , width , height , other]))))
print("CRC : {}".format(crc.encode("hex")))

for i in range(2 , pow(256 , 2)):
    tmp = pack(">i" , i)
    now = IHDR + tmp + height + other
    res = crc32(now)
    res = pack(">i" , res)

    if res == crc:
        print("New Width : {}".format(tmp.encode("hex")))
        break
```

