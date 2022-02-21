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

