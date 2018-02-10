'''
CIS 122 Spring 2016 Project8-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Grab Bag
'''
#(0) (CS Circles) 
def length(s):
    for ch in s.split():
        if len(ch) != 4:
            return False
    return True

def sum_check(s):
    each_char = 0
    for i in s:
        if i != ' ' and i.isdigit():
                each_char += int(i)
    return  each_char % 10 == 0 and each_char != 0

def check(s):
    '''
    (int) -> Bool.
    The function check should go through its one parameter of string s to see if it meets the conditions for it to return True.
    The conditions are:
    The numbers should be in this format "#### #### #### ####"
    The # has to be a digit.
    The sum of the digits is  divisible by 10.    
    Zero is  not considered to be divisible by 10.

    If it doesn't meet this requirement it will return False.
.        
    >>> check('2768 3424 2345 2358')
    False
    >>> check('9384 3495 3297 0121')
    True
    >>> check('1876 0954 325009182')
    False
    >>> check('0000000000000000')
    False
    >>> check('0000 0000 0000 000')
    False
    >>> check('0 0 0 0000000000000')
    False
    >>> check('')
    False
    >>> check('0000 0000')
    False
    >>> check('0123 4567 8902 4568')
    True
    >>> check('0123 4567 89AB EFGH')
    False
    >>> check('0123 4567 89AB 5555')
    False
    '''
   
    return length(s) and sum_check(s)
#1
from calendar import *
def whatDay(date,month,year):
    '''
    (int) -> str
    The function whatDay will take the parameter date, month and the year and will return the exact day of the week.
    >>> whatDay(9,2,1990)
    'Friday'
    >>> whatDay(12,6,1994)
    'Sunday'
    >>> whatDay(12,2,2000)
    'Saturday'
    >>> whatDay(2,2,2012)
    'Thursday'
    >>> whatDay(7,3,2017)
    'Tuesday'
    >>> whatDay(1,9,1980)
    'Monday'
    '''
    day = weekday(year,month,date)
    if day == 0:
        return 'Monday'
    if day == 1:
        return 'Tuesday'
    if day == 2:
        return 'Wednesday'
    if day == 3:
        return 'Thursday'
    if day == 4:
        return 'Friday'
    if day == 5:
        return 'Saturday'
    if day == 6:
        return 'Sunday'
    return day

#2 Text Analysis
def text_analysis(f):
    '''
    (file) -> list
    The function text_analysis will check its parameter f to see if there are any words in the text file that are repeated more then once.
    If it does then it will print the word and the number of times it was repeated.

    >>>text_analysis(cis122Project8-2.txt
    ['Hello', 'Goodbye', 'goodbye', 'hi']
    [2, 1, 1, 2]

    #Hello was repeated twice, Goodbye once, goodbye once and hi was written twice in that text file.
    '''
    with open (f, 'r') as checkf:
        contents = checkf.read()
    lista  = contents.split()
    listb = []
    number = []
    for ch in range(len(lista)):
        if lista[ch] not in listb:
            listb.append(lista[ch])
            number.append(1)
        else:
            ind = listb.index(lista[ch])
            number[ind] += 1
    print(listb)
    print(number)
            
        
        
        
    
