'''
CIS 122 Spring 2016 Project5-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: In the loop, part 2
'''
#(0)
def rats(weight, rate):
    '''
    (int, int) -> int
    prints the weight of the rat every week till the weight become 1.5 times its original weight.
    Input rate as a float number, lower then 1.

    >>>rats(90,0.2)
    108.0                    #weight by the end of week 1
    129.6                    #weight by the end of week 2
    155.51999999999998       #weight by the end of week 3
    3                        #number of weeks it took the rat to gain 1.5 times its original weight.
    '''
    new_weight = weight
    weeks = 0
    while new_weight < (1.5 * weight):
        new_weight += (new_weight * rate)
        weeks += 1
        print (new_weight)
    return weeks
print()

#(1a)
def any_uc_alpha(astring):
    '''
    (str) -> Boolean Expression
    Returns True if any of the letters that are input on the parameter 'astring' has an uppercase letter. Returns False if it doesn't.

    >>>any_uc_alpha('star')
    False
    #Returned False because there are no uppercase letter in the word 'star'.

    >>>any_uc_alpha('Star')
    True
    #Returned True because there is an uppercase letter in the word 'Star'.
    
    '''
    for ch in astring:
        if ch.isupper():
            return True
        else:
            return False
print()
    

#(1b)
def two_numbers (astring):
    '''
    (str) -> Boolean Expression
    Returns True if there are atleast two numbers in the input for astring. If there are less then two numbers it will return False.

    >>>two_numbers('CIS122')
    True
    #Returned True because CIS122 has more then two number numbers.

    >>>two_numbers('CIS')
    False
    #Returned False because CIS consists of no numbers.

    >>>two_numbers('CIS1')
    False
    #Returned False because CIS1 consists of only one number.
    '''
    counter = 0
    for ch in astring:
        if ch.isdigit():
            counter += 1
        if counter == 2:
            return True
        else:
            return False
print()

#(1c)
def any_special_char (astring):
    '''
    (str) -> Boolean Expression
    Returns True if there are atleast one special character in the input for astring. Special characters consists of '@','#','$','%','^','&'.
    If there are no special character it will return False.

    >>>any_special_char('CIS')
    False
    #Does not consist of any special character.

    >>>any_special_char('CIS@')
    True
    #Consist of a special character '@'
    '''
    character = ('@','#','$','%','^','&')
    for ch in astring:
        if character in astring:
            return True
        else:
            return False



#Challenge - CS Circles/ Recursion)
def countdownBy2(n):
    '''
    (int) -> int + str
    When an integar is put for the parameter n, numbers are printed from that integar and skips two numbers every time till it gets to zero or the lowest positive integar and prints 'Blastoff!'.

    >>>countdownBy2(7)
    7
    5
    3
    1
    'Blastoff!'

    >>>countdownBy2(10)
    10
    8
    6
    4
    2
    0
    'Blastoff!'
    '''
    if n < 0 :
        print('Blastoff!')
    else:
        print(n)
        countdownBy2(n - 2)
    return None
