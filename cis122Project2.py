'''
CIS 122 Spring 2016 Project2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Hello, Turtle
'''

#(0) Sun shine on a Cloudy Day
from turtle import *
shape ("turtle")
color ("yellow")
begin_fill ()
penup()
circle (109)
end_fill ()
setpos (200,80)
fillcolor ("blue")
begin_fill()
circle (1)
end_fill ()
penup()
right(90)

#(1) More Turtle Graphics

#(1a)
setpos(-50,-30)
x = input('Please specify the color for the square: ')
color(x)
begin_fill ()
fd(90)
pendown()
fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)
end_fill()
right(270) 
penup()


#(1b)
y = input('Please specify a color for the triangle: ')
color (y)
begin_fill()
fd(200)
pendown()
fd (120)
lt(120)
fd(120)
lt(120)
fd(120)
end_fill()
right(270)
left(360)
penup()

#(2)
setpos(-300,80)
color('black')
width(5)
pendown()
circle(60)
penup()
setpos(-270,190)
right(60)
pendown()
color('blue')
fd(70)
right(45)
color('green')
fd(50)
penup()
setpos(-270,120)
left(95)
pendown()
color('red')
fd(50)
penup()



