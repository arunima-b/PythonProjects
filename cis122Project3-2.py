'''
CIS 122 Spring 2016 Project3-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Form and function, part 2
'''
#(0) Credit card payment
def minimum_payment(a):
    pay1 = max(a*0.025, 15)
    pay2 = min(pay1,a)
    print(pay2)
    return None

#(1a) Turtle Functions
from turtle import *


#(1b)
def poly(sides,length,pcolor):
    fillcolor(pcolor)
    begin_fill()
    angle = 360/sides
    print(angle)
    for i in range(sides):
        fd(length)
        lt(angle)
    end_fill()
    return None

#(1c)
def house():
    poly(4,100, 'green')
    lt(90)
    penup()
    fd(100)
    right(90)
    fd(100)
    lt(120)
    pendown()
    poly(3,100, 'red')
    penup()
    lt(150)
    fd(100)
    right(90)
    fd(32)
    right(90)
    pendown()
    poly(4,35,'yellow')
    return None
        
