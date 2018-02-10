'''
CIS 122 Spring 2016 Project4-1
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: In the loop, Part 1
'''
#0 Population Density Analysis
'''number -> str + number

>>>density_rpt(110,10)
Land density is 11 per square mile.
Area is sparsely populated.

>>>density_rpt(700,2)
Land density is 350 per square mile.
Area is densely populated.
'''
def density_rpt(population,land_area):
    land_dense = round((population)/(land_area))
    if ((land_dense) > 100):
        print("Land density is",int(land_dense),"per square mile. " \
              "Area is densely populated")
    else:
        print("Land density is",int(land_dense),"per square mile. " \
              "Area is sparsely populated")
        return None
    
#1(a) DNA
'''str -> str
>>>transcribe(ACGT)
UGCA
>>>transcribe(TCGA)
AGCU
'''
def transcribe(DNA):
    s = ''
    i=0
    while i<len(DNA):
        if DNA[i] =='A': 
            s = s + 'U'
        if DNA[i] =='C':
            s = s +'G'
        if DNA[i] == 'G':
            s = s + 'C'
        if DNA[i] == 'T':
            s = s +'A'
        i+=1
    return s

#1(b)
'''
str -> str
Only this time instead of a while loop it will be under a for loop.
'''
def transcribe(DNA):
    s = ''
    for i in range (len(DNA)):
        if DNA[i] =='A': 
            s = s + 'U'
        if DNA[i] =='C':
            s = s +'G'
        if DNA[i] == 'G':
            s = s + 'C'
        if DNA[i] == 'T':
            s = s +'A'
    return s
# The for loop is better because the while loop has a risk of going on forever, but the for loop stops at one point.

from turtle import *
import random

#2
def rover_loc():
    return random.randint(-275,275)
    '''() -> integer
    Return rover's "location" - a random integer between -275 and 275.
    For example,     rover_loc()     -195     ''' 
def water_content():
    return random.randint(1,290)
def temp():
    return random.randint(-178,1)
    speed('fastest')
def mars_explore(num_trips):
    '''() -> None
    Function determines next position for exploration, calls functions to collect data, and reports(prints)the results.
    Called by:  mars_explore_main
    Calls: rover_loc, water_content, temp, display
    >>> mars_explore() 
    '''
    xpos = rover_loc()
    ypos = rover_loc()
    setpos(xpos,ypos)
    stamp()
    dot()
    pendown()
    water = water_content()
    temperature = temp()
    write((water,temperature),font=('arial'))
    print(xpos,ypos,water,temperature)
    
# Mars Explorer
def mars_explore_main(num_trips):
    '''() 
    -
    > None
    Main function for mars_explore
    sets up print and graphical
    output and then calls mars_explore.
    Calls:  mars_explore
    >>> mars_explore_main()
    '''
# label print output
    print('xpos', '\t','ypos', '\t','water', '\t','temp')
# set up for graphical output
    reset()
    hideturtle()
    title('Mars Rover')
    display_color = 'blue'
    color(display_color)
# draw the rover
    dot(10, display_color)
# explore twenty places on Mars
    for _ in range(num_trips):
        mars_explore(num_trips)
    return None


