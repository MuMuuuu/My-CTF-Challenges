#!/usr/bin/python

from random import randint

flag = "AIS3{0h_w0w_se3ms_theS3_ch4l1s_15_t0O_Ez_f0r_YoU}"

ls = []

for i in range(60):
    a = randint(0 , len(flag))
    if len(flag) - a < 5:
        b = a + randint(0 , 1)
    else:
        b = a + randint(2 , 5)
    ls.append('pass.substring({},{}).euqals("{}")'.format(a , b , flag[a : b]))

print("return " + " &&\n".join(ls) + ";")

