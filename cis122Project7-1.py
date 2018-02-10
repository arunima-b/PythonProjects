'''
CIS 122 Spring 2016 Project7-1
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Loops and lists, part-1
'''

#0a,b
def diff_first_last(L):
    '''
    (list) -> boolean
    Precondition:  len(L) >= 2
    Returns True if the first item of the list is different from the last; else returns False.
    >>> diff_first_last([3, 4, 2, 8, 3])
    False
    >>> diff_first_last(['apple', 'banana', 'pear'])
    True
    >>> diff_first_last([4.0, 4.5])
    True
    >>>diff_first_last(['bed','sheet','bed'])
    True
    >>>diff_first_last(['bed','red'])
    '''
    return L[0] == L[-1]
#1
def frequent(psw):
    '''
    str -> bool
    If any of the words in the list of pasw = ['password','Two34!','qwerty','letmein','trustno1','000000','passw0rd'] is in psw then return False, otherwise True
    >>>frequent('red')
    True
    >>>frequent('password')
    False
    >>>frequent('letmein')
    False
    >>>frequent('bed')
    True
    '''
    pasw = ['password','Two34!','qwerty','letmein','trustno1','000000','passw0rd']
    return not(psw in pasw)

#2
def mySum(L):
    '''
    (num) -> num
    It will return the total sum of list of numbers in the parameter L
    >>>mySum([3,2,2])
    10
    >>>mySum([10,3,1])
    14
    >>>mySum([2.1,3,2])
    7.1
    '''
    total = 0
    for numb in L:
        total += numb
    return total
    
