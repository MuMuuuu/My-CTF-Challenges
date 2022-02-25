#!/usr/bin/python3

from secret import flag
from Crypto.Util.number import getPrime , bytes_to_long
from random import shuffle

e = 0x10001

gen_list = [getPrime(1011) for i in range(len(flag))]
n_list = [gen_list[i - 1] * gen_list[i] for i in range(len(gen_list))]

flag = [bytes_to_long((flag[i - 2] + flag[i - 1] + flag[i]).encode()) for i in range(len(flag))]

shuffle(n_list)
shuffle(flag)

c_list = [pow(flag[i] , e , n_list[i]) for i in range(len(n_list))]

with open("output" , "w") as f:
    f.write(f"e = {e}\n")
    f.write(f"n_list = {str(n_list)}\n")
    f.write(f"c_list = {str(c_list)}\n")

