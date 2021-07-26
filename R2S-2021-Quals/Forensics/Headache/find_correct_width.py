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

