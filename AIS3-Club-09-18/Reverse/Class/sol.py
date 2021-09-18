#!/usr/bin/python

f = open("data" , "r").read().strip().split("\n")
f = map(lambda i : i.split(",") , f)

ls = list("?" * 49)

for i in f:
    for j in range(int(i[0]) , int(i[1])):
        try:
            ls[j] = i[2][j - int(i[0])]
        except:
            continue

    print("".join(ls))
