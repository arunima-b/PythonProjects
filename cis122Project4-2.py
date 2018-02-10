'''
CIS 122 Spring 2016 Project4-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Mars Rover, Part 2
'''
from turtle import *
import random

#1
def rover_loc():
    return random.randint(-275,275)
def water_content():
    return random.randint(1,290)
def temp():
    return random.randint(-178,1)
def mars_explore ():
    '''
    The x position and y position will be randomly selected from rover_loc to determine its position.
    Once it is printed it will set the location of the x, y, water and temperature position. 
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
    
#0 Mars Explorer
def mars_explore_main():
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
    for _ in range(20):
        mars_explore()
    return None

mars_explore_main()


    

    
