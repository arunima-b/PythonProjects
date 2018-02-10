'''
CIS 122 Spring 2016 Project8-1
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Fun with flies
'''
#0
import doctest
def is_anagram(word1,word2):
    '''
    (str, str) -> bool
    The function is_anagram takes in two parameter word1 and word2.
    If each charactar in word1 in not there in word 2 then it is not an anagram so it will return False.
    Otherwise it will return True.
    
    >>> is_anagram('tar', 'rat')
    True
    >>> is_anagram('abc', 'cba')
    True
    >>> is_anagram('cat', 'dog')
    False
    >>> is_anagram('act', 'cat')
    True
    >>> is_anagram('tar', 'tan')
    False
    >>> is_anagram('iceman', 'cinema')
    True
    >>> is_anagram('algorithm', 'logarithm')
    True
    >>> is_anagram('elephant', 'monkey')
    False
    >>> is_anagram('aabaa', 'bbabb')
    False
    >>> is_anagram('', '')
    True
    >>> is_anagram('', 'check')
    False
    >>> is_anagram('tan', 'atan')
    False
    >>> is_anagram('too', 'ton')
    False
    '''
    for ch in word1:
        if ch not in word2:
            return False
    for ch in word2:
        if ch not in word1:
            return False
    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            return False
    return True

#1
def process_file(f):
    '''
    (file) -> str
    The function process_file will take one parameter that is a name of a text file and will print all the contents inside it.
    >>> process_file(cis122project8-1.txt)
    Favorite Movies:
    Interstellar
    Lord of the Rings
    Harry Potter
    Devil Wears Prada

    >>>>>> process_file('project9.txt')
    Friday Saturday Sunday
    Monday
    Thursday
    Tuesday
    Wednesday
    '''
    with open (f, 'r') as checkf:
        contents = checkf.read()
        print(contents)
    return None
        
