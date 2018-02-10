'''
CIS 122 Spring 2016 Project4-1
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Make Good Choices, Part 1
'''
#(0) OK or Not OK?
#(0a)
''' len(str) -> str

The funtion longer_then_four will return True if whatever is inside the function is atleast 5 characters long.
It will return False if otherwise.

    >>>longer_then_four('red') < 5
    False
    >>>longer_then_four('paper') >== 5 
    True
    
'''
def longer_then_four(word):
    if (len(word)>= 5):
        return True
    else:
        return False
#(0b)
'''
The function not_alpha_numeric() will return True if whatever is inside the function parenthesis contains atleast one alphanumeric character,
It will return False if there are no alphanumeric characters.

    >>>not_alpha_numeric('paper')
    False
    >>>not_alpha_numeric('paper1')
    True
    
'''
def not_alpha_numeric(word):
    if('word'.isalnum()):
        return True
    else:
        return False
 
#(0c)
'''
It will return True if when you input any word inside the function no_e_character() does not contain the characters 'E' or 'e'.
It will return False if it does contain the characters 'E' or 'e'.
    >>> no_e_character('red')
    False
    >>> no_e_character('out')
    True
    
'''
def no_e_character(word):
    if ('E' in (word)) or ('e' in (word)):
        return False
    else:
        return True
#(1)
"""
The function is_safelead will return True if the number of points subtracted to 3 and 0.5 either added or subtracted from it depending if the team ahead has the ball and then squaring the whole result.
If the answer is bigger then the number of points then the team is safe.

>>>is_safelead(12,2,True)
    True
It is true because ((12-3)+0.5)**2 is bigger then 12 the number of points by which the team is ahead.
Also it is assumed that the team that is ahead has the ball so the third parameter is True and 0.5 is added.

>>>is_safelead(2, False, 5)
    False
This will return false because the team that is ahead doesn't have the ball, and the result is less then the number of seconds left in the game.
    
"""
def is_safelead(lead,time,ball):
    number_of_points =lead - 3
    if ball:
        number_of_points += 0.5
    else:
        number_of_points -= 0.5
    result = (number_of_points)**2
    if (result) > (time):
        return True
    else:
        return False
       
    
  
