from turtle import *

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
        
def isbn_gendigit(isbn):
    num = 1
    new_num = ''
    add_num = 0
    for i in isbn:
        mult = int(i) * num
        num +=1
        add_num += mult
        
        new_num = new_num + str(i)
    last_num = add_num % 11
    if (add_num + (10 *last_num))%11 == 0:
        print(new_num + str(last_num))

    return None

#(0) (CS Circles) Bridges(a)
def max_trans1(a,b,c):
    x = min(a,b,c) 
    print(x)
    return None
#(0) (b)
def max_trans2(a,b,c,d,e):
    z = min(a,b,c)
    y = min (d,e)
    print(max(z,y))
    return None
