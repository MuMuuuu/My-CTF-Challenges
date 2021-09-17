#!/usr/bin/python3

print("Welcome ot Python dlrow")
print("Pls tupni a rts to kcehc the galf" , end='')

ls = [94, 86, 76, 44, 100, 72, 44, 115, 92, 47, 114, 122, 64, 126, 123, 114, 46, 113, 64, 86, 42, 64, 75, 119, 44, 109, 90, 64, 43, 113, 102, 64, 119, 43, 92, 116, 44, 109, 42, 32, 98]

s = input(" : ")
assert s.startswith("41, 49, 53, 33, 7b") , s
s = s.split(", ")
s = list(map(lambda i : int(i , 16) , s))

if len(s) != len(ls):
    print("Wait ?tuw")
    exit(-1)
for i in range(len(s)):
    if s[i] ^ 31 != ls[i]:
        print("Dirty rekcaH")
        break
else:
    print("Welcome nimda")
