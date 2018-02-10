'''
CIS 122 Spring 2016 Project3-1
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Form and function, part 1
'''
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

#(1)Cricket Chirps: Nature's Thermometer
#(a)
def chirps_to_ftemp(c):
    tempf = c
    print(tempf + 40)
    return None

#(b)
def chirps_to_ctemp(t):
    tempc = t
    print((tempc/3) + 4)
    return None

