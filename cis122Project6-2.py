'''
CIS 122 Spring 2016 Project6-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Bug, Bug, Bug
'''

#0
def ttriangle(n):
    '''
    (int)-> None
    Prints a right triangle with n lines, 
    where the first line prints 1 'T' and the last line prints n 'T's.
    If n <= 0, do not print anything.             
    None value is returned.
    
    >>> ttriangle(6)
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT

    >>> ttriangle(8)
    T
    TT
    TTT
    TTTT
    TTTTT
    TTTTTT
    TTTTTTT
    TTTTTTTT
    '''
    ct = 1
    while ct <= n:   #ct is also equal to n, because the end row T will be written the name number of times as 'n'.
        print('T' * ct )
        ct += 1  #every line T is added one more time till the last line reaches the 'n' number.
    return None

#1
def find_min_and_max(values):
    '''
    (string) -> None
    Find the maximum and minimum values in a non-empty string of integers and print them.
    None value is returned.
    
    >>> find_min_and_max('438')
    The minimum value is 3
    The maximum value is 8

    >>> find_min_and_max('1023')
    The minimum value is 0
    The maximum value is 
    '''
    mmin = 9 #mmin will now only find the minimum number till 9 not till 0.
    mmax = 0
    for value in values:
        if int(value) > int(mmax): #the value and mmax had to be an integar for the function to determine the largest number in them.
           mmax = value
        if int(value) <= int(mmin): #same here
           mmin = value
    print('The minimum value is', mmin)
    print('The maximum value is', mmax)
    return None
#pulling the two pring and return statement out of the for loop gave the correct answer.
    #or
    #print('The minimum value is {}'.format(mmin))
    #print('The maximum value is {}'.format(mmax))


#2
def my_average(dataset):
    '''(string) -> float
    returns average of values in input string values,but zeros do not count at all
    >>> my_average('13')
    2.0
    >>> my_average('100')
    0.3333333333333333
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != 0:
            total += int(value)
        count += 1
    avg = total / count
    return avg

#3
def minutesToHours(minutes):
    '''(number) -> float
    convert input minutes to hours; return hours
    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    print(hours)
    return None

def hoursToDays(hours):
    '''(number) -> float
    convert input hours to days; return days
    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24       
    return days

def daysToYears(days):
    '''(number) -> float
    convert input days to years; return years
    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''    
    days = 365
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    '''(int) -> float
    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step.
   
    >>> minutesToYears(1300000)
    2
    >>> >>> minutesToYears(10000003)
    19
    '''
    y = (m/525600) #I was unable to call auxiliary function, but with this formula it is possible to find the answer for minutesToYears
    return round(y)
