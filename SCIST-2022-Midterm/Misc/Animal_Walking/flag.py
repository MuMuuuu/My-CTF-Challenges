#!/usr/bin/python3

from turtle import *

t = Turtle()
t.color("black")
t.pensize(4)
t.speed(20)

# H
t.up()
t.goto(-320, 0)
t.down()
t.seth(90)
t.forward(70)

t.up()
t.goto(-320, 35)
t.down()
t.right(90)
t.forward(50)
t.up()
t.goto(-270, 70)
t.down()
t.right(90)
t.forward(70)

# E
t.up()
t.goto(-260, 0)
t.down()
t.seth(90)
t.forward(70)
t.right(90)
t.forward(35)
t.up()
t.goto(-260, 35)
t.down()
t.forward(35)
t.up()
t.goto(-260, 0)
t.down()
t.forward(35)

# L
t.up()
t.goto(-210, 70)
t.down()
t.seth(270)
t.forward(70)
t.left(90)
t.forward(35)

# L
t.up()
t.goto(-165, 70)
t.down()
t.seth(270)
t.forward(70)
t.left(90)
t.forward(35)

# O
t.up()
t.goto(-90, 70)
t.down()
t.seth(0)

for i in range(25):
    t.right(15)
    t.forward(10)

# T

t.up()
t.goto(-40 , 70)
t.down()
t.seth(180)
t.backward(60)
t.forward(30)
t.left(90)
t.forward(70)

# U
t.up()
t.goto(30 , 70)
t.down()
t.seth(270)
t.forward(50)

for i in range(12):
    t.left(15)
    t.forward(7)

t.forward(43)

# R
t.up()
t.goto(100, 60)
t.down()
t.seth(270)
t.forward(65)
t.goto(100, 60)
t.right(200)
for i in range(20):
    t.right(15)
    t.forward(6)
t.left(184)
t.forward(55)

# T

t.up()
t.goto(150 , 70)
t.down()
t.seth(180)
t.backward(60)
t.forward(30)
t.left(90)
t.forward(70)

# L
t.up()
t.goto(230, 70)
t.down()
t.seth(270)
t.forward(70)
t.left(90)
t.forward(35)

# E
t.up()
t.goto(290, 0)
t.down()
t.seth(270)
t.right(180)
t.forward(70)
t.right(90)
t.forward(35)
t.up()
t.goto(290, 35)
t.down()
t.forward(35)
t.up()
t.goto(290, 0)
t.down()
t.forward(35)

